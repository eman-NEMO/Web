# Generated by Django 4.0.4 on 2022-05-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_com_contact_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=2)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('level', models.IntegerField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
            ],
        ),
    ]
