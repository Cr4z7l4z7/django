# Generated by Django 2.1.1 on 2018-10-28 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp_url', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pics',
            new_name='profile_pic',
        ),
    ]
