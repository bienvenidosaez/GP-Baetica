# -*- encoding: utf-8 -*-


from django.contrib import admin

from .models import Tarea


class TareaAdmin(admin.ModelAdmin):
    list_display = ( 'asunto', 'proyecto', 'de', 'para', 'get_descripcion', 'finalizada')

admin.site.register(Tarea, TareaAdmin)

