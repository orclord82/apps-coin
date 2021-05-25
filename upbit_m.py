import pyupbit
import time
import datetime

access_key = "3uKXY0VowEdkoNSFMdu77CaxIefP8Yjc4L1Bq1ys"
secret_key = "0vREi51Gpm78xiuvR8NoxspD9kup2HFPWMgIA6GH"
upbit = pyupbit.Upbit(access_key, secret_key)

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    all=[]
    if ticker == "all":
       
        for a in balances:
            all.append({'key' :a['currency'],'value' :a['balance']})
            
        return all
    else:
        for b in balances:
            
            
            if b['currency'] == ticker:
                if b['balance'] is not None:
                    return float(b['balance'])
                else:
                    return 0
        return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_mi60(ticker):
    """1시간 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=12)
    mi60 = df['close'].rolling(12).mean().iloc[-1]
    return mi60
# 로그인
# upbit = pyupbit.Upbit(access, secret)
# print("autotrade start")

# 자동매매 시작
class b:
    def __init__(self):
        print("Start Coin Trading!!")
        buy_price = 0
        sell_price = 0
        while True:
            try:
                now = datetime.datetime.now()
                start_time = get_start_time("KRW-ETH")
                end_time = start_time + datetime.timedelta(minutes=1)

                if start_time < now < end_time:
                    target_price = get_target_price("KRW-ETH", 0.4)
                    current_price = get_current_price("KRW-ETH")
                    mi60 = get_mi60("KRW-ETH")
                    if target_price < current_price and mi60 < current_price:
                        krw = get_balance("KRW")
                        if krw > 5000:
                            upbit.buy_market_order("KRW-ETH", krw*0.9995)
                          
                            buy_price = current_price
                            print("{}: Coin buy success!! Price: {}".format(now,buy_price))
                    
                else:
                    btc = get_balance("ETH")
                    
                    if btc > 5000/get_current_price("KRW-ETH"):
                        sell_price = get_current_price("KRW-ETH")
                        if buy_price * 1.01 < sell_price:
                            upbit.sell_market_order("KRW-ETH", btc*0.9995)
                            print("{}: Coin sell success!!! Price: {}".format(now,sell_price))
                            print("value : {}".format(sell_price - buy_price))
                        elif buy_price * 0.96 >= sell_price:
                            upbit.sell_market_order("KRW-ETH", btc*0.9995)
                            print("{}: Coin panic sell success... Price: {}".format(now,sell_price))
                            print("value : {}".format(sell_price - buy_price))
                        else:
                            pass
                time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(1)

class a:
    def __init__(self):
        while True:
                for i in range(1000000):
                    time.sleep(0.5)
                    print(i)

    