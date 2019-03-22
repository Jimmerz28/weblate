# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0021_auto_20190321_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='set_translation_team',
            new_name='set_language_team',
        ),
        migrations.AlterField(
            model_name='project',
            name='set_language_team',
            field=models.BooleanField(default=True, help_text='Lets Weblate update the "Language-Team" file header of your project.', verbose_name='Set "Language-Team" header'),
        ),
        migrations.AlterField(
            model_name='change',
            name='action',
            field=models.IntegerField(choices=[(0, 'Resource update'), (1, 'Translation completed'), (2, 'Translation changed'), (5, 'New translation'), (3, 'Comment added'), (4, 'Suggestion added'), (6, 'Automatic translation'), (7, 'Suggestion accepted'), (8, 'Translation reverted'), (9, 'Translation uploaded'), (10, 'Glossary added'), (11, 'Glossary updated'), (12, 'Glossary uploaded'), (13, 'New source string'), (14, 'Component locked'), (15, 'Component unlocked'), (16, 'Found duplicated string'), (17, 'Committed changes'), (18, 'Pushed changes'), (19, 'Reset repository'), (20, 'Merged repository'), (21, 'Rebased repository'), (22, 'Failed merge on repository'), (23, 'Failed rebase on repository'), (28, 'Failed push on repository'), (24, 'Parse error'), (25, 'Removed translation'), (26, 'Suggestion removed'), (27, 'Search and replace'), (29, 'Suggestion removed during cleanup'), (30, 'Source string changed'), (31, 'New string added'), (32, 'Bulk status change'), (33, 'Changed visibility'), (34, 'Added user'), (35, 'Removed user'), (36, 'Translation approved'), (37, 'Marked for edit'), (38, 'Removed component'), (39, 'Removed project'), (40, 'Found duplicated language'), (41, 'Renamed project'), (42, 'Renamed component'), (43, 'Moved component'), (44, 'New string to translate'), (45, 'New contributor'), (46, 'New whiteboard message'), (47, 'New component alert'), (48, 'Added new language'), (49, 'Requested new language')], default=2),
        ),
    ]