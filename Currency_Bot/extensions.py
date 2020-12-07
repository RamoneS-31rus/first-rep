import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class Get_price:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if base == quote:
            raise ConvertionException(f'Одинаковые валюты {base}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}')
        total_base = json.loads(r.content)['rates'][keys[quote]]
        total_base = round(total_base * amount, 2)

        return total_base