# Generated by Django 2.0 on 2017-12-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_affiliated_links_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='cp_int',
            field=models.IntegerField(default=0),
        ),
    ]
