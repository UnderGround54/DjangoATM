# Generated by Django 3.0 on 2020-02-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carte', '0002_auto_20200116_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='etat_Carte',
            field=models.CharField(max_length=19),
        ),
    ]
