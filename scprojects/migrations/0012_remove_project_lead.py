# Generated by Django 2.2.6 on 2020-01-23 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scprojects', '0011_project_lead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='lead',
        ),
    ]