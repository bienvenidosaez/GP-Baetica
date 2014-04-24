# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cliente.descripcion'
        db.delete_column(u'clientes_cliente', 'descripcion')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Cliente.descripcion'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.descripcion' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.descripcion'
        db.add_column(u'clientes_cliente', 'descripcion',
                      self.gf('tinymce.models.HTMLField')(),
                      keep_default=False)


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'segundo_apellido': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['clientes']