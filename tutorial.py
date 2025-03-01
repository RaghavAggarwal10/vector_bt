import vectorbt as vbt 


btc_price=vbt.YFData.download("BTC-USD").get("Close")
print(btc_price )
print(type(btc_price))
rsi=vbt.RSI.run(btc_price,window=14)
print(rsi)
print(rsi.rsi)
enteries=rsi.rsi_crossed_below(30)
print(enteries.to_string())