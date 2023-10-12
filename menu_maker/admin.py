from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ('title', 'slug')
    list_display = ('title', 'slug')
