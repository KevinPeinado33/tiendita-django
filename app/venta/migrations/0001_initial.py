# Generated by Django 4.1.7 on 2023-03-07 20:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.UUIDField(default=uuid.UUID('a8591dca-7a73-4432-af6d-88c7d7e88d3a'), editable=False, primary_key=True, serialize=False)),
                ('id_venta', models.IntegerField()),
                ('id_producto', models.IntegerField()),
                ('cantidad', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.UUIDField(default=uuid.UUID('f44217f7-ca5c-4153-99c3-1480a9431cb4'), editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('url_producto', models.CharField(max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.UUIDField(default=uuid.UUID('9164e9fb-464f-4845-860f-80db23958220'), editable=False, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.UUIDField(default=uuid.UUID('7113d76e-957e-49dc-9152-5df3b60ef720'), editable=False, primary_key=True, serialize=False)),
                ('id_usuario', models.IntegerField()),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=200)),
                ('cantidad', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
    ]
