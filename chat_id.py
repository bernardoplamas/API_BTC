import requests

TELEGRAM_TOKEN = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
response = requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates')
print(response.json())