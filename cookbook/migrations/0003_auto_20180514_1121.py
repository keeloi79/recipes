# Generated by Django 2.0.5 on 2018-05-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='icon',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]