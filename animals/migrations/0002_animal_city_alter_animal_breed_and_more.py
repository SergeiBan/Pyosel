# Generated by Django 4.1.5 on 2023-01-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='city',
            field=models.CharField(default='Калининград', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.CharField(choices=[('dogs', 'Собаки'), ('cats', 'Кошки')], max_length=16),
        ),
    ]
