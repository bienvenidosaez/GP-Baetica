from django.contrib import admin

from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'primer_apellido', 'segundo_apellido', 'nombre', 'email')

admin.site.register(Cliente, ClienteAdmin)