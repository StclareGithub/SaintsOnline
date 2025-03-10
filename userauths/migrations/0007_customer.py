# Generated by Django 5.1.5 on 2025-02-28 15:50

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0006_user_avatar_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('userauths.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
