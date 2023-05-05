# Generated by Django 4.2 on 2023-05-04 19:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0005_ride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='departure_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='rides_participating', to=settings.AUTH_USER_MODEL),
        ),
    ]
