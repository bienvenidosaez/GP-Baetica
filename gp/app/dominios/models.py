# -*- encoding: utf-8 -*-

from django.db import models

from tinymce.models import HTMLField

from core.models import Auditoria


class Configuracion(Auditoria):
    ssh = HTMLField(null=True, blank=True)
    bbdd = HTMLField(null=True, blank=True)
    email = HTMLField(null=True, blank=True)
    ftp = HTMLField(null=True, blank=True)
    notas = HTMLField(null=True, blank=True)


class Dominio(Auditoria):
    url = models.URLField(max_length=50)
    ip = models.IPAddressField(null=True, blank=True)
    url_temporal = models.URLField(max_length=50, verbose_name=u'URL Temporal', blank=True, null=True)
    compra = models.DateField(verbose_name=u'Fecha de compra')
    caducidad = models.DateField(verbose_name=u'Fecha de caducidad')
    registrador = models.CharField(max_length=50, verbose_name=u'Registrador')
    configuracion = models.OneToOneField(Configuracion, blank=True, null=True)

    def __unicode__(self):
        return self.url


