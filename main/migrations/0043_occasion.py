# Generated by Django 5.1.2 on 2024-11-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_remove_category_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, null=True)),
            ],
        ),
    ]
