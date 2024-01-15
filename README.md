# django-drf-spectular-boilerplate

A Django RESTfull Framework Boilerplate

## Structure

* settings, urls and wsgi in configuration
* core app for main functions and backend app for rest API
* each API version has its serializer, url and view in its own folder

## Features

* Upgrade to OpenAPI 3.0
* Password is validated against upper, lower and numeric
* Both Token and Bearer are accepted
* Serializer with example is enabled
* check_allowed_versions decorator checks for API version
* authentication_required decorator checks for token authentication

## Additional Packages

* include an one-time link module that able to generate one-time only links

## Extra Scripts

* Dockerfile and compose yaml
* Cython scripts
