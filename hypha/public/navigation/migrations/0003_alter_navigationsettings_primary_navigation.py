# Generated by Django 3.2.14 on 2022-07-22 08:44

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_remove_unused_navigation_elements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationsettings',
            name='primary_navigation',
            field=wagtail.fields.StreamField([('link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False))]))], blank=True, help_text='Main site navigation', use_json_field=True),
        ),
    ]
