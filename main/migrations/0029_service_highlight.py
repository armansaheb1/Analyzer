# Generated by Django 5.1.2 on 2024-10-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_service_button_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='highlight',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
