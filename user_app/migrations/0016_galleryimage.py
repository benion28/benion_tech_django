# Generated by Django 3.2.4 on 2022-08-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0015_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=20)),
                ('key', models.CharField(max_length=30)),
            ],
        ),
    ]