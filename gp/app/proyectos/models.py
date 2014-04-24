# -*- encoding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField

from core.models import Auditoria
from app.clientes.models import Cliente


class Proyecto(Auditoria):
	nombre = models.CharField(max_length=150, verbose_name=u'Nombre del proyecto')
	cliente = models.ForeignKey(Cliente, blank=True, null=True)
	f_inicio = models.DateField(verbose_name=u'Fecha de inicio del proyecto')
	descripcion = HTMLField(verbose_name=u'Descripción del proyecto')

	def __unicode__(self):
		return self.nombre