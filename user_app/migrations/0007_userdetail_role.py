# Generated by Django 3.2.4 on 2022-08-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_alter_userdetail_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='role',
            field=models.TextField(default='guest', max_length=15),
        ),
    ]
