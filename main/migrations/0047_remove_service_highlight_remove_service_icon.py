# Generated by Django 5.1.2 on 2024-11-21 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_newscategory_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='highlight',
        ),
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
    ]
