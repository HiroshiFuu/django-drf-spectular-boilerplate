from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

import ipaddress
import ipware
import traceback
import requests


def api_response_200(data: dict = {}):
    return Response(data=data, status=status.HTTP_200_OK)


def api_response_201(data: dict = {}):
    return Response(data=data, status=status.HTTP_201_CREATED)


def api_response_204():
    return Response(status=status.HTTP_204_NO_CONTENT)


def api_response_400(error_message: str = '', additional_data: dict = {}):
    data = {'Error': error_message}
    if additional_data:
        data.update(additional_data)
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


def api_response_403(msg: str):
    return Response(data={'Error': msg}, status=status.HTTP_403_FORBIDDEN)


def api_response_500(data: dict = {}):
    return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_client_ip_address(request) -> str:
    """
    Get client IP address as configured by the user.
    The django-ipware package is used for address resolution.
    """

    client_ip_address, _ = ipware.ip.get_client_ip(request)
    return client_ip_address


def get_location_data__from_ip(ip):
    if ipaddress.ip_address(ip).is_private:
        return None, False
    is_success = False
    location_info = {
        'country_name': '',
        'state_prov': '',
        'city': '',
        'latitude': 0,
        'longitude': 0,
    }
    try:
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={settings.IPINFO_TOKEN}&ip={ip}"
        r = requests.get(url, verify=True, timeout=3)
        if r.status_code == 200:
            location_info.update(r.json())
            is_success = True
    except Exception:
        traceback.print_exc()
    return location_info, is_success
