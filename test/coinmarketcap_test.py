import pytest
from cryptotik.coinmarketcap import CoinMarketCap

mcap = CoinMarketCap()

def test_get_ticker():

    assert isinstance(mcap.get_ticker('peercoin'), dict)
    assert 'price_eur' in mcap.get_ticker('peercoin', 'eur')

def test_get_global():
    
    assert isinstance(mcap.get_global(), dict)
    assert 'total_24h_volume_eur' in mcap.get_global('eur')
