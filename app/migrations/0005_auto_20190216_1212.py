# Generated by Django 2.1.7 on 2019-02-16 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190216_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ccount',
            new_name='account',
        ),
    ]
