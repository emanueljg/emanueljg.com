# Generated by Django 3.2.4 on 2021-08-03 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='_date_posted',
        ),
    ]
