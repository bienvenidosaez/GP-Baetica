# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Dominio.configuracion'
        db.alter_column(u'dominios_dominio', 'configuracion_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dominios.Configuracion'], unique=True, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Dominio.configuracion'
        raise RuntimeError("Cannot reverse this migration. 'Dominio.configuracion' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Dominio.configuracion'
        db.alter_column(u'dominios_dominio', 'configuracion_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dominios.Configuracion'], unique=True))

    models = {
        u'dominios.configuracion': {
            'Meta': {'object_name': 'Configuracion'},
            'actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'bbdd': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'ftp': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'ssh': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dominios.dominio': {
            'Meta': {'object_name': 'Dominio'},
            'actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'caducidad': ('django.db.models.fields.DateField', [], {}),
            'compra': ('django.db.models.fields.DateField', [], {}),
            'configuracion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dominios.Configuracion']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'registrador': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '150'}),
            'url_temporal': ('django.db.models.fields.URLField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dominios']