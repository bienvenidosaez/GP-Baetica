# -*- encoding: utf-8 -*-


from django.db import models


class Auditoria(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True