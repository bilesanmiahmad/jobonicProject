from django.apps import AppConfig


class JobonicusersConfig(AppConfig):
    name = 'jobonicusers'

    def ready(self):
        import jobonicusers.signals
