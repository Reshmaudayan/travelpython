# Generated by Django 3.2.9 on 2021-12-11 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_alter_people_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='desc',
            new_name='descs',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='img',
            new_name='imgs',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='names',
        ),
    ]
