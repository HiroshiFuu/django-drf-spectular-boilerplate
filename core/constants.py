from django.conf import settings

import copy


REST_FRAMEWORK_SETTINGS = getattr(settings, 'REST_FRAMEWORK', None)
ALLOWED_VERSIONS = REST_FRAMEWORK_SETTINGS.get('ALLOWED_VERSIONS', '')

RESPONSE_400_DATA = {
    'status': 400,
    'error': 'BAD REQUEST',
    'message': None
}

RESPONSE_401_DATA = {
    'status': 401,
    'error': 'UNAUTHORIZED',
    'message': None
}

RESPONSE_403_DATA = {
    'status': 403,
    'error': 'FORBIDDEN',
    'message': None
}

RESPONSE_403_AUTH = {
    'status': 403,
    'error': 'FORBIDDEN',
    'message': 'authroization token is required'
}

RESPONSE_403_VERSION = {
    'status': 403,
    'error': 'NOT FOUND',
    'message': 'version number not allowed.'
}

RESPONSE_404_DATA = {
    'status': 404,
    'error': 'NOT FOUND',
    'message': None
}

RESPONSE_404_VERSION = {
    'status': 404,
    'error': 'NOT FOUND',
    'message': 'version number not found'
}

RESPONSE_404_ENDPOINT = {
    'status': 404,
    'error': 'NOT FOUND',
    'message': 'this endpoint does not exist'
}

RESPONSE_500_DATA = {
    'status': 500,
    'error': 'INTERNAL SERVER ERROR',
    'message': None
}


def response_500_data(message: str = None):
    res_data = copy.deepcopy(RESPONSE_500_DATA)
    if message is not None:
        res_data['message'] = message
    return res_data
