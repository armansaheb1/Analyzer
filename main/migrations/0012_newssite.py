# Generated by Django 5.1.1 on 2024-10-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_newsintrest'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField()),
            ],
        ),
    ]
