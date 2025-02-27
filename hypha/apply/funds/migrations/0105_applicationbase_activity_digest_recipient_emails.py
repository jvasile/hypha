# Generated by Django 3.2.15 on 2022-11-02 20:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0104_show_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationbase',
            name='activity_digest_recipient_emails',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.EmailField(default='', max_length=254),
                blank=True,
                help_text='Comma separated list of emails where a summary of all the activities related to this fund will be sent.',
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name='labbase',
            name='activity_digest_recipient_emails',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.EmailField(default='', max_length=254),
                blank=True,
                help_text='Comma separated list of emails where a summary of all the activities related to this lab will be sent.',
                null=True,
                size=None,
            ),
        ),
    ]
