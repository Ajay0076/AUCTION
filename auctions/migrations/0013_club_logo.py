# Generated by Django 4.1.6 on 2023-05-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_club_contactno'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
