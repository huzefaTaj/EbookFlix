# Generated by Django 3.2.9 on 2022-05-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0034_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='seoclicks',
            field=models.IntegerField(default=0),
        ),
    ]
