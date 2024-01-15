from django import http
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as session_login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_http_methods
from django.views.static import serve

from .serializers import *
from .view_imports import *

import logging


User = get_user_model()


logger = logging.getLogger(__name__)


@require_http_methods(['GET', 'POST'])
def index(request):
    if request.user.is_authenticated:
        verions = settings.REST_FRAMEWORK['ALLOWED_VERSIONS']
        return render(request, 'home.html', {'verions': verions})
    else:
        return http.HttpResponseRedirect(reverse('account_login'))


@require_GET
def protected_serve(request, path, document_root=None, show_indexes=False):
    if allowed_ips := getattr(settings, 'ALLOWED_IPS', None):
        found_allowed = False
        for allowed_ip in allowed_ips:
            if request.META['REMOTE_ADDR'] == allowed_ip:
                found_allowed = True
                break
            else:
                allowed_ip_parts = allowed_ip.split('.')
                remote_ip_parts = request.META['REMOTE_ADDR'].split('.')
                matched = True
                for a_i_p, r_i_p in zip(allowed_ip_parts, remote_ip_parts):
                    if a_i_p == '%':
                        continue
                    matched &= a_i_p == r_i_p
                if matched:
                    found_allowed = True
                    break
        if not found_allowed:
            print(f"403: {request.META['REMOTE_ADDR']=}")
            return HttpResponseForbidden('<h1>Forbidden</h1>')
    return serve(request, path, document_root, show_indexes)


class RegistrationView(APIView):

    @extend_schema(description='Create an user', request=AccountSerializer, responses={200: AccountSerializer}, tags=['Account'])
    @check_allowed_versions(version=None)
    @authentication_required(return_user=True)
    def post(self, request, token_user):
        if not token_user.is_staff:
            return api_response_403('Only admins are allowed to create users')
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=serializer.data.get('username'),
                email=serializer.data.get('email'),
                first_name=serializer.data.get('first_name'),
                last_name=serializer.data.get('last_name')
            )
            user.set_password(serializer.data.get('password'))
            user.save()
            return api_response_200(serializer.data)
        return api_response_400(serializer.errors)


class ListUserView(APIView):

    @extend_schema(description='List users', responses={200: UserSerializer(many=True)}, tags=['User'])
    @check_allowed_versions(version=None)
    @authentication_required(return_user=True)
    def get(self, request, token_user):
        queryset = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(queryset, many=True)
        return api_response_200(serializer.data)
