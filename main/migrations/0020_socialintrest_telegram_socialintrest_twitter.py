# Generated by Django 5.1.2 on 2024-10-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_socialintrest'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialintrest',
            name='telegram',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='socialintrest',
            name='twitter',
            field=models.BooleanField(null=True),
        ),
    ]