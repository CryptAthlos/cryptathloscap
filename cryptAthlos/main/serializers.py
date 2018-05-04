from rest_framework import serializers
from .models import Main


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'name_id', 'name', 'symbol', 'rank', 'prices_usd', 'prices_btc', 'volume_usd_24h',
                  'market_usd_cap', 'available_supply', 'total_supply', 'max_supply', 'percent_change_1h',
                  'percent_change_24h', 'percent_change_7d', 'cached', 'created_at', 'updated_at')
