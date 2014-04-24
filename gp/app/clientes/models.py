# -*- encoding: utf-8 -*-

from django.db import models

from core.models import Auditoria

class Cliente(Auditoria):
    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    primer_apellido = models.CharField(null=True, blank=True, max_length=50, verbose_name=u'Primer Apellido')
    segundo_apellido = models.CharField(null=True, blank=True, max_length=50, verbose_name=u'Segundo Apellido')
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.primer_apellido+' '+self.segundo_apellido+', '+self.nombre
