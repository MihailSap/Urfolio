# Generated by Django 5.0.6 on 2024-06-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cloud_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='figma_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tg_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vk_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
