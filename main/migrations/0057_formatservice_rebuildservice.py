# Generated by Django 5.1.2 on 2024-12-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_remove_newscategory_json_newsservice_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('prompt', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RebuildService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('prompt', models.TextField(null=True)),
            ],
        ),
    ]
