exec(open('util.py').read())
import yfinance as yf
stock = yf.Ticker("MSFT")
hist = stock.history(period="5y")
array = dataframe_to_list2([hist])
pri(array)