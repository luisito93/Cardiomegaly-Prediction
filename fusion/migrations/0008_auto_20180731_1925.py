# Generated by Django 2.0.7 on 2018-07-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0007_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='limit',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]