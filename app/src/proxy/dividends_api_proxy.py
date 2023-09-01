from ..service import freedom_finance_api_service
from flask import abort
from datetime import datetime


def get_aggregated_dividends(apiKey: str, startDate: datetime, endDate: datetime, ticker: str) -> float:
    api_response = freedom_finance_api_service.get_dividends(apiKey, ticker)

    if api_response.status_code != 200:
        if 'responseStatus' in api_response.json().keys():
            abort(api_response.status_code, api_response.json())
        else:
            abort(500, f"An error occurred while trying to get dividends for ticker {ticker}. Error: {api_response}")

    results = api_response.json()['results']

    ranged_date_results = [
        result for result in results
        if startDate <= datetime.fromisoformat(result['date']) <= endDate
    ]

    sum_value = sum([result['amount'] for result in ranged_date_results])
    return sum_value
