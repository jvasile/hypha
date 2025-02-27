# Generated by Django 2.2.16 on 2020-09-16 09:36

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('users', '0013_add_approver_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consent_show', models.BooleanField(default=False, verbose_name='Show consent checkbox in login form')),
                ('consent_text', models.CharField(max_length=255)),
                ('consent_help', wagtail.fields.RichTextField()),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'user settings',
            },
        ),
    ]
