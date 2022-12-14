# Generated by Django 4.1 on 2022-08-29 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_grade_school_remove_user_city_remove_user_pincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('school', 'school'), ('student', 'student')], default='student', max_length=20),
        ),
    ]
