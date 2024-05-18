from requests import Response, Session
from .currency_api import CurrencyApi

class FreeCurrencyApi(CurrencyApi):
    def __init__(self, base_url:str,
                 endpoint_codes:str,
                 endpoint_latest:str,
                 session:Session) -> None:
        super().__init__(base_url, endpoint_codes, endpoint_latest, session)

    def treat_codes(self, json: dict):
        if not 'data' in json:
            raise Exception("Data it's not found")

        return json['data'].keys()

    def treat_latest(self, json: dict):
        if not 'data' in json:
            raise Exception("Data it's not found")

        return json['data']

    def _validate_status_code(self, response: Response):
        if response.status_code != 200:
            raise Exception("Status code diff of 200")
