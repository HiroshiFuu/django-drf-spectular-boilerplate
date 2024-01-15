from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Diamond, Rectangle, Square, Triangle
from .utils import get_choice_from_model


from django.conf.locale.en import formats as en_formats  # isort: skip
en_formats.DATE_FORMAT = "Y-m-d"  # isort: skip


class ShapeAdminMixin(admin.ModelAdmin):
    shape_type = None
    list_filter = ('shape_type',)
    search_fields = ['name']
    readonly_fields = ['created_by', 'created_at', 'modified_by', 'modified_at']

    def get_readonly_fields(self, request, obj=None):
        rf = super().get_readonly_fields(request, obj)
        if obj:
            rf += ['shape_type']
        return rf

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'shape_ptr':
            self.shape_type = get_choice_from_model(db_field.remote_field.field.model)
        if db_field.name == 'shape_type':
            field.initial = self.shape_type
            field.disabled = True
        return field

    def get_list_display(self, request):
        ld = super().get_list_display(request)
        return ['id'] + ld + ['area', 'perimeter']


@admin.register(Triangle)
class TriangleAdmin(ShapeAdminMixin):
    list_display = [
        'side_a',
        'side_b',
        'side_c',
    ]


@admin.register(Rectangle)
class RectangleAdmin(ShapeAdminMixin):
    list_display = [
        'width',
        'height',
    ]


@admin.register(Square)
class SquareAdmin(ShapeAdminMixin):
    list_display = [
        'side',
    ]


@admin.register(Diamond)
class DiamondAdmin(ShapeAdminMixin):
    list_display = [
        'diagonal_1',
        'diagonal_2',
    ]
