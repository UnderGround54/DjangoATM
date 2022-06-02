# Generated by Django 3.0 on 2020-01-16 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_Dab', models.CharField(max_length=10)),
                ('lieu', models.CharField(max_length=50)),
                ('nombre_Billet_20000', models.IntegerField()),
                ('nombre_Billet_10000', models.IntegerField()),
                ('nombre_Billet_5000', models.IntegerField()),
                ('id_Agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agence.Agence')),
            ],
        ),
    ]