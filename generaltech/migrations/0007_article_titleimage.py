# Generated by Django 2.2.1 on 2022-07-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generaltech', '0006_auto_20220715_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='titleImage',
            field=models.ImageField(default='d', upload_to='file/'),
            preserve_default=False,
        ),
    ]
