# Generated by Django 5.1.2 on 2024-11-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_newsservice_icon_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
