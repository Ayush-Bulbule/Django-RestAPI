# Generated by Django 4.1.1 on 2022-09-10 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='createed_at',
            new_name='created_at',
        ),
    ]
