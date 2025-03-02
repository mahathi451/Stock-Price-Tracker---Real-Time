# 📈 Live Stock Monitor

![Real-time](https://img.shields.io/badge/update%20interval-60s-orange)
![Alerts](https://img.shields.io/badge/notifications-SMS%2FEmail-green)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)

Real-time financial instrument tracker with price alerts and historical analysis.

## 🚀 Features

- 1-minute price updates
- Custom threshold alerts
- 5-year historical data
- Multi-channel notifications
- REST API endpoints

## 🛠 Tech Stack

Component | Technology
---|---
Backend | FastAPI
Data | yfinance, pandas
Alerts | Twilio, SendGrid
Frontend | Plotly Dash

## ⚙️ Setup

git clone https://github.com/yourusername/stock-tracker.git
cd stock-tracker
Install dependencies

pip install -r requirements.txt
Set environment variables

export TWILIO_SID='your_sid'
export TWILIO_TOKEN='your_token'
text

## 🚦 Running the Application

Start server

uvicorn app.main:app --reload
Access dashboard at http://localhost:8000

text

## 📡 API Documentation

Endpoint | Method | Description
---|---|---
`/stocks/{symbol}` | GET | Get real-time data
`/alerts` | POST | Create price alert
`/history/{symbol}` | GET | Get historical data

## 🚨 Alert Configuration Example

{
"symbol": "AAPL",
"alert_type": "above",
"threshold": 150.00,
"channels": ["email", "sms"],
"notification_frequency": "once"
}
text

## 📊 Data Flow Diagram

graph TD
A[Stock Exchanges] --> B(Data Fetcher)
B --> C{Alert Engine}
C --> D[Email]
C --> E[SMS]
C --> F[Webhook]
B --> G[(Database)]
G --> H[Analytics Dashboard]
