import unittest
from unittest.mock import MagicMock, Mock
from requests import Response, Timeout
from src.services.currency_service import CurrencyService
from faker import Faker

class CurrencyServiceTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.__faker = Faker()

    def test_name(self):
        excepted :list[str] = self.__generate_code_currencies(20)

        api :Mock = Mock()

        api.get_codes = Mock(return_value=excepted)

        currency_apis = {
            "Api": api
        }

        instance : CurrencyService = CurrencyService(name="Api", currency_apis=currency_apis)

        self.assertEqual(instance.name, "Api")


    def test_get_codes(self):
        excepted :list[str] = self.__generate_code_currencies(20)

        api :Mock = Mock()

        api.get_codes = Mock(return_value=excepted)

        currency_apis = {
            "Api": api
        }

        instance : CurrencyService = CurrencyService(name="Api", currency_apis=currency_apis)

        self.assertEqual(instance.get_codes(), excepted)

    def test_get_codes_throw_same_exception(self):
        message :str = self.__faker.lexify(text='Random Identifier: ??????????')

        api :Mock = Mock()

        api.get_codes = MagicMock(side_effect=Exception(message))

        currency_apis = {
            "Api": api
        }

        instance : CurrencyService = CurrencyService(name="Api", currency_apis=currency_apis)

        with self.assertRaises(Exception) as cm:
            instance.get_codes()

        self.assertEqual(message, str(cm.exception))


    def test_get_latest(self):
        api :Mock = Mock()

        api.get_latest = Mock(return_value=[""])

        currency_apis = {
            "Api": api
        }

        instance : CurrencyService = CurrencyService(name="Api", currency_apis=currency_apis)

        codes :list[str] = self.__generate_code_currencies(20)

        self.assertEqual(instance.get_latest(codes=codes), [""])

    def test_get_latest_throw_same_exception(self):
        message :str = self.__faker.lexify(text='Random Identifier: ??????????')

        api :Mock = Mock()

        api.get_latest = MagicMock(side_effect=Exception(message))

        currency_apis = {
            "Api": api
        }

        instance : CurrencyService = CurrencyService(name="Api", currency_apis=currency_apis)

        codes :list[str] = self.__generate_code_currencies(20)

        with self.assertRaises(Exception) as cm:
            instance.get_latest(codes=codes)

        self.assertEqual(message, str(cm.exception))

    def __generate_code_currencies(self, number:int):
        codes = set()

        for _ in range(number):
            codes.add(self.__faker.currency_code())

        return list(codes)
