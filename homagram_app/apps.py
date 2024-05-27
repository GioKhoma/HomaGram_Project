from django.apps import AppConfig


class HomagramAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homagram_app'

    def ready(self):
        import homagram_app.signals
