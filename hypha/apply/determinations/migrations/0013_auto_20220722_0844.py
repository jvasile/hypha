# Generated by Django 3.2.14 on 2022-07-22 08:44

from django.db import migrations
import wagtail.blocks
import wagtail.blocks.static_block
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('determinations', '0012_auto_20220509_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='determination',
            name='form_fields',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False)), ('word_limit', wagtail.blocks.IntegerBlock(default=1000, label='Word limit'))], group='Fields')), ('markdown_text', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False)), ('word_limit', wagtail.blocks.IntegerBlock(default=1000, label='Word limit'))], group='Fields')), ('char', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('format', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('url', 'URL')], label='Format', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default value', required=False))], group='Fields')), ('text', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False)), ('word_limit', wagtail.blocks.IntegerBlock(default=1000, label='Word limit'))], group='Fields')), ('text_markup', wagtail.blocks.RichTextBlock(group='Fields', label='Section text/header')), ('checkbox', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.BooleanBlock(required=False))], group='Fields')), ('dropdown', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Choice')))], group='Fields')), ('send_notice', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.BooleanBlock(required=False))], group='Fields')), ('determination', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('info', wagtail.blocks.static_block.StaticBlock())], group=' Required')), ('message', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('info', wagtail.blocks.static_block.StaticBlock())], group=' Required'))], default=[], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='determinationform',
            name='form_fields',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False)), ('word_limit', wagtail.blocks.IntegerBlock(default=1000, label='Word limit'))], group='Fields')), ('markdown_text', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False)), ('word_limit', wagtail.blocks.IntegerBlock(default=1000, label='Word limit'))], group='Fields')), ('char', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('format', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('url', 'URL')], label='Format', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default value', required=False))], group='Fields')), ('text', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False)), ('word_limit', wagtail.blocks.IntegerBlock(default=1000, label='Word limit'))], group='Fields')), ('text_markup', wagtail.blocks.RichTextBlock(group='Fields', label='Section text/header')), ('checkbox', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.BooleanBlock(required=False))], group='Fields')), ('dropdown', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Choice')))], group='Fields')), ('send_notice', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.BooleanBlock(required=False))], group='Fields')), ('determination', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('info', wagtail.blocks.static_block.StaticBlock())], group=' Required')), ('message', wagtail.blocks.StructBlock([('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('help_link', wagtail.blocks.URLBlock(label='Help link', required=False)), ('info', wagtail.blocks.static_block.StaticBlock())], group=' Required'))], default=[], use_json_field=True),
        ),
    ]
