# Generated by Django 4.2.5 on 2023-10-05 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("student", "Student"),
                    ("facilitator", "Facilitator"),
                    ("teamlead", "Teamlead"),
                ],
                max_length=20,
            ),
        ),
    ]
