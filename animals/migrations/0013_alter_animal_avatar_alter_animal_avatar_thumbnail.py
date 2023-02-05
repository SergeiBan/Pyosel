# Generated by Django 4.1.5 on 2023-02-05 14:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0012_animal_avatar_thumbnail_alter_animal_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, scale=None, size=[1920, 1080], upload_to='animals'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='avatar_thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, scale=None, size=[360, 360], upload_to='animals'),
        ),
    ]
