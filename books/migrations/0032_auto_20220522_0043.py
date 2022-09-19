# Generated by Django 3.2.9 on 2022-05-21 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0031_auto_20220522_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='category2',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='category3',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.category3'),
        ),
    ]