# Generated by Django 5.0.4 on 2024-06-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_project_course_number_alter_project_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='course_number',
            field=models.CharField(choices=[('1 курс', 'Первый Курс'), ('2 курс', 'Второй Курс'), ('3 курс', 'Третий Курс'), ('4 курс', 'Четвёртый Курс')], max_length=128),
        ),
    ]
