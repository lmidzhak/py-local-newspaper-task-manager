# Generated by Django 5.0.6 on 2024-06-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_alter_redactor_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspaperedition",
            name="published_date",
            field=models.DateField(auto_now=True),
        ),
    ]
