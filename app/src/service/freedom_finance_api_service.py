import requests
from requests import Response

url_dividends = "https://freedom-finance.p.rapidapi.com/dividends"
rapid_api_host = "freedom-finance.p.rapidapi.com"


def get_dividends(apiKey: str, ticker: str) -> Response:
    print("--- service get_dividends")
    try:
        query_string = {"Symbol": f"{ticker}", "OrderBy": "Ascending"}
        headers = {
            "X-RapidAPI-Key": f"{apiKey}",
            "X-RapidAPI-Host": f"{rapid_api_host}"
        }
        print(f"QueryString: {query_string}")
        print(f"Headers: {headers}")
        response = requests.get(url_dividends, headers=headers, params=query_string)
        return response
    except Exception as e:
        abort(500, f"An error occurred while trying to get dividends for ticker {ticker}. Error: {e}")
