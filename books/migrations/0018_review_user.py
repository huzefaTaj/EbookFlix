# Generated by Django 3.2.9 on 2022-05-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_alter_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
