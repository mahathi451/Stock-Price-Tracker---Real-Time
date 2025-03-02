from flask import render_template
from app import app, stock_monitor

@app.route('/')
def dashboard():
    return render_template('dashboard.html', 
                         prices=stock_monitor.prices,
                         symbols=stock_monitor.symbols)

@app.route('/set_alert/<symbol>/<alert_type>/<value>')
def set_alert(symbol, alert_type, value):
    # Alert logic here
    return f"Alert set for {symbol} {alert_type} {value}"
