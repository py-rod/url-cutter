# Generated by Django 5.0.2 on 2024-03-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_link', '0007_alter_saveurlshortened_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveurlshortened',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
