from requests import Session

from ..apis.fast_forex_api import FastForexApi
from ..apis.fake_api import FakeApi
from src.prefect.currency_flow import currency_flow

if __name__ == '__main__':
    session:Session = Session()

    currency_apis = {
        "FakeApi": FakeApi(base_url="http://currency-api-timeout:5000/",
                        endpoint_codes='currencies?apikey=sgiPfh4j3aXFR3l2CnjWqdKQzxpqGn9pX5b3CUsz',
                        endpoint_latest='latest?apikey=sgiPfh4j3aXFR3l2CnjWqdKQzxpqGn9pX5b3CUsz&base_currency=USD&currencies',
                        session=session)
    }

    currency_flow(name="FakeApi",
                  currency_apis=currency_apis)
