# Generated by Django 5.0.3 on 2024-03-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copal_manager', '0004_alter_contrat_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrat',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
    ]
