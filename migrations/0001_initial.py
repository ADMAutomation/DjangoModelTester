# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTesterRealModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberField', models.IntegerField()),
                ('numberFieldChoices', models.IntegerField(choices=[(0, 'zero'), (1, 'uno'), (2, 'due')])),
            ],
        ),
        migrations.CreateModel(
            name='ModelTesterRelatedRealModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relatedField', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoModelTester.ModelTesterRealModel')),
            ],
        ),
    ]