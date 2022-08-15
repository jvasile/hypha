# Generated by Django 2.0.2 on 2018-06-19 08:02

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('determinations', '0002_add_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeterminationMessageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_accepted', wagtail.fields.RichTextField(verbose_name='Accepted')),
                ('request_rejected', wagtail.fields.RichTextField(verbose_name='Rejected')),
                ('request_more_info', wagtail.fields.RichTextField(verbose_name='Needs more info')),
                ('concept_accepted', wagtail.fields.RichTextField(verbose_name='Accepted')),
                ('concept_rejected', wagtail.fields.RichTextField(verbose_name='Rejected')),
                ('concept_more_info', wagtail.fields.RichTextField(verbose_name='Needs more info')),
                ('proposal_accepted', wagtail.fields.RichTextField(verbose_name='Accepted')),
                ('proposal_rejected', wagtail.fields.RichTextField(verbose_name='Rejected')),
                ('proposal_more_info', wagtail.fields.RichTextField(verbose_name='Needs more info')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'determination messages',
            },
        ),
    ]
