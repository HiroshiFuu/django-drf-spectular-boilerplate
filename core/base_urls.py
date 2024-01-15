from django.urls import include, re_path

from dj_rest_auth.urls import urlpatterns
from dj_rest_auth.views import PasswordResetConfirmView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import ListUserView, RegistrationView


from .apps import CoreConfig  # isort: skip
app_name = CoreConfig.name

base_urlpatterns = [
    re_path(r'^dj-rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^dj-rest-auth/', include([url for url in urlpatterns if url.name not in ['account_confirm_email']])),
    re_path(r'^schema/$', SpectacularAPIView.as_view(), name='schema'),
    re_path(r'^schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    re_path(r'users$', ListUserView.as_view(), name='users'),
    re_path(r'registration', RegistrationView.as_view(), name='registration')
]
