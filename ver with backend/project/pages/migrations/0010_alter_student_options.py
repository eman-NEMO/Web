# Generated by Django 4.0.4 on 2022-05-18 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_rename_students_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['level', 'department', 'status', 'stuId']},
        ),
    ]
