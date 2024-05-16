import logging
import json
from requests import Session, Timeout
from prefect import task, flow, get_run_logger
from ..services.currency_service import CurrencyService

retries:int=2

@task(retries=retries, retry_delay_seconds=10)
def get_codes(currency_service:CurrencyService,
              endpoint:str,
              codes:list,
              logger:logging.Logger):
    codes:list = currency_service.get_brands(endpoint=endpoint, codes=codes)
    logger.info("Get codes successfully")
    return codes

@task(retries=retries, retry_delay_seconds=10)
def get_latest(currency_service:CurrencyService,
               endpoint:str,
               codes:list,
               logger:logging.Logger):
    latest:dict = currency_service.get_latest(endpoint=endpoint, codes=codes)
    logger.info(f"Get latest currency successfully")
    return latest

@flow(log_prints=True)
def currency_flow(url:str,
                  codes:list,
                  endpoint_codes:str,
                  endpoint_latest:str): # pragma: no cover
    logger = get_run_logger()

    currency_service = CurrencyService(base_url=url,
                                       session=Session(),
                                       ratio_latest=10**retries)

    current_codes:list = get_codes(currency_service=currency_service,
                                   endpoint=endpoint_codes,
                                   codes=codes,
                                   logger=logger)

    latest:dict = get_latest(currency_service=currency_service,
                             endpoint=endpoint_latest,
                             codes=current_codes,
                             logger=logger)

    logger.info(f"Latest currency: {json.dumps(latest)}")
