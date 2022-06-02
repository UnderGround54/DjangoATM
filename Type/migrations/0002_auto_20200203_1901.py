# Generated by Django 3.0 on 2020-02-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Type', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='limite_Montant',
        ),
        migrations.RemoveField(
            model_name='type',
            name='limite_Transaction',
        ),
        migrations.AddField(
            model_name='type',
            name='limite_Montant_Jours',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='type',
            name='limite_Montant_Mois',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='type',
            name='limite_Transaction_Jours',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='type',
            name='limite_Transaction_Mois',
            field=models.IntegerField(),
        ),
    ]