# Generated by Django 3.2.19 on 2023-05-31 11:37

import django.core.files.storage
from django.db import migrations, models
import hypha.apply.projects.models.project


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0075_alter_pafapprovals_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractdocumentcategory',
            options={'ordering': ('-required', 'name'), 'verbose_name_plural': 'Contract Document Categories'},
        ),
        migrations.AlterModelOptions(
            name='documentcategory',
            options={'ordering': ('-required', 'name'), 'verbose_name_plural': 'Project Document Categories'},
        ),
        migrations.AlterModelOptions(
            name='packetfile',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='contractdocumentcategory',
            name='required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contractdocumentcategory',
            name='template',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to=hypha.apply.projects.models.project.contract_document_template_path),
        ),
        migrations.AddField(
            model_name='documentcategory',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='documentcategory',
            name='template',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to=hypha.apply.projects.models.project.document_template_path),
        ),
        migrations.AlterField(
            model_name='contractdocumentcategory',
            name='recommended_minimum',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentcategory',
            name='recommended_minimum',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
