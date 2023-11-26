# Generated by Django 4.2.7 on 2023-11-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='variation',
            name='fields',
            field=models.JSONField(default=''),
        ),
    ]
