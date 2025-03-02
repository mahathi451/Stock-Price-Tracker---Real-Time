import smtplib
from twilio.rest import Client
from config import Config

class AlertSystem:
    def __init__(self):
        self.config = Config()
        
    def trigger_alert(self, symbol: str, price: float, threshold: float, alert_type: str):
        message = (f"Alert: {symbol} price ${price:.2f} has crossed "
                  f"{'above' if alert_type == 'above' else 'below'} "
                  f"${threshold:.2f}")
        
        if 'sms' in self.config.ALERT_METHODS:
            self._send_sms(message)
        if 'email' in self.config.ALERT_METHODS:
            self._send_email(message)

    def _send_sms(self, message: str):
        client = Client(self.config.TWILIO_CONFIG['account_sid'],
                       self.config.TWILIO_CONFIG['auth_token'])
        client.messages.create(
            body=message,
            from_=self.config.TWILIO_CONFIG['from_number'],
            to=os.getenv('USER_PHONE')
        )

    def _send_email(self, message: str):
        with smtplib.SMTP(self.config.SMTP_CONFIG['server'], 
                         self.config.SMTP_CONFIG['port']) as server:
            server.starttls()
            server.login(self.config.SMTP_CONFIG['username'],
                        self.config.SMTP_CONFIG['password'])
            server.sendmail(
                from_addr=self.config.SMTP_CONFIG['username'],
                to_addrs=os.getenv('USER_EMAIL'),
                msg=f"Subject: Stock Alert\n\n{message}"
            )
