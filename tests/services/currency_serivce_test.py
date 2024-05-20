import unittest
import json
import io
from unittest.mock import MagicMock, Mock
from requests import Response, Timeout
from src.services.currency_service import CurrencyService
from faker import Faker

class CurrencyServiceTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.faker = Faker()



    # def test_get_latest(self):
    #     codes = self.__generate_code_currencies(20)

    #     latest_currency_data = {
    #         "data": self.__generate_latest_currency_data(codes=codes)
    #     }

    #     response = Response()

    #     response.status_code=200

    #     response.raw=io.BytesIO(json.dumps(latest_currency_data, indent=4).encode('utf-8'))

    #     session_mock = Mock()

    #     session_mock.get = Mock(return_value=response)

    #     instance = CurrencyService(base_url="", session=session_mock)

    #     self.assertEqual(instance.get_latest(endpoint="", codes=codes), latest_currency_data['data'])

    # def test_get_latest_status_code_diff_success_raise_exception(self):
    #     session_mock = Mock()

    #     response = Response()

    #     response.status_code = self.__generate_random_int_except(200)

    #     instance = CurrencyService(base_url="", session=session_mock)

    #     with self.assertRaises(Exception) as cm:
    #         instance.get_latest(endpoint="", codes=[""])

    #     self.assertEqual("Status code diff of 200", str(cm.exception))

    # def test_get_latest_data_not_exists_raise_exception(self):
    #     currency_data = {

    #     }

    #     session_mock = Mock()

    #     response = Response()

    #     response.status_code=200

    #     response.raw=io.BytesIO(json.dumps(currency_data, indent=4).encode('utf-8'))

    #     session_mock.get = Mock(return_value=response)

    #     instance = CurrencyService(base_url="", session=session_mock)

    #     with self.assertRaises(Exception) as cm:
    #         instance.get_latest(endpoint="", codes=[""])

    #     self.assertEqual("Data it's not found", str(cm.exception))

    # def test_get_latest_codes_is_empty_raise_exception(self):
    #     session_mock = Mock()

    #     instance = CurrencyService(base_url="", session=session_mock)

    #     with self.assertRaises(Exception) as cm:
    #         instance.get_latest(endpoint="", codes=[])

    #     self.assertEqual("Codes of currencies are empty", str(cm.exception))

    # def test_get_latest_throw(self):
    #     codes = self.__generate_code_currencies(20)

    #     latest_currency_data = {
    #         "data": self.__generate_latest_currency_data(codes=codes)
    #     }

    #     response = Response()

    #     response.status_code=200

    #     response.raw=io.BytesIO(json.dumps(latest_currency_data, indent=4).encode('utf-8'))

    #     session_mock = Mock()

    #     session_mock.get.side_effect = Mock(side_effect=Timeout('Test'))

    #     instance = CurrencyService(base_url="", session=session_mock)

    #     with self.assertRaises(Exception):
    #         instance.get_latest(endpoint="", codes=[""])

    # def __generate_random_int_except(self, exclude_value):
    #     random_int = self.faker.pyint()  # Generate a random integer using Faker
    #     while random_int == exclude_value:
    #         random_int = self.faker.pyint(min_value=100, max_value=500, step=100)  # Generate another random integer if it matches the excluded value
    #     return random_int

    # def __generate_code_currencies(self, number:int):
    #     codes = set()

    #     for _ in range(number):
    #         codes.add(self.faker.currency_code())

    #     return list(codes)

    # def __generate_code_currencies_data(self, codes:list):
    #     data = {}
    #     for code in codes:
    #         data[code] = {
    #             'symbol': self.faker.currency_symbol(),
    #             'name': self.faker.currency_name(),
    #             'symbol_native': self.faker.currency_symbol(),
    #             'decimal_digits': self.faker.random_int(min=0, max=2),
    #             'rounding': self.faker.random_int(min=0, max=10),
    #             'code': code,
    #             'name_plural': self.faker.currency_name(),
    #             'type': 'fiat'  # Assuming all currencies are of type 'fiat'
    #         }
    #     return data

    # def __generate_latest_currency_data(self, codes:list):
    #     data = {}
    #     for code in codes:
    #         data[code] = self.faker.pyfloat(positive=True)
    #     return data
