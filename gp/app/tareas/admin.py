from django.contrib import admin

from .models import Tarea


class TareaAdmin(admin.ModelAdmin):
    list_display = ( 'asunto', 'proyecto', 'de', 'para', 'descripcion', 'finalizada')

admin.site.register(Tarea, TareaAdmin)

