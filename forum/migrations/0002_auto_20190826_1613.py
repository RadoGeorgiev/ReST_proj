# Generated by Django 2.2.4 on 2019-08-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]