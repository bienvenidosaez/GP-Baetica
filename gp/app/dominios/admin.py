# -*- encoding: utf-8 -*-


from django.contrib import admin

from .models import Configuracion, Dominio


class DominioAdmin(admin.ModelAdmin):
    list_display = ('url', 'compra', 'caducidad', 'ip', 'registrador')
    ordering = ['compra', ]

admin.site.register(Dominio, DominioAdmin)

admin.site.register(Configuracion)
