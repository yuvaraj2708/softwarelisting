# Generated by Django 5.0.1 on 2024-04-27 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listingapp', '0002_softwarelist_is_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwarelist',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
