## Summary
This application has been written for educational purposes to study the Python API implementation and its deployment on the Google Cloud Platform **Cloud Run** service. This Microservice (ms) should retrieve the Dividends from Third-Party APIs by exposing some endpoints.

Currently, the application is using [Freedom Finance](https://rapidapi.com/integraatio/api/freedom-finance) as Third-Party API to get the Financial Data as the Stock's dividends. To use the API, is needed to obtain the API Key provided by the API Page hosted in RapidAPI Hub. It's pretty easy to do from the [link provided here](https://rapidapi.com/integraatio/api/freedom-finance/pricing).

The code implementation has been documented here -> [https://medium.com/@Tutonews/getting-started-a-cloud-run-python-application-4f8a54b4d951](https://medium.com/@augustocadini/getting-started-a-cloud-run-python-application-4f8a54b4d951)

## Running
1. Active Python venv: `/venv-ms-get-dividends/bin % source ./activate`

2. Install the libraries: `/ms-get-dividends % pip install --no-cache-dir -r requirements.txt`

3. Run the service: `/ms-get-dividends/app % python main.py`

## Deploy to Cloud Run
1. `/ms-get-dividends % gcloud run deploy total-return-dev --region=us-central1 --source=.`

## Endpoints
- `@GET /v1/stock/dividends`

Retrieve the Dividends in aggregated form based on a Date Range. Arguments Ticker, Start Date, and End Date are passed by entity Payload. For Brazilian stocks must add the suffix `.SA` along the Ticker code.

Headers:

`X-API-Key`: `API-KEY-PROVIDED-BY-THIRD-PARTY-API`

`Content-Type`: `application/json`

Body:
```
{
    "ticker": "ITSA4.SA",
    "startDate": "2018-01-01",
    "endDate": "2022-12-31"
}
```

Example:
```
curl --location 'localhost:8080/v1/stock/dividends' \
--header 'X-API-Key: API-KEY-PROVIDED-BY-THIRD-PARTY-API' \
--header 'Content-Type: application/json' \
--data '{
    "ticker": "ITSA.SA",
    "startDate": "2018-01-01",
    "endDate": "2022-12-31"
}'

{
    "endDate": "2022-12-31",
    "startDate": "2018-01-01",
    "sumValue": 2.9267410000000007,
    "ticker": "ITSA4.SA"
}
```

- `@GET /healthcheck`

Health Check. Mostly simple as possible health check:

No headers.

No body.

Example:


```
% curl --location --request GET 'localhost:8080/healthcheck'
{"status":"ok"}
```

## Architecture
- **Resource**: endpoints declaration.
- **Resource Implementation**: endpoints logic implementation.
- **Service Proxy**: service API routes. It makes it easier to decouple the third-party API in case need to change it.
- **Service**: downstream service call implementation.
