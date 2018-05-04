from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
import json

from ..models import Crypto
from ..serializers import CryptoSerializer


# initialize the APIClient app
client = Client()


class GetAllCryptosTest(TestCase):
    """ Test module for GET all main API """
    def setUp(self):
        Crypto.objects.create(
            name='FakeCoin', symbol='FC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )
        Crypto.objects.create(
            name='NewFakeCoin', symbol='NFC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )
        Crypto.objects.create(
            name='ForkFakeCoin', symbol='FFC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )
        Crypto.objects.create(
            name='NewForkFakeCoin', symbol='NFFC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )

    def test_get_all_cryptos(self):
        # get API response
        response = client.get(reverse('get_post_cryptos'))
        # get data from db
        cryptos = Crypto.objects.all()
        serializer = CryptoSerializer(cryptos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCryptoTest(TestCase):
    """ Test module for GET single crypto API """

    def setUp(self):
        self.fakecoin = Crypto.objects.create(
            name='FakeCoin', symbol='FC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )
        self.newfakecoin = Crypto.objects.create(
            name='NewFakeCoin', symbol='NFC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )
        self.forkfakecoin = Crypto.objects.create(
            name='ForkFakeCoin', symbol='FFC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )
        self.newforkfakecoin = Crypto.objects.create(
            name='NewForkFakeCoin', symbol='NFFC', price_usd=0, price_btc=0, volume_usd_24h=0, market_cap_usd=0,
            available_supply=0, total_supply=0, max_supply=0, percent_change_1h=0, percent_change_24h=0,
            percent_change_7d=0, last_updated=0, price_eur=0, volume_eur_24h=0, market_cap_eur=0
        )

    def test_get_valid_single_crypto(self):
        response = client.get(
            reverse('get_delete_update_crypto', kwargs={'pk': self.fakecoin.pk}))
        crypto = Crypto.objects.get(pk=self.fakecoin.pk)
        serializer = CryptoSerializer(crypto)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_crypto(self):
        response = client.get(
            reverse('get_delete_update_crypto', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewCryptoTest(TestCase):
    """ Test module for inserting a new crypto """

    def setUp(self):

        self.valid_payload = {
            'name': 'FartCoin',
            'symbol': 'FART',
            'rank': 0,
            'price_usd': 0,
            'price_btc': 0,
            'volume_usd_24h': 0,
            'market_cap_usd': 0,
            'available_supply': 0,
            'total_supply': 0,
            'max_supply': 0,
            'percent_change_1h': 0,
            'percent_change_24h': 0,
            'percent_change_7d': 0,
            'last_updated': 0,
            'price_eur': 0,
            'volume_eur_24h': 0,
            'market_cap_eur': 0
        }

        self.invalid_payload = {
            'name': '',
            'symbol': '',
            'rank': 0,
            'price_usd': 0,
            'price_btc': 0,
            'volume_usd_24h': 0,
            'market_cap_usd': 0,
            'available_supply': 0,
            'total_supply': 0,
            'max_supply': 0,
            'percent_change_1h': 0,
            'percent_change_24h': 0,
            'percent_change_7d': 0,
            'last_updated': 0,
            'price_eur': 0,
            'volume_eur_24h': 0,
            'market_cap_eur': 0
        }

    def test_create_valid_crypto(self):
        response = client.post(
            reverse('get_post_cryptos'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_crypto(self):
        response = client.post(
            reverse('get_post_cryptos'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleCryptoTest(TestCase):
    """ Test module for updating an existing crypto record """

    def setUp(self):
        self.fart = Crypto.objects.create(
            name='FartCoin', symbol='FART')
        self.poop = Crypto.objects.create(
            name='PoopCoin', symbol='POP')
        self.valid_payload = {
            'name': 'PoopCoin',
            'symbol': 'POOP'
        }
        self.invalid_payload = {
            'name': '',
            'symbol': 'POOP'
        }

    def test_valid_update_crypto(self):
        response = client.put(
            reverse('get_delete_update_crypto', kwargs={'pk': self.poop.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_crypto(self):
        response = client.put(
            reverse('get_delete_update_crypto', kwargs={'pk': self.poop.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleCryptoTest(TestCase):
    """ Test module for deleting an existing crypto record """

    def setUp(self):
        self.fart = Crypto.objects.create(
            name='FartCoin', symbol='FART')
        self.poop = Crypto.objects.create(
            name='PoopCoin', symbol='POOP')

    def test_valid_delete_crypto(self):
        response = client.delete(
            reverse('get_delete_update_crypto', kwargs={'pk': self.poop.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_crypto(self):
        response = client.delete(
            reverse('get_delete_update_crypto', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
