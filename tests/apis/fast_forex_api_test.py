import io
import json
import unittest
from unittest.mock import Mock
from requests import Response
from src.apis.fast_forex_api import FastForexApi
from faker import Faker


class FastForexApiTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.faker = Faker()

    def test_get_codes(self):
        codes = self.__generate_code_currencies(20)

        code_currency_data = {
            "currencies": self.__generate_code_currencies_data(codes=codes)
        }

        response = Response()

        response.status_code=200

        response.raw=io.BytesIO(json.dumps(code_currency_data, indent=4).encode('utf-8'))

        session_mock = Mock()

        session_mock.get = Mock(return_value=response)

        instance = FastForexApi(base_url="",
                                endpoint_codes="",
                                endpoint_latest="",
                                session=session_mock)

        self.assertListEqual(instance.get_codes(), codes)

    def test_get_codes_status_code_diff_success_raise_exception(self):
        session_mock = Mock()

        response = Response()

        response.status_code = self.__generate_random_int_except(200)

        instance = FastForexApi(base_url="",
                                endpoint_codes="",
                                endpoint_latest="",
                                session=session_mock)

        with self.assertRaises(Exception) as cm:
            instance.get_codes()

        self.assertEqual("Status code diff of 200", str(cm.exception))

    def test_get_codes_data_not_exists_raise_exception(self):
        expected = self.__generate_code_currencies(20)

        currency_data = {

        }

        session_mock = Mock()

        response = Response()

        response.status_code=200

        response.raw=io.BytesIO(json.dumps(currency_data, indent=4).encode('utf-8'))

        session_mock.get = Mock(return_value=response)

        instance = FastForexApi(base_url="",
                                endpoint_codes="",
                                endpoint_latest="",
                                session=session_mock)

        with self.assertRaises(Exception) as cm:
            instance.get_codes()

        self.assertEqual("Data it's not found", str(cm.exception))

    def test_get_latest(self):
        codes = self.__generate_code_currencies(20)

        latest_currency_data = {
            "results": self.__generate_latest_currency_data(codes=codes)
        }

        response = Response()

        response.status_code=200

        response.raw=io.BytesIO(json.dumps(latest_currency_data, indent=4).encode('utf-8'))

        session_mock = Mock()

        session_mock.get = Mock(return_value=response)

        instance = FastForexApi(base_url="",
                                endpoint_codes="",
                                endpoint_latest="",
                                session=session_mock)

        self.assertEqual(instance.get_latest(codes=codes), latest_currency_data['results'])

    def test_get_latest_status_code_diff_success_raise_exception(self):
        session_mock = Mock()

        response = Response()

        response.status_code = self.__generate_random_int_except(200)

        instance = FastForexApi(base_url="",
                                endpoint_codes="",
                                endpoint_latest="",
                                session=session_mock)

        with self.assertRaises(Exception) as cm:
            instance.get_latest(codes=[""])

        self.assertEqual("Status code diff of 200", str(cm.exception))

    def test_get_latest_data_not_exists_raise_exception(self):
        currency_data = {

        }

        session_mock = Mock()

        response = Response()

        response.status_code=200

        response.raw=io.BytesIO(json.dumps(currency_data, indent=4).encode('utf-8'))

        session_mock.get = Mock(return_value=response)

        instance = FastForexApi(base_url="",
                                endpoint_codes="",
                                endpoint_latest="",
                                session=session_mock)

        with self.assertRaises(Exception) as cm:
            instance.get_latest(codes=[""])

        self.assertEqual("Data it's not found", str(cm.exception))

    def test_get_latest_codes_is_empty_raise_exception(self):
        session_mock = Mock()

        instance = FastForexApi(base_url="",
                                endpoint_codes="",
                                endpoint_latest="",
                                session=session_mock)

        with self.assertRaises(Exception) as cm:
            instance.get_latest(codes=[])

        self.assertEqual("Codes of currencies are empty", str(cm.exception))

    def __generate_random_int_except(self, exclude_value):
        random_int = self.faker.pyint()  # Generate a random integer using Faker
        while random_int == exclude_value:
            random_int = self.faker.pyint(min_value=100, max_value=500, step=100)  # Generate another random integer if it matches the excluded value
        return random_int

    def __generate_code_currencies(self, number:int):
        codes = set()

        for _ in range(number):
            codes.add(self.faker.currency_code())

        return list(codes)

    def __generate_code_currencies_data(self, codes:list):
        data = {}
        for code in codes:
            data[code] = self.faker.currency_name()
        return data

    def __generate_latest_currency_data(self, codes:list):
        data = {}
        for code in codes:
            data[code] = self.faker.pyfloat(positive=True)
        return data
