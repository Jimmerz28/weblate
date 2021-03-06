# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-07 14:42
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import F, Func, Value


def fix_alert_occurence(apps, schema_editor):
    Alert = apps.get_model("trans", "Alert")
    db_alias = schema_editor.connection.alias
    Alert.objects.using(db_alias).filter(details__contains='"occurences"').update(
        details=Func(
            F("details"),
            Value('"occurences"'),
            Value('"occurrences"'),
            function="replace",
        )
    )


def unfix_alert_occurence(apps, schema_editor):
    Alert = apps.get_model("trans", "Alert")
    db_alias = schema_editor.connection.alias
    Alert.objects.using(db_alias).filter(details__contains='"occurrences"').update(
        details=Func(
            F("details"),
            Value('"occurrences"'),
            Value('"occurences"'),
            function="replace",
        )
    )


class Migration(migrations.Migration):

    dependencies = [("trans", "0015_linked_component_branch")]

    operations = [
        migrations.RunPython(
            fix_alert_occurence, reverse_code=unfix_alert_occurence, elidable=True
        )
    ]
