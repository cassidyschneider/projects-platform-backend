# Generated by Django 2.2.6 on 2019-12-28 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('github_url', models.URLField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('looking_for', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('contributors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to=settings.AUTH_USER_MODEL)),
                ('tech_stack', models.ManyToManyField(to='scprojects.Tag')),
            ],
        ),
    ]
