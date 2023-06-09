# Generated by Django 2.2.7 on 2023-05-25 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20230525_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptdeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='No', max_length=20)),
                ('clubname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Club')),
                ('playername', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Player')),
            ],
        ),
    ]
