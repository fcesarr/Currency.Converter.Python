import logging
import json
from requests import Session, Timeout
from prefect import task, flow, get_run_logger
from ..services.currency_service import CurrencyService

retries:int=2

@task(retries=retries, retry_delay_seconds=10)
def get_codes(currency_service:CurrencyService,
              logger:logging.Logger):
    codes:list = currency_service.get_codes()
    logger.info(f"{currency_service.name}: Get codes successfully")
    return codes

@task(retries=retries, retry_delay_seconds=10)
def get_latest(currency_service:CurrencyService,
               codes:list,
               logger:logging.Logger):
    latest:dict = currency_service.get_latest(codes=codes)
    logger.info(f"{currency_service.name}: Get latest currency successfully")
    return latest

@flow(log_prints=True)
def currency_flow(name:str,
                  currency_apis:dict): # pragma: no cover
    logger = get_run_logger()

    currency_service = CurrencyService(name=name, currency_apis=currency_apis)

    current_codes:list = get_codes(currency_service=currency_service,
                                   logger=logger)

    latest:dict = get_latest(currency_service=currency_service,
                             codes=current_codes,
                             logger=logger)

    logger.info(f"{currency_service.name}: Latest currency: {json.dumps(latest)}")
