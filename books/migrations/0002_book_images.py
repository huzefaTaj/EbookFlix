# Generated by Django 3.2.9 on 2022-04-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='images',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]