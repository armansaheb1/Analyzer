# Generated by Django 5.1.2 on 2024-11-21 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_newscategory_alter_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsservice',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.newscategory'),
        ),
    ]
