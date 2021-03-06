# Generated by Django 3.2 on 2021-04-21 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProsPyApp', '0002_organismo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('especificaciontecnica', models.TextField(max_length=200)),
                ('foto1', models.ImageField(upload_to='static/img/')),
                ('foto2', models.ImageField(upload_to='static/img/')),
                ('foto3', models.ImageField(upload_to='static/img/')),
                ('foto4', models.ImageField(upload_to='static/img/')),
                ('estado', models.BooleanField(default=True)),
                ('tiporeactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProsPyApp.tiporeactor')),
            ],
            options={
                'verbose_name': 'reactor',
                'verbose_name_plural': 'reatores',
                'ordering': ['marca'],
            },
        ),
        migrations.CreateModel(
            name='CaBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=200)),
                ('y', models.FloatField(max_length=10)),
                ('ks', models.FloatField(max_length=10)),
                ('umax', models.FloatField(max_length=10)),
                ('ms', models.FloatField(max_length=10)),
                ('f', models.FloatField(max_length=10)),
                ('t', models.FloatField(max_length=10)),
                ('v0', models.FloatField(max_length=10)),
                ('v', models.FloatField(max_length=10)),
                ('vf', models.FloatField(max_length=10)),
                ('so', models.FloatField(max_length=10)),
                ('n', models.FloatField(max_length=10)),
                ('x', models.FloatField(max_length=10)),
                ('organismo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProsPyApp.organismo')),
                ('reactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProsPyApp.reactor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cabatch',
                'verbose_name_plural': 'cabatchs',
                'ordering': ['titulo'],
            },
        ),
    ]
