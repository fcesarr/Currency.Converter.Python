import unittest
from unittest.mock import Mock
from src.prefect.currency_flow import get_codes, get_latest
from faker import Faker
from prefect.logging import disable_run_logger

class CurrencyFlowTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.faker = Faker()

    def test_get_codes(self):
        with disable_run_logger():
            codes = self.__generate_code_currencies(20)

            currency_service_mock = Mock()

            currency_service_mock.get_brands = Mock(return_value=codes)

            logger_mock = Mock()

            self.assertListEqual(get_codes.fn(currency_service=currency_service_mock, endpoint="", codes=codes, logger=logger_mock), codes)

    def test_get_latest(self):
        with disable_run_logger():
            codes = self.__generate_code_currencies(20)

            currency_service_mock = Mock()

            currency_service_mock.get_latest = Mock(return_value=codes)

            logger_mock = Mock()

            self.assertListEqual(get_latest.fn(currency_service=currency_service_mock, endpoint="", codes=codes, logger=logger_mock), codes)

    def __generate_code_currencies(self, number:int):
        codes = set()

        for _ in range(number):
            codes.add(self.faker.currency_code())

        return list(codes)
