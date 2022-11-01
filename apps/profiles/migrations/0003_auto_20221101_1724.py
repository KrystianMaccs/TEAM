# Generated by Django 2.2.10 on 2022-11-01 16:24

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default='NG', max_length=2, verbose_name='Country'),
        ),
    ]
