# Generated by Django 4.1.5 on 2023-02-09 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0008_animal_accessory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='accessory',
            new_name='accessories',
        ),
    ]
