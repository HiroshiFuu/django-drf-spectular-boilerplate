from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'backend'
    verbose_name = 'Backend'

    # def ready(self):
    #     import backend.signals  # noqa
