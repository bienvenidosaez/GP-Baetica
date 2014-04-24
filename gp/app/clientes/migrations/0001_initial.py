# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('primer_apellido', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('segundo_apellido', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('descripcion', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('tinymce.models.HTMLField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'segundo_apellido': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['clientes']