# Generated by Django 5.1.2 on 2024-12-13 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_newssubservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newssubservice',
            name='category',
        ),
        migrations.AddField(
            model_name='newssubservice',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainservices', to='main.newsservice'),
        ),
        migrations.AddField(
            model_name='newssubservice',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subservices', to='main.newssite'),
        ),
    ]
