# Generated by Django 3.2.2 on 2021-05-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
