# Generated by Django 4.2.1 on 2023-07-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_consiliu'),
    ]

    operations = [
        migrations.AddField(
            model_name='anunturi',
            name='tip',
            field=models.CharField(blank=True, choices=[('Anunturi', 'Anunturi'), ('Concursuri angajare', 'Concursuri angajare')], max_length=255),
        ),
    ]