# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Article.publisher'
        db.add_column('articlefeed_article', 'publisher', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True), keep_default=False)

        # Changing field 'Article.author_name'
        db.alter_column('articlefeed_article', 'author_name', self.gf('django.db.models.fields.CharField')(max_length=80, null=True))


    def backwards(self, orm):
        
        # Deleting field 'Article.publisher'
        db.delete_column('articlefeed_article', 'publisher')

        # Changing field 'Article.author_name'
        db.alter_column('articlefeed_article', 'author_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


    models = {
        'articlefeed.article': {
            'Meta': {'object_name': 'Article'},
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'has_topics_and_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'through': "orm['articlefeed.Topic']", 'to': "orm['articlefeed.Image']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '255'})
        },
        'articlefeed.image': {
            'Meta': {'object_name': 'Image'},
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '255'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'articlefeed.topic': {
            'Meta': {'object_name': 'Topic'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'to': "orm['articlefeed.Article']"}),
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'to': "orm['articlefeed.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['articlefeed']
