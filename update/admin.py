from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.update_book)
admin.site.register(models.host)
admin.site.register(models.project)
admin.site.register(models.local)
admin.site.register(models.local_project_ship)
admin.site.register(models.history_version)
admin.site.register(models.update_type)