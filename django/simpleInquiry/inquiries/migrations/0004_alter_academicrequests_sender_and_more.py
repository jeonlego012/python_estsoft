# Generated by Django 4.2.5 on 2023-10-05 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inquiries", "0003_alter_academicrequests_receiver_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicrequests",
            name="sender",
            field=models.ForeignKey(
                default=None,
                help_text="Sent By...",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_academic_requests",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="administrativerequests",
            name="sender",
            field=models.ForeignKey(
                default=None,
                help_text="Sent By...",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_admin_requests",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="AcademicReply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(max_length=2000)),
                ("reply_date", models.DateTimeField(auto_now_add=True)),
                (
                    "academic_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inquiries.academicrequests",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="academicrequests",
            name="reply",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="inquiries.academicreply",
            ),
        ),
    ]
