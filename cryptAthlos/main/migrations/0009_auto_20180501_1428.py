# Generated by Django 2.0.4 on 2018-05-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180430_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='cached',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='crypto',
            name='name_id',
            field=models.CharField(default=0, help_text='Enter Crypto', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crypto',
            name='price_true',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='name',
            field=models.CharField(help_text='Enter crypto', max_length=20),
        ),
    ]
