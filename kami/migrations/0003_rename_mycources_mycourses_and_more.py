# Generated by Django 4.2.3 on 2023-08-12 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kami', '0002_mycources_cource_mycources_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyCources',
            new_name='MyCourses',
        ),
        migrations.RenameField(
            model_name='mycourses',
            old_name='cource',
            new_name='course',
        ),
    ]