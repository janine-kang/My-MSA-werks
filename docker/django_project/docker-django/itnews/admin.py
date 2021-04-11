from django.contrib import admin
from .models import IT_news
# Register your models here.

class IT_Admin(admin.ModelAdmin):
    pass

admin.site.register(IT_news, IT_Admin)