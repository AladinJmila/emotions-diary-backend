# Generated by Django 4.2.2 on 2023-07-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0001_rename_coping_mechanism_emotionalstate_coping_mechanisms'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotionalstate',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
