# Generated by Django 2.2.7 on 2020-01-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_auto_20200117_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img\\'),
        ),
    ]
