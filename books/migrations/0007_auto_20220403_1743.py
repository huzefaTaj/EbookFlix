# Generated by Django 3.2.9 on 2022-04-03 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
