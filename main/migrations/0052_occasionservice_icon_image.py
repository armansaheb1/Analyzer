# Generated by Django 5.1.2 on 2024-11-24 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_occasionservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='occasionservice',
            name='icon_image',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
    ]
