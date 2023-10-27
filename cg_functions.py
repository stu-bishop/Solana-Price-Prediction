import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def coin_price(coin_id, days):
    coin = cg.get_coin_market_chart_by_id(coin_id, vs_currency='usd', days=str(days))
    prices = coin['prices']
    market_caps = coin['market_caps']

    ### Loop to create numpy array time series of market cap (M), price (P)
    M = np.nan*np.ones((len(market_caps), ))
    P = np.nan*np.ones((len(market_caps), ))
    tm = np.nan*np.ones((len(market_caps), ))
    for n in range(len(market_caps)):
        mc = market_caps[n]
        p = prices[n]
        M[n] = mc[1]
        P[n] = p[1]
        tm[n] = p[0]

    S = M/P  # Circulating Supply
    time = pd.to_datetime(tm, unit='ms')  # Convert unix time to datetime

    return P, M, S, time 
