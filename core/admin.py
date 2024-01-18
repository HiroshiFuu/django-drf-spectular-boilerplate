
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from django.conf.locale.en import formats as en_formats  # isort: skip
en_formats.DATE_FORMAT = "Y-m-d"  # isort: skip

User = get_user_model()


class UserCustomAdmin(UserAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_superuser=False)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        fieldsets = super().get_fieldsets(request, obj)
        if request.user.is_superuser:
            fieldsets[2][1]['fields'] = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        else:
            fieldsets[2][1]['fields'] = ('is_active', 'is_staff', 'groups')
        return fieldsets

    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff


admin.site.unregister(User)
admin.site.register(User, UserCustomAdmin)
