# Generated by Django 4.0 on 2022-01-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0002_alter_adddatamod_assignment1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddatamod',
            name='average',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adddatamod',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adddatamod',
            name='assignment1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='adddatamod',
            name='assignment2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='adddatamod',
            name='assignment3',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='adddatamod',
            name='assignment4',
            field=models.IntegerField(),
        ),
    ]
