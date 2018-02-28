from django.contrib import admin

# Register your models here.
from webservice.models import sanlp


@admin.register(sanlp)
class sanlpAdmin(admin.ModelAdmin):
    list_display = ('id','p_id','p_name','created_at','modified_at')