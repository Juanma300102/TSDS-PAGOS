# Generated by Django 4.1 on 2022-09-19 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("deudas", "0001_initial"),
        ("suscripciones", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="deuda",
            name="suscripcion",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="suscripciones.suscripcion",
            ),
        ),
    ]
