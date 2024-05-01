# Generated by Django 4.0 on 2024-02-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BanJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MumbJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
    ]
