# Generated by Django 5.1.2 on 2024-11-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_newsreport_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageservice',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
