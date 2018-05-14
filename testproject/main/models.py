# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Main(models.Model):

    id = models.AutoField(primary_key=True)
    name_id = models.CharField(max_length=20, help_text="Enter crypto")
    name = models.CharField(max_length=20, help_text="Enter Crypto")
    symbol = models.CharField(max_length=10, help_text="Enter CRYPTO ticker")
    rank = models.CharField(max_length=10, blank=True, null=True)
    prices_usd = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    prices_btc = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    volume_usd_24h = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    market_usd_cap = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    available_supply = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    total_supply = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    max_supply = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    percent_change_1h = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    percent_change_24h = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    percent_change_7d = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    last_updated = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    cached = models.CharField(verbose_name=None, max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    """
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Main, self).save(*args, **kwargs)
    """

    def get_crypto(self):
        return self.symbol

    def __repr__(self):
        return self.symbol + ' added.'

    class Meta:
        unique_together = ["name", "symbol"]
        db_table = 'main'
