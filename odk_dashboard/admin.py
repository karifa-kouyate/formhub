from django.contrib import admin
from . import models

admin.site.register(models.Phone)
admin.site.register(models.GPS)
admin.site.register(models.SurveyType)
admin.site.register(models.ParsedSubmission)
admin.site.register(models.Surveyor)