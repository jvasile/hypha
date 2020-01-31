# Generated by Django 2.2.9 on 2020-01-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0071_update_field_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationbase',
            name='guide_link',
            field=models.URLField(blank=True, help_text='Link to the apply guide.', max_length=255),
        ),
        migrations.AddField(
            model_name='labbase',
            name='guide_link',
            field=models.URLField(blank=True, help_text='Link to the apply guide.', max_length=255),
        ),
    ]
