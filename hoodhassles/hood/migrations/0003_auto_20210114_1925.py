# Generated by Django 3.1.4 on 2021-01-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20210114_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='date',
            field=models.DateTimeField(),
        ),
    ]