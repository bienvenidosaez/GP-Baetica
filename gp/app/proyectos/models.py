# -*- encoding: utf-8 -*-

from django.db import models

from core.models import Auditoria


class Proyecto(Auditoria):
	nombre = models.CharField(max_length=150)
    f_inicio = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(max_length=500, blank=True)
    #cliente = models.ForeignKey(Cliente, )