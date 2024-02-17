from django.contrib import admin
from new.models import new
class newad(admin.ModelAdmin):
    list_display=('first','second')
admin.site.register(new,newad) 
# Register your models here.
