# Generated by Django 2.0.4 on 2018-05-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180501_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(help_text='Enter crypto', max_length=20)),
                ('name', models.CharField(help_text='Enter Crypto', max_length=20)),
                ('symbol', models.CharField(help_text='Enter CRYPTO ticker', max_length=10)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('prices_usd', models.FloatField(blank=True, max_length=20, null=True)),
                ('prices_btc', models.FloatField(blank=True, max_length=20, null=True)),
                ('volume_usd_24h', models.FloatField(blank=True, max_length=20, null=True)),
                ('market_usd_cap', models.FloatField(blank=True, max_length=20, null=True)),
                ('available_supply', models.FloatField(blank=True, max_length=20, null=True)),
                ('total_supply', models.FloatField(blank=True, max_length=20, null=True)),
                ('max_supply', models.FloatField(blank=True, max_length=20, null=True)),
                ('percent_change_1h', models.FloatField(blank=True, max_length=20, null=True)),
                ('percent_change_24h', models.FloatField(blank=True, max_length=20, null=True)),
                ('percent_change_7d', models.FloatField(blank=True, max_length=20, null=True)),
                ('last_updated', models.FloatField(blank=True, max_length=20, null=True)),
                ('cached', models.FloatField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True, max_length=20)),
            ],
            options={
                'db_table': 'main',
            },
        ),
        migrations.DeleteModel(
            name='Crypto',
        ),
        migrations.AlterUniqueTogether(
            name='main',
            unique_together={('name', 'symbol')},
        ),
    ]
