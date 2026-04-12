import requests;

base_url= 'https://api.fxratesapi.com/latest'
currency = input('Enter currency code: ').upper()
amount = float(input('Enter amount: '))
target = input('Enter target currency code: ').upper()

def convert(amount, currency, target):
    response = requests.get(base_url, params={'base': currency})
    data = response.json()
    rate = data['rates'][target]
    converted = amount * rate
    print(f'{amount} in {currency} equals {converted} in {target}')

convert(amount, currency, target)


