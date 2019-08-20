import requests

url = 'http://localhost:127.0.0.1/predict_api'
r = requests.post(url, json={'RevBal':11000, 'IntRate':12, 'Installment':300, 'FICO':455})

print(r.json())