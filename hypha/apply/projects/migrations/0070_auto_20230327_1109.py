# Generated by Django 3.2.18 on 2023-03-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0069_contractpacketfile_contractdocumentcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='uploaded_by_applicant_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='uploaded_by_contractor_at',
            field=models.DateTimeField(null=True),
        ),
    ]
