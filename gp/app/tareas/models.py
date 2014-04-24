# -*- encoding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

from core.models import Auditoria
from app.proyectos.models import Proyecto


class Tarea(Auditoria):
    proyecto = models.ForeignKey(Proyecto)
    de = models.ForeignKey(User, verbose_name=u'¿Quien manda la tarea?', related_name='de')
    para = models.ForeignKey(User, verbose_name=u'¿A quién va destinada?', related_name='para')
    asunto = models.CharField(max_length=150, verbose_name=u'Asunto')
    descripcion = HTMLField(verbose_name=u'Descripción')
    finalizada = models.BooleanField(default=False)

    def __unicode__(self):
        return self.asunto

    def get_descripcion(self):
        return self.descripcion

    get_descripcion.allow_tags = True

    class Meta:
        verbose_name = 'Lista de tareas'
        verbose_name_plural = 'Lista de tareas'
