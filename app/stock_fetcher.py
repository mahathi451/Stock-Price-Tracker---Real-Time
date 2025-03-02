import yfinance as yf
from threading import Thread
from time import sleep

class StockMonitor:
    def __init__(self, symbols):
        self.symbols = symbols
        self.prices = {}
        
    def fetch_prices(self):
        while True:
            for symbol in self.symbols:
                ticker = yf.Ticker(symbol)
                data = ticker.history(period='1d')
                self.prices[symbol] = {
                    'current': data['Close'].iloc[-1],
                    'high': data['High'].iloc[-1],
                    'low': data['Low'].iloc[-1]
                }
            sleep(60)  # Update every minute

class AlertSystem:
    def check_alerts(self, symbol, price, alerts):
        for alert_type, value in alerts.items():
            if alert_type == 'above' and price > value:
                self.trigger_alert(symbol, price, value)
            elif alert_type == 'below' and price < value:
                self.trigger_alert(symbol, price, value)
