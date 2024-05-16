from src.prefect.currency_flow import currency_flow

if __name__ == '__main__':
    currency_flow(url="https://api.freecurrencyapi.com/v1/",
                codes=["EUR", "USD", "CAD", "BRL"],
                endpoint_codes='currencies?apikey=kDvU6mSmi78Y5YQ8EzrhVrEFfSUOBkajHfhG715o&currencies',
                endpoint_latest='latest?apikey=kDvU6mSmi78Y5YQ8EzrhVrEFfSUOBkajHfhG715o&currencies')
