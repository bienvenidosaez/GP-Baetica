# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Configuracion'
        db.create_table(u'dominios_configuracion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('ssh', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('bbdd', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('email', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('ftp', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('notas', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dominios', ['Configuracion'])

        # Adding model 'Dominio'
        db.create_table(u'dominios_dominio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=150)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('url_temporal', self.gf('django.db.models.fields.URLField')(max_length=150, null=True, blank=True)),
            ('compra', self.gf('django.db.models.fields.DateField')()),
            ('caducidad', self.gf('django.db.models.fields.DateField')()),
            ('registrador', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('configuracion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dominios.Configuracion'], unique=True)),
        ))
        db.send_create_signal(u'dominios', ['Dominio'])


    def backwards(self, orm):
        # Deleting model 'Configuracion'
        db.delete_table(u'dominios_configuracion')

        # Deleting model 'Dominio'
        db.delete_table(u'dominios_dominio')


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
            'configuracion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dominios.Configuracion']", 'unique': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'registrador': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '150'}),
            'url_temporal': ('django.db.models.fields.URLField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dominios']