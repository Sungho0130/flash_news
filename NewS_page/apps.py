from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NewS_page'
    def ready(self):
        from .background_play import main
        main()

