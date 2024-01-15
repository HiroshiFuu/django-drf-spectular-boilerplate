from rest_framework import authentication


class BearerAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'


class TokenAuthentication(authentication.TokenAuthentication):
    keyword = 'Token'
