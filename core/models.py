from django.db import models
from django.conf import settings
from django.utils import timezone

from .middleware import get_current_user


class AuditMixin(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(editable=False, auto_now_add=True, verbose_name='Created At')
    modified_at = models.DateTimeField(blank=True, null=True, verbose_name='Modified At')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_created', editable=False, verbose_name='Created By')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_modified', blank=True, null=True, verbose_name='Modified By')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
            if not getattr(self, 'created_by', None):
                self.created_by = get_current_user()
        else:
            self.modified_at = timezone.now()
            if not getattr(self, 'modified_by', None):
                self.modified_by = get_current_user()
        return super().save(*args, **kwargs)
