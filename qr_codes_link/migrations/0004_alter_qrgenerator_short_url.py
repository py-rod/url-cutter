# Generated by Django 5.0.2 on 2024-03-31 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_codes_link', '0003_alter_qrgenerator_options_alter_qrgenerator_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrgenerator',
            name='short_url',
            field=models.CharField(blank=True, default='', max_length=300, unique=True),
        ),
    ]
