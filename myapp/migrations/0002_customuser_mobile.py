# Generated by Django 4.1.3 on 2024-03-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
