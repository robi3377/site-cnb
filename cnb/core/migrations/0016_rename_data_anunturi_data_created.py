# Generated by Django 4.2.1 on 2023-05-25 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_anunturi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anunturi',
            old_name='data',
            new_name='data_created',
        ),
    ]
