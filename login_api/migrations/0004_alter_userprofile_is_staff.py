# Generated by Django 4.1.1 on 2022-10-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_api", "0003_rename_create_on_profilefeeditem_created_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="is_staff",
            field=models.BooleanField(default=True),
        ),
    ]
