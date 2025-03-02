import vectorbt as vbt
import numpy as np
import pandas as pd
import datetime
end_date=datetime.datetime.now()
start_date=end_date-datetime.timedelta(days=2)
btc_price=vbt.YFData.download("BTC-USD",interval="1m",start=start_date,end=end_date).get("Close")
def customer_indicator(close, rsi_window=14, ma_window=50):
    close_5min = close.resample("5T").last().dropna()
    rsi = vbt.RSI.run(close_5min, window=rsi_window).rsi
    rsi = rsi.reindex(close.index).fillna(method="ffill")

    ma = vbt.MA.run(close_5min, ma_window).ma
    ma = ma.reindex(close.index).fillna(method="ffill")

    close = close.to_numpy()
    rsi = rsi.to_numpy()
    ma = ma.to_numpy()

    trend = np.where(rsi > 70, -1, 0)
    trend = np.where((rsi < 30) & (close < ma), 1, trend)

    return trend

ind=vbt.IndicatorFactory( 
    class_name='Combination',
    short_name='comb',
    input_names=["close"],
    param_names=['rsi_window','ma_window'],
    output_names=['value']  ).from_apply_func(customer_indicator,rsi_window=14 ,ma_window=50,keep_pd=True)
res=ind.run(btc_price,  rsi_window=21,ma_window=50)
print(res.value.to_string())
# print(btc_price)
enteries=res.value==1.0
exits=res.value==-1.0
pf=vbt.Portfolio.from_signals(btc_price,enteries,exits)
print(pf.stats())
print(pf.total_return())