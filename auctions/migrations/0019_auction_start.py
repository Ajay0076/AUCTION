# Generated by Django 2.2.7 on 2023-05-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auction_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='start',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
