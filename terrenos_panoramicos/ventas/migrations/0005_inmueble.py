# Generated by Django 3.1.4 on 2021-01-07 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_profile_last_namema'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0004_delete_inmueble'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface', models.DecimalField(decimal_places=10, max_digits=19)),
                ('front', models.DecimalField(decimal_places=10, max_digits=15)),
                ('bottom', models.DecimalField(decimal_places=10, max_digits=15)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('totalprice', models.DecimalField(decimal_places=10, max_digits=19)),
                ('photo', models.ImageField(upload_to='ventas/photos_terrenos')),
                ('creted', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('regimen_propiedad', models.CharField(choices=[('PR', 'Privada'), ('EJ', 'Ejidal'), ('CM', 'Comunal')], default='PR', max_length=2)),
                ('status', models.CharField(choices=[('OF', 'Oferta'), ('SO', 'Solicitud'), ('VD', 'Vendido')], default='SO', max_length=2)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
