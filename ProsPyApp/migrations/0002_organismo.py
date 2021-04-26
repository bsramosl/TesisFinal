# Generated by Django 3.2 on 2021-04-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProsPyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecientifico', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'organismo',
                'verbose_name_plural': 'organismos',
                'ordering': ['nombrecientifico'],
            },
        ),
    ]