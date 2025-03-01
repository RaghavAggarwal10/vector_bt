import vectorbt as vbt 
import datetime
end_date=datetime.datetime.now()
start_date=end_date-datetime.timedelta(days=3)

btc_price=vbt.YFData.download(["BTC-USD","ETH-USD","XMR-USD","ADA-USD"],interval="1m",start=start_date,end=end_date).get("Close")
print(btc_price )
print(type(btc_price))
rsi=vbt.RSI.run(btc_price,window=14)
print(rsi)
print(rsi.rsi)
enteries=rsi.rsi_crossed_below(30)
exits=rsi.rsi_crossed_above(70)
pf=vbt.Portfolio.from_signals(btc_price,enteries,exits)
print(enteries.to_string())
print("Hi")
print(pf.stats())
# this will help us get to know how well our strategy is working and every thing  that our startegy is doing 
print(pf.total_return())#this will help us know hoow well our startegy is performing and what is the return it provided in end if we go with this 
# pf.plot().show()