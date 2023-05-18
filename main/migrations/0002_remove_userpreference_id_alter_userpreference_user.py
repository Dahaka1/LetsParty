# Generated by Django 4.2.1 on 2023-05-18 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userpreference",
            name="id",
        ),
        migrations.AlterField(
            model_name="userpreference",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                primary_key=True,
                serialize=False,
                to="main.user",
                verbose_name="Пользователь",
            ),
        ),
    ]
