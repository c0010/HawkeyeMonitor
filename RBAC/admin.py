from django.contrib import admin

from . import models

admin.site.register(models.Menu)
admin.site.register(models.Permission)
admin.site.register(models.Role)
admin.site.register(models.Area)
admin.site.register(models.Profile)
admin.site.register(models.UserRequest)
