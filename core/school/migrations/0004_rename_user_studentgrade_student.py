# Generated by Django 4.1 on 2022-08-29 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_school_school_alter_user_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentgrade',
            old_name='user',
            new_name='student',
        ),
    ]
