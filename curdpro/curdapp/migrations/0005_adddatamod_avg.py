# Generated by Django 4.0 on 2022-01-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0004_remove_adddatamod_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddatamod',
            name='avg',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
