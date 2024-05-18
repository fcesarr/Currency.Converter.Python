
from ..apis.currency_api import CurrencyApi

class CurrencyService(object):
    def __init__(self, name:str, currency_apis:dict):
        self.__name=name
        self.__currency_api=currency_apis[name]

    @property
    def name(self):
        return self.__name

    def get_codes(self):
        api:CurrencyApi = self.__currency_api

        return api.get_codes()

    def get_latest(self, codes:list):
        api:CurrencyApi = self.__currency_api

        return api.get_latest(codes=codes)
