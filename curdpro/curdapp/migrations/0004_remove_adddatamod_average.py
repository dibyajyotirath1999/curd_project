# Generated by Django 4.0 on 2022-01-15 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0003_adddatamod_average_adddatamod_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adddatamod',
            name='average',
        ),
    ]
