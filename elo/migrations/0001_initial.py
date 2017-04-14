# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hemisphire', models.CharField(choices=[('NORTHERN', 'Northern'), ('SOUTHERN', 'Southern')], default='Northern', max_length=10)),
                ('flag_url', models.CharField(max_length=400)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('importance', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.CharField(editable=False, max_length=300, primary_key=True, serialize=False)),
                ('hometeam_score', models.IntegerField()),
                ('awayteam_score', models.IntegerField()),
                ('match_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('calculated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterEmails',
            fields=[
                ('email_address', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RatingTimestamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('dated_rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('image_url', models.CharField(max_length=400)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elo.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=1500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('image_url', models.CharField(max_length=400)),
                ('logo_url', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('website', models.CharField(default='Unknown', max_length=400)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elo.Country')),
                ('stadium', models.ManyToManyField(to='elo.Stadium')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.CharField(max_length=400)),
                ('logo_url', models.CharField(max_length=400)),
                ('countries', models.ManyToManyField(to='elo.Country')),
                ('teams', models.ManyToManyField(blank=True, null=True, related_name='tournaments', to='elo.Team')),
            ],
        ),
        migrations.AddField(
            model_name='ratingtimestamp',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elo.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='awayteam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='elo.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='hometeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='elo.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elo.Tournament'),
        ),
    ]
