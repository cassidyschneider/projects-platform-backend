# Generated by Django 2.2.6 on 2020-01-23 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scprojects', '0005_remove_userprofile_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to='scprojects.UserProfile'),
        ),
    ]
