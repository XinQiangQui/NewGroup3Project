# Generated by Django 3.1.7 on 2021-05-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduler', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skills',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
