# Generated by Django 4.1.1 on 2022-10-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_api", "0005_userprofile_is_admin"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="is_admin",),
        migrations.AlterField(
            model_name="userprofile",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]