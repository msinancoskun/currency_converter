import json
import requests


API_KEY = 'ad569808e32a64605e44daea'

FROM_CURRENCY = input("from...").upper()
TO_CURRENCY = input("to...").upper()


def create_json_currency():
    with open('currency.json', 'w') as json_file:
        json.dump(currency_dict, json_file, indent=True, sort_keys=True)


def convert(from_cur, to_cur, amount: int):
    if from_cur in currency_dict.keys() and to_cur in currency_dict.keys():
        conversion = float(currency_dict[to_cur]) * amount
        return "1 USD = {} {}".format(conversion, to_cur)


if __name__ == '__main__':
    URL = 'https://v6.exchangerate-api.com/v6/{0}/latest/{1}'.format(API_KEY, FROM_CURRENCY)
    source = requests.get(URL).json()
    currency_dict = {}
    conversion_rates = source['conversion_rates']

    for currency, rate in conversion_rates.items():
        currency_dict[currency] = rate

    print(convert(FROM_CURRENCY, TO_CURRENCY, 100))
