import yfinance as yf
import datetime


start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime.now().strftime('%Y-%m-%d')

btc_data = yf.download('BTC-USD', start=start_date, end=end_date) #dados btc

btc_data['Media Movel'] = btc_data['Close'].rolling(window=200).mean() #media movel

btc_data['Mayer Multiple'] = btc_data['Close'] / btc_data['Media Movel'] #calculo do indicador

print(btc_data[['Close', 'Media Movel', 'Mayer Multiple']].tail(10))