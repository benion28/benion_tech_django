# Generated by Django 3.2.4 on 2022-08-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=2000)),
                ('category', models.CharField(max_length=15)),
                ('tag', models.CharField(max_length=15)),
            ],
        ),
    ]
