# Generated by Django 3.2.9 on 2021-12-13 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_alter_people_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='descs',
            new_name='des',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='imgs',
            new_name='image',
        ),
    ]
