# Generated by Django 2.2.1 on 2019-05-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190508_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ormcontact',
            name='photo',
            field=models.CharField(max_length=30),
        ),
    ]