from abc import ABC, abstractmethod

from requests import Response, Session, Timeout

class CurrencyApi(ABC):
    def __init__(self, base_url:str,
                 endpoint_codes:str,
                 endpoint_latest:str,
                 session:Session) -> None:
        super().__init__()
        self.__base_url=base_url
        self.__endpoint_codes=endpoint_codes
        self.__endpoint_latest=endpoint_latest
        self.__session=session

    def get_codes(self):
        response = self.__session.get(f"{self.__base_url}{self.__endpoint_codes}")

        json = response.json()

        self._validate_status_code(response)

        codes = self.treat_codes(json=json)

        return list(codes)

    def get_latest(self, codes:list):
        if not codes:
            raise Exception("Codes of currencies are empty")

        response = self.__session.get(f"{self.__base_url}{self.__endpoint_latest}={",".join(codes)}")

        json = response.json()

        self._validate_status_code(response)

        return self.treat_latest(json=json)

    @abstractmethod
    def treat_codes(self, json:dict): # pragma: no cover
        pass

    @abstractmethod
    def treat_latest(self, json:dict): # pragma: no cover
        pass

    @abstractmethod
    def _validate_status_code(self, response:Response): # pragma: no cover
        pass
