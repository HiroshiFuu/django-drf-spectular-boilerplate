from django.conf import settings
from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext

from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView

from .decorators import authentication_required, check_allowed_versions, exception_wrapper
from .utils import api_response_200, api_response_201, api_response_204, api_response_400, api_response_403, api_response_500

import copy
import json
import os
import traceback
from datetime import datetime


DJANGO_IMPORTS = ['settings', 'FieldDoesNotExist', 'ObjectDoesNotExist', 'timezone', 'gettext', 'Q']
DRF_IMPORTS = ['APIView', 'FormParser', 'MultiPartParser']
SPECTACULAR_IMPORTS = ['extend_schema', 'OpenApiExample']
HELPER_IMPORTS = ['api_response_200', 'api_response_201', 'api_response_204', 'api_response_400', 'api_response_403', 'api_response_500']
DECO_IMPORTS = ['authentication_required', 'check_allowed_versions', 'exception_wrapper']
THIRD_PARTY_IMPORTS = ['copy', 'os', 'traceback', 'datetime']

__all__ = DJANGO_IMPORTS + DRF_IMPORTS + SPECTACULAR_IMPORTS + HELPER_IMPORTS + DECO_IMPORTS + THIRD_PARTY_IMPORTS
