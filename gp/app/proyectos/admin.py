from django.contrib import admin

from .models import Proyecto


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'f_inicio',)

admin.site.register(Proyecto, ProyectoAdmin)