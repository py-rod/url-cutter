# Generated by Django 5.0.2 on 2024-04-03 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_codes_link', '0010_alter_qrgenerator_bg_color_qr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrgenerator',
            name='bg_color_qr',
            field=models.CharField(blank=True, default='#FFFFFF', max_length=200),
        ),
        migrations.AlterField(
            model_name='qrgenerator',
            name='color_qr',
            field=models.CharField(blank=True, default='#00CA7D', max_length=200),
        ),
    ]
