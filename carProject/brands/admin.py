from django.contrib import admin
from . import models

# Register your models here.

class brandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brandName',)}
    list_display = ['brandName', 'slug']

admin.site.register(models.Brands, brandAdmin)