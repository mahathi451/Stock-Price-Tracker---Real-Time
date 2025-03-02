import os

class Config:
    ALERT_METHODS = ['email', 'sms']
    FINANCE_API_KEY = os.getenv('FINANCE_API_KEY', 'demo')
    TWILIO_CONFIG = {
        'account_sid': os.getenv('TWILIO_SID'),
        'auth_token': os.getenv('TWILIO_TOKEN'),
        'from_number': '+1234567890'
    }
    SMTP_CONFIG = {
        'server': 'smtp.gmail.com',
        'port': 587,
        'username': os.getenv('SMTP_USER'),
        'password': os.getenv('SMTP_PASS')
    }
