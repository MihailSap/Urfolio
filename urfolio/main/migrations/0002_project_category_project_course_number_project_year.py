# Generated by Django 5.0.4 on 2024-05-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('WEBSITE', 'Website'), ('NOVELL', 'Novell'), ('MOBILE_APP', 'Mobile App')], default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='course_number',
            field=models.CharField(choices=[('FIRST', 'First'), ('SECOND', 'Second'), ('THIRD', 'Third'), ('FOURTH', 'Fourth')], default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.CharField(choices=[('FIRST', 'First'), ('SECOND', 'Second'), ('THIRD', 'Third'), ('FOURTH', 'Fourth')], default=1, max_length=128),
            preserve_default=False,
        ),
    ]
