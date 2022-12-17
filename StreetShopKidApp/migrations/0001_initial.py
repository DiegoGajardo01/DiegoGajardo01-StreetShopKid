# Generated by Django 3.2.4 on 2022-11-08 23:50

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('imagen', models.CharField(max_length=250)),
                ('marca', models.CharField(max_length=250)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.IntegerField()),
                ('destacado', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StreetShopKidApp.categoria')),
            ],
            options={
                'verbose_name_plural': 'Producto',
            },
        ),
    ]