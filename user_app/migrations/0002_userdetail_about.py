# Generated by Django 3.2.4 on 2022-08-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='about',
            field=models.CharField(default='', max_length=200),
        ),
    ]