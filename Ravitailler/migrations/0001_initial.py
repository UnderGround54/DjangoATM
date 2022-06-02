# Generated by Django 3.0 on 2020-02-11 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Operateur', '0001_initial'),
        ('Dab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ravitailler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Ravitailler', models.DateTimeField(auto_now_add=True, verbose_name='date de ravitailler')),
                ('nombre_20000_Inserer', models.IntegerField()),
                ('nombre_10000_Inserer', models.IntegerField()),
                ('nombre_5000_Inserer', models.IntegerField()),
                ('id_Dab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dab.Dab')),
                ('id_Operateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operateur.Operateur')),
            ],
        ),
    ]