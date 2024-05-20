import time
from flask import Flask

app = Flask(__name__)

counter :int=0

@app.route("/currencies")
def currencies():
    return {
        "data": {
            "EUR": {
            "symbol": "€",
            "name": "Euro",
            "symbol_native": "€",
            "decimal_digits": 2,
            "rounding": 0,
            "code": "EUR",
            "name_plural": "Euros",
            "type": "fiat"
            },
            "USD": {
            "symbol": "$",
            "name": "US Dollar",
            "symbol_native": "$",
            "decimal_digits": 2,
            "rounding": 0,
            "code": "USD",
            "name_plural": "US dollars",
            "type": "fiat"
            },
            "CAD": {
            "symbol": "CA$",
            "name": "Canadian Dollar",
            "symbol_native": "$",
            "decimal_digits": 2,
            "rounding": 0,
            "code": "CAD",
            "name_plural": "Canadian dollars",
            "type": "fiat"
            }
        }
    }


@app.route("/latest")
def latest():
    global counter

    if not counter % 2:
        time.sleep(5)

    counter += 1

    return {
        "data": {
            "CAD": 1.3650002621,
            "EUR": 0.9245901699,
            "USD": 1
        }
    }
