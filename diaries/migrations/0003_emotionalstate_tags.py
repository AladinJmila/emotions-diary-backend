# Generated by Django 4.2.2 on 2023-07-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_emotionalstate_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotionalstate',
            name='tags',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
