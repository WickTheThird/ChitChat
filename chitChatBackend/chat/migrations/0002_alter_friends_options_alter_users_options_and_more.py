# Generated by Django 4.1.5 on 2023-05-23 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="friends",
            options={"ordering": ["user"]},
        ),
        migrations.AlterModelOptions(
            name="users",
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="friends",
            name="requestsReceived",
            field=models.ManyToManyField(
                related_name="requests_received", to="chat.users"
            ),
        ),
        migrations.AddField(
            model_name="friends",
            name="requestsSent",
            field=models.ManyToManyField(related_name="requests_sent", to="chat.users"),
        ),
        migrations.CreateModel(
            name="FriendRequest",
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
                (
                    "reciever",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_reciever",
                        to="chat.users",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_sender",
                        to="chat.users",
                    ),
                ),
            ],
        ),
    ]
