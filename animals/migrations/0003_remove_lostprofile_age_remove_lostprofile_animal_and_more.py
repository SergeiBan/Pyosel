# Generated by Django 4.1.5 on 2023-02-06 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_remove_animal_price_remove_animal_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostprofile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='lostprofile',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='lostprofile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='lostprofile',
            name='parent',
        ),
        migrations.AddField(
            model_name='animal',
            name='lost_profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animals.lostprofile'),
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('age', models.CharField(max_length=32)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offspring', to='animals.personalprofile')),
            ],
        ),
    ]
