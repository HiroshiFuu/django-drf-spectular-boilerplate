
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from django.conf.locale.en import formats as en_formats  # isort: skip
en_formats.DATE_FORMAT = "Y-m-d"  # isort: skip

User = get_user_model()

admin.site.unregister(User)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_superuser=False)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        if not request.user.is_superuser:
            fieldsets = (
                (None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {
                    'fields': ('is_active', 'is_staff', 'groups', 'user_permissions'),
                }),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )
            if request.user.groups.filter(name='ATS Engineer').exists():
                return (
                    (None, {'fields': ('username', 'password')}),
                    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                )
            return fieldsets
        else:
            return self.fieldsets
