# Generated by Django 5.1.2 on 2025-02-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("referrals", "0003_alter_referralclick_identifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referralclick",
            name="page",
            field=models.CharField(max_length=60),
        ),
    ]
