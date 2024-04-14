from django.contrib import admin
from .models import Corporation, Software, Version

@admin.register(Corporation)
class CorporationAdmin(admin.ModelAdmin):
    list_display = ('name','year')
    list_filter = ('year',)

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer')
    list_filter = ('developer',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'soft_name')
    list_filter = ('soft_name',)