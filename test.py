import pyupbit
import time
import datetime

access_key = "3uKXY0VowEdkoNSFMdu77CaxIefP8Yjc4L1Bq1ys"
secret_key = "0vREi51Gpm78xiuvR8NoxspD9kup2HFPWMgIA6GH"
upbit = pyupbit.Upbit(access_key, secret_key)

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute15", count=4)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute15", count=4)
    start_time = df.index[0]
    return start_time

target_price = get_target_price("KRW-ETH", 0.2)
start_time = get_start_time("KRW-ETH")
print(target_price,start_time)