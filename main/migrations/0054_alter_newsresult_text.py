# Generated by Django 5.1.2 on 2024-12-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_newsresult_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsresult',
            name='text',
            field=models.TextField(null=True),
        ),
    ]