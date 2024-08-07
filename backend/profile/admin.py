from django.contrib import admin
from profile.models import ReadingProgress, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ReadingProgress)
