# Generated by Django 2.0 on 2017-12-21 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171221_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='price',
            new_name='current_price',
        ),
    ]