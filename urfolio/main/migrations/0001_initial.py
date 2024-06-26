# Generated by Django 5.0.6 on 2024-06-12 20:13

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default-project.png', upload_to='projects_images')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_publication', models.DateField(default=datetime.date.today)),
                ('category', models.CharField(choices=[('WEBSITE', 'Website'), ('NOVELL', 'Novell'), ('MOBILE_APP', 'Mobile App')], max_length=128)),
                ('course_number', models.CharField(choices=[('FIRST', 'First'), ('SECOND', 'Second'), ('THIRD', 'Third'), ('FOURTH', 'Fourth')], max_length=128)),
                ('year', models.CharField(choices=[('FIRST', 'First'), ('SECOND', 'Second'), ('THIRD', 'Third'), ('FOURTH', 'Fourth')], max_length=128)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('slikess', models.ManyToManyField(related_name='likedposts', through='main.LikedPost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='likedpost',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('body', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('parent_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.project')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('body', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.comment')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
