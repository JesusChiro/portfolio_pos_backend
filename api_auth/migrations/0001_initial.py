# Generated by Django 3.2 on 2023-07-01 04:13

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_foto', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('emp_tipo', models.CharField(choices=[('admin', 'Administrador'), ('cajero', 'Cajero'), ('mozo', 'Mozo')], max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_empleado',
            },
        ),
    ]
