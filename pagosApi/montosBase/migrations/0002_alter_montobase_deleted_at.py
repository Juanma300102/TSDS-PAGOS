# Generated by Django 4.1 on 2022-08-29 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("montosBase", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="montobase",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
