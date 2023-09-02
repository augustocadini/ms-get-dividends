from flask import abort
from datetime import datetime
from ..model.dividends_get_request import DividendsGetRequest
from ..model.dividends_get_response import DividendsGetResponse
from ..proxy.dividends_api_proxy import get_aggregated_dividends


def read_dividends(apiKey: str, request: DividendsGetRequest) -> DividendsGetResponse:
    print("--- impl read dividends ---")
    start_date = datetime.fromisoformat(request.startDate)
    end_date = datetime.fromisoformat(request.endDate)
    _validate_dates(start_date, end_date)
    sum_value = get_aggregated_dividends(apiKey, start_date, end_date, request.ticker)
    return DividendsGetResponse(
        ticker=request.ticker,
        startDate=request.startDate,
        endDate=request.endDate,
        sumValue=sum_value
    )


def _validate_dates(startDate, endDate):
    if startDate > endDate:
        abort(400, 'The end date is greater than the start date.')

