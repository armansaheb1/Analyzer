# Generated by Django 5.1.2 on 2024-11-24 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_remove_newsservice_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccasionService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prompt', models.TextField(null=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
