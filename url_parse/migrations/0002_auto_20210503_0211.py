# Generated by Django 3.1.7 on 2021-05-02 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_parse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='ADDRESS',
            new_name='FILE_PATH',
        ),
    ]
