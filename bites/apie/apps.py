from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ApieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apie'

    class Meta:
        verbose_name = _('apie')
        
