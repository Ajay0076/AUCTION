# Generated by Django 2.2.7 on 2023-05-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auctionreg_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='deadline',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
