# Generated by Django 5.1.1 on 2024-09-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
