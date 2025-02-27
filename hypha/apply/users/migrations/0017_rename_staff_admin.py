
# Generated by Django 2.0.9 on 2018-12-19 13:21
from __future__ import unicode_literals

from django.contrib.auth.models import Group
from django.db import migrations

from hypha.apply.users.groups import TEAMADMIN_GROUP_NAME


def rename_group(apps, schema_editor):
    try:
        team_admin_group = Group.objects.get(name='Team Admin')
    except Group.DoesNotExist:
        pass
    else:
        team_admin_group.name = TEAMADMIN_GROUP_NAME
        team_admin_group.save()


def unrename_group(apps, schema_editor):
    try:
        team_admin_group = Group.objects.get(name=TEAMADMIN_GROUP_NAME)
    except Group.DoesNotExist:
        pass
    else:
        team_admin_group.name = 'Team Admin'
        team_admin_group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_add_finance_group'),
    ]

    operations = [
        migrations.RunPython(rename_group, unrename_group)
    ]
