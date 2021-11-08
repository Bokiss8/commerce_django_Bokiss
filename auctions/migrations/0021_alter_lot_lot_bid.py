# Generated by Django 3.2.9 on 2021-11-03 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_lot_lot_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='lot_bid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lotbid', to='auctions.bid'),
        ),
    ]
