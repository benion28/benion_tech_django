# Generated by Django 3.2.4 on 2022-08-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0014_auto_20220812_0431'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('key', models.CharField(max_length=30)),
            ],
        ),
    ]
