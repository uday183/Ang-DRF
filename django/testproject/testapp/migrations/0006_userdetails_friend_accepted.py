# Generated by Django 3.1 on 2020-10-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_friendrelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='friend_accepted',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
