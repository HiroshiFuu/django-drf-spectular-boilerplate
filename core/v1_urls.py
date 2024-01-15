from django.urls import include, re_path, path

from backend.v1.urls import urlpatterns as backend_url_patterns  # isort: skip

from .base_urls import base_urlpatterns, app_name

urlpatterns = base_urlpatterns + [
    path('', include(backend_url_patterns)),
]
