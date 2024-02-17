from django.contrib import admin
from data.models import Solo1
class dataAdmin(admin.ModelAdmin):
    list_display=('email','password')
admin.site.register(Solo1,dataAdmin) 
# Register your models here.
