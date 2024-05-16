from requests import Response, Session, Timeout

class CurrencyService(object):
    def __init__(self, base_url:str, session:Session, ratio_latest:int=1):
        self.__base_url=base_url
        self.__session=session
        self.__timeout_latest=1/ratio_latest

    def get_brands(self, endpoint:str, codes:list):
        if not codes:
            raise Exception("Codes of currencies are empty")

        response = self.__session.get(f"{self.__base_url}{endpoint}={",".join(codes)}")

        json = response.json()

        self.__validate_response(response, json)

        codes = json['data'].keys()

        return list(codes)

    def get_latest(self, endpoint:str, codes:list):
        try:
            if not codes:
                raise Exception("Codes of currencies are empty")

            response = self.__session.get(f"{self.__base_url}{endpoint}={",".join(codes)}", timeout=self.__timeout_latest)

            json = response.json()

            self.__validate_response(response, json)

            return json['data']
        except Timeout:
            self.__timeout_latest*=10
            raise

    def __validate_response(self, response:Response, json:dict):
        if response.status_code != 200:
            raise Exception("Status code diff of 200")

        if not 'data' in json:
            raise Exception("Data it's not found")
