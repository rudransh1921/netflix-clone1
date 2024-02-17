from django.contrib import admin
from service.models import Solo
class SoloAdmin(admin.ModelAdmin):
    list_display=('mai1','mai2','mai3')
admin.site.register(Solo,SoloAdmin) 
# Register your models here.
