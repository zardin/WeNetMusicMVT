# Generated by Django 5.0 on 2023-12-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WMusic', '0002_alter_music_musicfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='MusicFile',
            field=models.FileField(upload_to='.'),
        ),
    ]