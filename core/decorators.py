from django.conf import settings

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .constants import ALLOWED_VERSIONS, RESPONSE_403_AUTH, RESPONSE_403_DATA, RESPONSE_403_VERSION, RESPONSE_404_VERSION, response_500_data

import copy
import traceback


def check_allowed_versions(version=None):
    def decorator_wrapper(view_func):
        def func_wrapper(view_obj, request, *args, **kwargs):
            if not request.version:
                return Response(data=RESPONSE_404_VERSION, status=status.HTTP_404_NOT_FOUND)
            if request.version not in ALLOWED_VERSIONS:
                return Response(data=RESPONSE_403_VERSION, status=status.HTTP_403_FORBIDDEN)
            if version and request.version != version:
                return Response(data=RESPONSE_403_VERSION, status=status.HTTP_403_FORBIDDEN)
            return view_func(view_obj, request, *args, **kwargs)
        return func_wrapper
    return decorator_wrapper


def authentication_required(return_user=False, admin_only=False, restrict_admin_msg=''):
    def decorator_wrapper(view_func):
        def func_wrapper(view_obj, request, *args, **kwargs):
            try:
                if token_key := request.auth:
                    token = Token.objects.get(key=token_key)
                    if admin_only:
                        if not token.user.is_staff:
                            res_data = copy.deepcopy(RESPONSE_403_DATA)
                            res_data['Error'] = restrict_admin_msg
                            return Response(data=res_data, status=status.HTTP_403_FORBIDDEN)
                    if return_user:
                        kwargs['token_user'] = token.user
                else:
                    return Response(data=RESPONSE_403_AUTH, status=status.HTTP_403_FORBIDDEN)
            except Exception:
                traceback.print_exc()
                return Response(data=response_500_data(traceback.format_exc()), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return view_func(view_obj, request, *args, **kwargs)
        return func_wrapper
    return decorator_wrapper


def exception_wrapper():
    def decorator_wrapper(view_func):
        def func_wrapper(view_obj, request, *args, **kwargs):
            try:
                return view_func(view_obj, request, *args, **kwargs)
            except Exception:
                request.META['traceback'] = traceback.format_exc()
                traceback.print_exc()
                return Response(data=response_500_data(traceback.format_exc()), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return func_wrapper
    return decorator_wrapper
