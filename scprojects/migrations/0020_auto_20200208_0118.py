# Generated by Django 2.2.6 on 2020-02-08 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scprojects', '0019_auto_20200204_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='looking_for',
            field=models.TextField(blank=True),
        ),
    ]
