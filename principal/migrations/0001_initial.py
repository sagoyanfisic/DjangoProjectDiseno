# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bebida'
        db.create_table('principal_bebida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ingredientes', self.gf('django.db.models.fields.TextField')()),
            ('preparacion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('principal', ['Bebida'])


    def backwards(self, orm):
        # Deleting model 'Bebida'
        db.delete_table('principal_bebida')


    models = {
        'principal.bebida': {
            'Meta': {'object_name': 'Bebida'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredientes': ('django.db.models.fields.TextField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'preparacion': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['principal']