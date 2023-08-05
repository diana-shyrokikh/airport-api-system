# Generated by Django 4.2.4 on 2023-08-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0004_alter_airplane_options_alter_airplanetype_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="airport",
            old_name="city",
            new_name="closest_big_city",
        ),
        migrations.AlterUniqueTogether(
            name="airport",
            unique_together={("name", "closest_big_city")},
        ),
        migrations.AlterField(
            model_name="route",
            name="destination",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="routs_destination",
                to="airport.airport",
            ),
        ),
        migrations.AlterField(
            model_name="route",
            name="source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="routs_source",
                to="airport.airport",
            ),
        ),
    ]
