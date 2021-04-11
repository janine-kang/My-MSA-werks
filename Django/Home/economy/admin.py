from django.contrib import admin
from .models import EconomyNews
# Register your models here.

class EconomyAdmin(admin.ModelAdmin):
    pass

admin.site.register(EconomyNews, EconomyAdmin)