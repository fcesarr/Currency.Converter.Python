
from ..apis.currency_api import CurrencyApi

class CurrencyService(object):
    def __init__(self, name: str, currency_apis: dict):
        self.__name: str=name
        self.__currency_api: CurrencyApi=currency_apis[name]

    @property
    def name(self):
        return self.__name

    def get_codes(self):
        return self.__currency_api.get_codes()

    def get_latest(self, codes: list[str]):
        return self.__currency_api.get_latest(codes=codes)
