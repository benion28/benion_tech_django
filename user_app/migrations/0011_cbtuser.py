# Generated by Django 3.2.4 on 2022-08-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0010_userdetail_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='CbtUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10)),
                ('className', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('accessCode', models.IntegerField()),
                ('creator', models.IntegerField()),
                ('school', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=30)),
                ('activeExam', models.CharField(max_length=10)),
                ('regType', models.CharField(max_length=10)),
                ('completed', models.BooleanField()),
            ],
        ),
    ]
