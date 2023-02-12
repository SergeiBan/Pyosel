# Generated by Django 4.1.5 on 2023-02-07 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_remove_animal_lost_profile_lostprofile_animal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostprofile',
            name='animal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lost_profile', to='animals.animal'),
        ),
    ]