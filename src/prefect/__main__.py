from requests import Session

from ..apis.fast_forex_api import FastForexApi
from ..apis.free_currency_api import FreeCurrencyApi
from src.prefect.currency_flow import currency_flow

if __name__ == '__main__':
    session:Session = Session()

    currency_apis = {
        "FreeCurrencyApi": FreeCurrencyApi(base_url="https://api.freecurrencyapi.com/v1/",
                        endpoint_codes='currencies?apikey=sgiPfh4j3aXFR3l2CnjWqdKQzxpqGn9pX5b3CUsz',
                        endpoint_latest='latest?apikey=sgiPfh4j3aXFR3l2CnjWqdKQzxpqGn9pX5b3CUsz&base_currency=USD&currencies',
                        session=session),
        "FastForexApi": FastForexApi(base_url=" https://api.fastforex.io/",
                        endpoint_codes='currencies?api_key=demo',
                        endpoint_latest='fetch-multi?api_key=demo&from=USD&to=',
                        session=session)
    }

    currency_flow(name="FreeCurrencyApi",
                  currency_apis=currency_apis)

    # currency_flow(name="FastForexApi",
    #               currency_apis=currency_apis)
