# Generated by Django 5.0.2 on 2024-03-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_link', '0004_alter_saveurlshortened_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveurlshortened',
            name='icon',
            field=models.CharField(default='./default/icon_broken.webp', max_length=400),
        ),
        migrations.AddField(
            model_name='saveurlshortened',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='saveurlshortened',
            name='created',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
