# Generated by Django 5.1.2 on 2024-12-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_occasionservice_icon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsresult',
            name='json',
            field=models.JSONField(null=True),
        ),
    ]