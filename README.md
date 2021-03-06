# yahoo-client
Real time low latency Yahoo Finance API for stock market, crypto currencies, and currency exchange

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import yahoo_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import yahoo_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import yahoo_client
from yahoo_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
query = 'query_example' # str | 
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN` (optional)
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)

try:
    api_instance.autocomplete(query, region=region, lang=lang)
except ApiException as e:
    print("Exception when calling APIApi->autocomplete: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
ticker = 'ticker_example' # str | 
comparisons = 'comparisons_example' # str | The tickers for comparison separated by comma. Max 10 tickers (optional)
range = 'range_example' # str | `1d` `5d` `1mo` `3mo` `6mo` `1y` `5y` `10y` `ytd` `max` (optional)
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN` (optional)
interval = 'interval_example' # str | `1m` `5m` `15m` `1d` `1wk` `1mo` (optional)
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)
events = 'events_example' # str |  (optional)

try:
    api_instance.chart(ticker, comparisons=comparisons, range=range, region=region, interval=interval, lang=lang, events=events)
except ApiException as e:
    print("Exception when calling APIApi->chart: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
symbols = 'symbols_example' # str | Separated by comm. Max 10
interval = 'interval_example' # str | `1m` `5m` `15m` `1d` `1wk` `1mo` (optional)
range = 'range_example' # str | `1d` `5d` `1mo` `3mo` `6mo` `1y` `5y` `max` (optional)

try:
    api_instance.history(symbols, interval=interval, range=range)
except ApiException as e:
    print("Exception when calling APIApi->history: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
symbol = 'symbol_example' # str | 

try:
    api_instance.insights(symbol)
except ApiException as e:
    print("Exception when calling APIApi->insights: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
symbol = 'symbol_example' # str | 
_date = 1.2 # float | example: 1510876800 (optional)

try:
    api_instance.options(symbol, _date=_date)
except ApiException as e:
    print("Exception when calling APIApi->options: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
scr_ids = 'scr_ids_example' # str | 
count = 1.2 # float |  (optional)

try:
    api_instance.popular(scr_ids, count=count)
except ApiException as e:
    print("Exception when calling APIApi->popular: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
symbols = 'symbols_example' # str | Multiple symbols separated by commas. Max is 10
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `IT` `ES` `GB` `IN` (optional)
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)

try:
    api_instance.quotes(symbols, region=region, lang=lang)
except ApiException as e:
    print("Exception when calling APIApi->quotes: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
symbol = 'symbol_example' # str | 

try:
    api_instance.similar(symbol)
except ApiException as e:
    print("Exception when calling APIApi->similar: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
modules = 'modules_example' # str | `summaryDetail` `assetProfile` `fundProfile` `financialData` `defaultKeyStatistics` `calendarEvents` `incomeStatementHistory` `incomeStatementHistoryQuarterly` `cashflowStatementHistory` `balanceSheetHistory` `earnings` `earningsHistory` `insiderHolders` `cashflowStatementHistory` `cashflowStatementHistoryQuarterly` `insiderTransactions` `secFilings` `indexTrend` `sectorTrend` `earningsTrend` `netSharePurchaseActivity` `upgradeDowngradeHistory` `institutionOwnership` `recommendationTrend` `balanceSheetHistory` `balanceSheetHistoryQuarterly` `fundOwnership` `majorDirectHolders` `majorHoldersBreakdown`, `price`, `quoteType`, `esgScores`
symbol = 'symbol_example' # str | A single symbol
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN` (optional)

try:
    api_instance.stock_details(modules, symbol, lang=lang, region=region)
except ApiException as e:
    print("Exception when calling APIApi->stock_details: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN` (optional)

try:
    api_instance.summary(lang=lang, region=region)
except ApiException as e:
    print("Exception when calling APIApi->summary: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN`

try:
    api_instance.trending(region)
except ApiException as e:
    print("Exception when calling APIApi->trending: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://yfapi.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIApi* | [**autocomplete**](docs/APIApi.md#autocomplete) | **GET** /v6/finance/autocomplete | 
*APIApi* | [**chart**](docs/APIApi.md#chart) | **GET** /v8/finance/chart/{ticker} | 
*APIApi* | [**history**](docs/APIApi.md#history) | **GET** /v8/finance/spark | 
*APIApi* | [**insights**](docs/APIApi.md#insights) | **GET** /ws/insights/v1/finance/insights | 
*APIApi* | [**options**](docs/APIApi.md#options) | **GET** /v7/finance/options/{symbol} | 
*APIApi* | [**popular**](docs/APIApi.md#popular) | **GET** /ws/screeners/v1/finance/screener/predefined/saved | 
*APIApi* | [**quotes**](docs/APIApi.md#quotes) | **GET** /v6/finance/quote | 
*APIApi* | [**similar**](docs/APIApi.md#similar) | **GET** /v6/finance/recommendationsbysymbol/{symbol} | 
*APIApi* | [**stock_details**](docs/APIApi.md#stock_details) | **GET** /v11/finance/quoteSummary/{symbol} | 
*APIApi* | [**summary**](docs/APIApi.md#summary) | **GET** /v6/finance/quote/marketSummary | 
*APIApi* | [**trending**](docs/APIApi.md#trending) | **GET** /v1/finance/trending/{region} | 

## Documentation For Models


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author


