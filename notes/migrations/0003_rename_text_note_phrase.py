# Generated by Django 5.2.1 on 2025-05-17 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_test_note_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='text',
            new_name='phrase',
        ),
    ]
