from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Project)
admin.site.register(models.Entry)
