# Generated by Django 5.1.2 on 2024-10-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0004_remove_resolution_name_resolution_resolve'),
    ]

    operations = [
        migrations.AddField(
            model_name='resolution',
            name='name',
            field=models.CharField(default='<Temp_Value>', max_length=255),
        ),
    ]