from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ModelTesterRealModel(models.Model):
    numberField = models.IntegerField()
    numberFieldChoices = models.IntegerField( choices=((0, 'zero'), (1, 'uno'), (2, 'due')) )

class ModelTesterRelatedRealModel(models.Model):
    relatedField = models.ForeignKey(ModelTesterRealModel)
    