''' file to get information on stocks'''
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.graph_objects as go

import yfinance as yf
import pandas as pd

def get_stock_price(stock_name) :
    '''returns stock price'''
    stock = yf.Ticker(stock_name)
    price = stock.info['currentPrice']
    return price

def change_since_close(stock_name) :
    ''' gets the change since yesterday's close '''
    stock = yf.Ticker(stock_name)
    cur_price = stock.info['currentPrice']
    yday_close = stock.info['previousClose']
    return cur_price - yday_close

def get_company_logo(stock_name) :
    ''' returns a link to the company's logo'''
    stock = yf.Ticker(stock_name)
    return stock.info['logo_url']

def get_stocks_history(stock_list) :
    ''' to get the stock history of multiple stocks '''
    data = yf.download(tickers = stock_list, threads=True, group_by='column')
    print(data)
    return data

def compare_stocks(stock_name1, stock_name2, time_period) :
    ''' plots two stocks close data'''
    ticker1 = yf.Ticker(stock_name1)
    ticker2 = yf.Ticker(stock_name2)
    data1 = ticker1.history(period=time_period)
    data2 = ticker2.history(period=time_period)
    sb.lineplot(data=data1["Close"])
    sb.lineplot(data=data2["Close"])
    plt.xticks(rotation=30)
    plt.title(f"Closing Prices for {stock_name1} and {stock_name2}")
    plt.show()

def plot_closing_price(stock_name, time_period) :
    ''' plots closing price of the stock in time period '''
    stock = yf.Ticker(stock_name)
    price_data = stock.history(period=time_period)  # 1mo, 6mo, 1y
    sb.lineplot(data=price_data["Close"])  #open, low, high, volume, dividends, stock splits
    sb.set_theme()
    plt.xticks(rotation=30)
    plt.title(f"Closing Prices for {stock_name}")
    plt.show()

def plot_open_price(stock_name, time_period) :
    ''' plots opening price of the stock in time period '''
    stock = yf.Ticker(stock_name)
    price_data = stock.history(period=time_period)
    sb.lineplot(data=price_data["Open"])
    sb.set_theme()
    plt.xticks(rotation=30)
    plt.title(f"Opening Prices for {stock_name}")
    plt.show()

def plot_volume(stock_name, time_period) :
    ''' plots number of shares of the stock in time period '''
    stock = yf.Ticker(stock_name)
    price_data = stock.history(period=time_period)
    sb.lineplot(data=price_data["Volume"])
    sb.set_theme()
    plt.xticks(rotation=30)
    plt.title(f"Volume for {stock_name}")
    plt.show()

def plot_ohlc_lineplot(stock_name, time_period) :
    ''' plots open, high, low, close data for stock_name in time_period but as a lineplot'''
    stock = yf.Ticker(stock_name)
    price_data = stock.history(period=time_period)
    data_preproc = pd.DataFrame({
        'O': price_data['Open'],
        'H': price_data['High'],
        'L': price_data['Low'],
        'C': price_data['Close'], })
    sb.lineplot(data=data_preproc)
    sb.set_theme()
    plt.xticks(rotation=30)
    plt.title(f"OHLC Plot for {stock_name}")
    plt.show()

def plot_ohlc(stock_name, time_period) :
    ''' plots ohlc but in an interactive format  '''
    stock = yf.Ticker(stock_name)
    data = stock.history(period=time_period)
    fig = go.Figure()
    fig = go.Figure(data=go.Ohlc(
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close']))
    fig.update_layout(title = f"{stock_name} Share Price", yaxis_title = 'Stock Price')
    fig.show()

def plot_candlestick(stock_name, time_period) :
    ''' plots in candlestick format  '''
    stock = yf.Ticker(stock_name)
    data = stock.history(period=time_period)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,open = data['Open'],
        high=data['High'], low=data['Low'], close=data['Close'], name = 'Market Data'))
    fig.update_layout(title = f"{stock_name} Share Price", yaxis_title = 'Stock Price')
    fig.show()

def get_yearly_change(stock_name) :
    ''' returns how much the stock price has changed in a year '''
    stock = yf.Ticker(stock_name)
    yearly_change = stock.info['52WeekChange']
    return yearly_change

def get_average(stock_name) :
    ''' returns the average stock price '''
    stock = yf.Ticker(stock_name)
    # average = stock.info['twoHundredDayAverage']
    average = stock.info
    print(average)
    return average

def get_yearly_low(stock_name) :
    ''' returns the lowest price stock_name has been in a year '''
    stock = yf.Ticker(stock_name)
    yearly_change = stock.info['fiftyTwoWeekLow']
    return yearly_change

def get_daily_low(stock_name) :
    ''' returns the lowest price the stock was today '''
    stock = yf.Ticker(stock_name)
    daily_low = stock.info['dayLow']
    return daily_low

def get_bid(stock_name) :
    ''' returns the bid of stock_name '''
    stock = yf.Ticker(stock_name)
    daily_low = stock.info['bid']
    return daily_low

def get_recs(stock_name) :
    ''' returns the reccoemdnations that this stock has received '''
    stock = yf.Ticker(stock_name)
    recs = stock.recommendations
    return recs

def get_dividends(stock_name) :
    ''' returns the dividencds of stock '''
    stock = yf.Ticker(stock_name)
    daily_low = stock.info['dayLow']
    return daily_low

def get_weekly_change(stock_name) :
    ''' plots number of shares of the stock in time period '''
    stock = yf.Ticker(stock_name)
    daily_low = stock.info['dayLow']
    return daily_low

def get_currency(stock_name) :
    ''' plots number of shares of the stock in time period '''
    stock = yf.Ticker(stock_name)
    cur = stock.info['currency']
    return cur

def get_reccomendation_mean(stock_name) :
    ''' gets the reccomendation mean. 1 = strong buy 5 = strong sell'''
    stock = yf.Ticker(stock_name)
    cur = stock.info['recommendationMean']
    return cur

def get_ask(stock_name) :
    ''' gets the ask (lowest price the seller will sell) '''
    stock = yf.Ticker(stock_name)
    cur = stock.info['ask']
    return cur

def get_sustainability(stock_name) :
    ''' returns information on the company's ethical practices '''
    stock = yf.Ticker(stock_name)
    recs = stock.sustainability
    return recs

def percent_increase_today(stock_name) :
    ''' returns what percent the stock has increased today'''
    change = change_since_close(stock_name)
    cur_price = get_stock_price(stock_name)
    return change * 100 / cur_price

