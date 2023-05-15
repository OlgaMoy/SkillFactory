import requests
import json
from config import keys

class APIException(Exception):
    pass

class ValueConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}. Проверьте правильность ввода, воспользуйтесь командой /help')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}. Проверьте правильность написания /values.')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}. Проверьте правильность написания /values.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}. '
                               f'Пожалуйста, введите целое положительное число или дробь через точку - например 3.1.')

        if amount <= 0:
            raise APIException(f'Невозможно конвертировать количество валюты меньше или равное 0. Введите положительное число.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base.lower()]]

        return round(total_base * amount, 2)