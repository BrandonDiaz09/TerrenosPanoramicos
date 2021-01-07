# Generated by Django 3.1.4 on 2021-01-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='status',
            field=models.CharField(choices=[('OF', 'Oferta'), ('SO', 'Solicitud'), ('VD', 'Vendido')], default='SO', max_length=2),
        ),
    ]