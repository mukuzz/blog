# Generated by Django 2.2.1 on 2022-07-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generaltech', '0008_auto_20220720_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
