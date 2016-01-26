# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 21:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('mangaki', '0026_auto_20160108_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('score', models.FloatField()),
                ('nb_ratings', models.PositiveIntegerField()),
                ('nb_stars', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('directors', 'Réalisateurs'), ('authors', 'Auteurs'), ('composers', 'Compositeurs')], max_length=10, unique_for_date='date')),
                ('contents', models.ManyToManyField(through='mangaki.Ranking', to='contenttypes.ContentType')),
            ],
        ),
        migrations.AddField(
            model_name='ranking',
            name='top',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Top'),
        ),
    ]
