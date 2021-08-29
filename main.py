import json
import requests


API_KEY = 'ad569808e32a64605e44daea'
currency_dict = {}


def create_json_currency():
    with open('currency.json', 'w') as json_file:
        json.dump(currency_dict, json_file, indent=True, sort_keys=True)


def convert(from_cur, to_cur, amount: int):
    url = 'https://v6.exchangerate-api.com/v6/{0}/latest/{1}'.format(API_KEY, from_cur)
    source = requests.get(url).json()
    conversion_rates = source['conversion_rates']
    for currency, rate in conversion_rates.items():
        currency_dict[currency] = rate
    if from_cur in currency_dict.keys() and to_cur in currency_dict.keys():
        conversion = float(currency_dict[to_cur]) * amount
        print("{} {} = {:.2f} {}".format(amount, from_cur, conversion, to_cur))


if __name__ == '__main__':
    control = True
    while control:
        try:
            convert(input("from...").upper(), input("to...").upper(), int(input("What is the amount of currency?\n")))
            quit_program = input("Q to quit! Press ENTER to continue...").upper()
            if quit_program == 'Q':
                control = False

        except KeyError:
            print("Currency not found! Try again...")
