# Generated by Django 3.0.5 on 2020-12-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201217_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
