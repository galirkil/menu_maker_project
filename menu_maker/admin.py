from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ('title', 'slug')
    list_display = ('title', 'slug')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    fields = ('title', 'menu', 'path', 'parent_item')
    list_display = ('title', 'menu', 'path', 'parent_item')
