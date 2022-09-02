# Generated by Django 3.2.4 on 2022-08-30 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_area', '0003_auto_20220826_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='value',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='key',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]