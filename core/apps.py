from django.apps import AppConfig

#Configuracion de la app por defecto
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
