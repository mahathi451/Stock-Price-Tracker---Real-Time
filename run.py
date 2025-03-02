from app import app, stock_monitor
from threading import Thread

if __name__ == "__main__":
    # Start price fetching thread
    monitor = StockMonitor(['AAPL', 'GOOGL', 'MSFT'])
    Thread(target=monitor.fetch_prices, daemon=True).start()
    
    app.run(port=5000)
