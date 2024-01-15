# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin

import ipware
from threading import local


# thread local support
_thread_locals = local()


def set_current_user(user):
    """
    Assigns the current user from the request to thread_locals.
    This function is used by CurrentUserMiddleware.
    """
    _thread_locals.user = user


def get_current_user():
    """
    Returns the current user or None
    """
    return getattr(_thread_locals, 'user', None)


def set_current_user_ipaddress(ipaddress):
    _thread_locals.ipaddress = ipaddress


def get_current_user_ipaddress():
    return getattr(_thread_locals, 'ipaddress', None)


class CurrentUserMiddleware(MiddlewareMixin):
    """
    Adds information about the currently logged in user to the thread.
    """

    def process_request(self, request):
        set_current_user(getattr(request, 'user', None))
        client_ip_address, _ = ipware.ip.get_client_ip(request)
        set_current_user_ipaddress(client_ip_address)
