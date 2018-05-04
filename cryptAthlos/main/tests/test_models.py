from django.test import TestCase

from ..models import Crypto


class CryptoTest(TestCase):
    """ Test module for Crypto model """

    def setUp(self):
        Crypto.objects.create(
            name='FakeCoin', symbol='FC', rank=0, price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )
        Crypto.objects.create(
            name='NewFakeCoin', symbol='NFC', rank=0, price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )

    def test_crypto_symbol(self):
        crypto_fakecoin = Crypto.objects.get(name='FakeCoin')
        crypto_newfakecoin = Crypto.objects.get(name='NewFakeCoin')
        self.assertEqual(
            crypto_fakecoin.get_crypto(), 'FC')
        self.assertEqual(
            crypto_newfakecoin.get_crypto(), 'NFC')
