# Generated by Django 2.2.1 on 2019-05-08 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190508_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ormcontact',
            options={'verbose_name': 'ORMContact', 'verbose_name_plural': 'ORMContacts'},
        ),
    ]