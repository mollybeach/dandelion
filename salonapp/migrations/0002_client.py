# Generated by Django 3.2.5 on 2021-07-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salonapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('telephone', models.CharField(max_length=150)),
                ('appointment_date', models.DateTimeField()),
            ],
        ),
    ]