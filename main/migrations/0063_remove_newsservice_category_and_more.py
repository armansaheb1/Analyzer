# Generated by Django 5.1.2 on 2024-12-13 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_remove_newsservice_json_remove_newssubservice_json_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsservice',
            name='category',
        ),
        migrations.RemoveField(
            model_name='newssubservice',
            name='service',
        ),
        migrations.RemoveField(
            model_name='newssubservice',
            name='site',
        ),
    ]