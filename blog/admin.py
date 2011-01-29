from django.contrib.admin import site
from blog import models

site.register(models.Blog)
