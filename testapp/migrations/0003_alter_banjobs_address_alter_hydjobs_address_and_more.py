# Generated by Django 4.0 on 2024-02-26 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_banjobs_mumbjobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banjobs',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mumbjobs',
            name='address',
            field=models.TextField(),
        ),
    ]
