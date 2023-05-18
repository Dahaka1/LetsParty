# Generated by Django 4.2.1 on 2023-05-18 10:52

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("main", "0001_initial"),
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="main.creator",
                verbose_name="Организатор",
            ),
        ),
        migrations.AddField(
            model_name="party",
            name="subculture",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main.subculture",
                verbose_name="Субкультура",
            ),
        ),
        migrations.AddField(
            model_name="party",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Теги",
            ),
        ),
    ]
