# Generated by Django 5.1.2 on 2024-12-18 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_alter_newslink_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newssite',
            name='url',
        ),
    ]
