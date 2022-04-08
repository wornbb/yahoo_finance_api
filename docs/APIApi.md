# yahoo_client.APIApi

All URIs are relative to *https://yfapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](APIApi.md#autocomplete) | **GET** /v6/finance/autocomplete | 
[**chart**](APIApi.md#chart) | **GET** /v8/finance/chart/{ticker} | 
[**history**](APIApi.md#history) | **GET** /v8/finance/spark | 
[**insights**](APIApi.md#insights) | **GET** /ws/insights/v1/finance/insights | 
[**options**](APIApi.md#options) | **GET** /v7/finance/options/{symbol} | 
[**popular**](APIApi.md#popular) | **GET** /ws/screeners/v1/finance/screener/predefined/saved | 
[**quotes**](APIApi.md#quotes) | **GET** /v6/finance/quote | 
[**similar**](APIApi.md#similar) | **GET** /v6/finance/recommendationsbysymbol/{symbol} | 
[**stock_details**](APIApi.md#stock_details) | **GET** /v11/finance/quoteSummary/{symbol} | 
[**summary**](APIApi.md#summary) | **GET** /v6/finance/quote/marketSummary | 
[**trending**](APIApi.md#trending) | **GET** /v1/finance/trending/{region} | 

# **autocomplete**
> autocomplete(query, region=region, lang=lang)



Get auto complete stock suggestions

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **region** | **str**| &#x60;US&#x60; &#x60;AU&#x60; &#x60;CA&#x60; &#x60;FR&#x60; &#x60;DE&#x60; &#x60;HK&#x60; &#x60;US&#x60; &#x60;IT&#x60; &#x60;ES&#x60; &#x60;GB&#x60; &#x60;IN&#x60; | [optional] 
 **lang** | **str**| &#x60;en&#x60; &#x60;fr&#x60; &#x60;de&#x60; &#x60;it&#x60; &#x60;es&#x60; &#x60;zh&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chart**
> chart(ticker, comparisons=comparisons, range=range, region=region, interval=interval, lang=lang, events=events)



Get chart data by ticker

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **comparisons** | **str**| The tickers for comparison separated by comma. Max 10 tickers | [optional] 
 **range** | **str**| &#x60;1d&#x60; &#x60;5d&#x60; &#x60;1mo&#x60; &#x60;3mo&#x60; &#x60;6mo&#x60; &#x60;1y&#x60; &#x60;5y&#x60; &#x60;10y&#x60; &#x60;ytd&#x60; &#x60;max&#x60; | [optional] 
 **region** | **str**| &#x60;US&#x60; &#x60;AU&#x60; &#x60;CA&#x60; &#x60;FR&#x60; &#x60;DE&#x60; &#x60;HK&#x60; &#x60;US&#x60; &#x60;IT&#x60; &#x60;ES&#x60; &#x60;GB&#x60; &#x60;IN&#x60; | [optional] 
 **interval** | **str**| &#x60;1m&#x60; &#x60;5m&#x60; &#x60;15m&#x60; &#x60;1d&#x60; &#x60;1wk&#x60; &#x60;1mo&#x60; | [optional] 
 **lang** | **str**| &#x60;en&#x60; &#x60;fr&#x60; &#x60;de&#x60; &#x60;it&#x60; &#x60;es&#x60; &#x60;zh&#x60; | [optional] 
 **events** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history**
> history(symbols, interval=interval, range=range)



Stock history

### Example
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
symbols = 'symbols_example' # str | Separated by comm. Max 10
interval = 'interval_example' # str | `1m` `5m` `15m` `1d` `1wk` `1mo` (optional)
range = 'range_example' # str | `1d` `5d` `1mo` `3mo` `6mo` `1y` `5y` `max` (optional)

try:
    api_instance.history(symbols, interval=interval, range=range)
except ApiException as e:
    print("Exception when calling APIApi->history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Separated by comm. Max 10 | 
 **interval** | **str**| &#x60;1m&#x60; &#x60;5m&#x60; &#x60;15m&#x60; &#x60;1d&#x60; &#x60;1wk&#x60; &#x60;1mo&#x60; | [optional] 
 **range** | **str**| &#x60;1d&#x60; &#x60;5d&#x60; &#x60;1mo&#x60; &#x60;3mo&#x60; &#x60;6mo&#x60; &#x60;1y&#x60; &#x60;5y&#x60; &#x60;max&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insights**
> insights(symbol)



Research insights

### Example
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
symbol = 'symbol_example' # str | 

try:
    api_instance.insights(symbol)
except ApiException as e:
    print("Exception when calling APIApi->insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options**
> options(symbol, _date=_date)



Get option chain for a particular symbol

### Example
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
symbol = 'symbol_example' # str | 
_date = 1.2 # float | example: 1510876800 (optional)

try:
    api_instance.options(symbol, _date=_date)
except ApiException as e:
    print("Exception when calling APIApi->options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **_date** | **float**| example: 1510876800 | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **popular**
> popular(scr_ids, count=count)



Most added to watchlist

### Example
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
scr_ids = 'scr_ids_example' # str | 
count = 1.2 # float |  (optional)

try:
    api_instance.popular(scr_ids, count=count)
except ApiException as e:
    print("Exception when calling APIApi->popular: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scr_ids** | **str**|  | 
 **count** | **float**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotes**
> quotes(symbols, region=region, lang=lang)



Real time quote data for stocks, ETFs, mutuals funds, etc…

### Example
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
symbols = 'symbols_example' # str | Multiple symbols separated by commas. Max is 10
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `IT` `ES` `GB` `IN` (optional)
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)

try:
    api_instance.quotes(symbols, region=region, lang=lang)
except ApiException as e:
    print("Exception when calling APIApi->quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Multiple symbols separated by commas. Max is 10 | 
 **region** | **str**| &#x60;US&#x60; &#x60;AU&#x60; &#x60;CA&#x60; &#x60;FR&#x60; &#x60;DE&#x60; &#x60;HK&#x60; &#x60;IT&#x60; &#x60;ES&#x60; &#x60;GB&#x60; &#x60;IN&#x60; | [optional] 
 **lang** | **str**| &#x60;en&#x60; &#x60;fr&#x60; &#x60;de&#x60; &#x60;it&#x60; &#x60;es&#x60; &#x60;zh&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar**
> similar(symbol)



List similar stocks

### Example
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
symbol = 'symbol_example' # str | 

try:
    api_instance.similar(symbol)
except ApiException as e:
    print("Exception when calling APIApi->similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_details**
> stock_details(modules, symbol, lang=lang, region=region)



Get very detailed information for a particular stock.  The next portions of data can be retrieved with the service: `summaryDetail` `assetProfile` `fundProfile` `financialData` `defaultKeyStatistics` `calendarEvents` `incomeStatementHistory` `incomeStatementHistoryQuarterly` `cashflowStatementHistory` `balanceSheetHistory` `earnings` `earningsHistory` `insiderHolders` `cashflowStatementHistory` `cashflowStatementHistoryQuarterly` `insiderTransactions` `secFilings` `indexTrend` `sectorTrend` `earningsTrend` `netSharePurchaseActivity` `upgradeDowngradeHistory` `institutionOwnership` `recommendationTrend` `balanceSheetHistory` `balanceSheetHistoryQuarterly` `fundOwnership` `majorDirectHolders` `majorHoldersBreakdown`, `price`, `quoteType`, `esgScores`

### Example
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
modules = 'modules_example' # str | `summaryDetail` `assetProfile` `fundProfile` `financialData` `defaultKeyStatistics` `calendarEvents` `incomeStatementHistory` `incomeStatementHistoryQuarterly` `cashflowStatementHistory` `balanceSheetHistory` `earnings` `earningsHistory` `insiderHolders` `cashflowStatementHistory` `cashflowStatementHistoryQuarterly` `insiderTransactions` `secFilings` `indexTrend` `sectorTrend` `earningsTrend` `netSharePurchaseActivity` `upgradeDowngradeHistory` `institutionOwnership` `recommendationTrend` `balanceSheetHistory` `balanceSheetHistoryQuarterly` `fundOwnership` `majorDirectHolders` `majorHoldersBreakdown`, `price`, `quoteType`, `esgScores`
symbol = 'symbol_example' # str | A single symbol
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN` (optional)

try:
    api_instance.stock_details(modules, symbol, lang=lang, region=region)
except ApiException as e:
    print("Exception when calling APIApi->stock_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modules** | **str**| &#x60;summaryDetail&#x60; &#x60;assetProfile&#x60; &#x60;fundProfile&#x60; &#x60;financialData&#x60; &#x60;defaultKeyStatistics&#x60; &#x60;calendarEvents&#x60; &#x60;incomeStatementHistory&#x60; &#x60;incomeStatementHistoryQuarterly&#x60; &#x60;cashflowStatementHistory&#x60; &#x60;balanceSheetHistory&#x60; &#x60;earnings&#x60; &#x60;earningsHistory&#x60; &#x60;insiderHolders&#x60; &#x60;cashflowStatementHistory&#x60; &#x60;cashflowStatementHistoryQuarterly&#x60; &#x60;insiderTransactions&#x60; &#x60;secFilings&#x60; &#x60;indexTrend&#x60; &#x60;sectorTrend&#x60; &#x60;earningsTrend&#x60; &#x60;netSharePurchaseActivity&#x60; &#x60;upgradeDowngradeHistory&#x60; &#x60;institutionOwnership&#x60; &#x60;recommendationTrend&#x60; &#x60;balanceSheetHistory&#x60; &#x60;balanceSheetHistoryQuarterly&#x60; &#x60;fundOwnership&#x60; &#x60;majorDirectHolders&#x60; &#x60;majorHoldersBreakdown&#x60;, &#x60;price&#x60;, &#x60;quoteType&#x60;, &#x60;esgScores&#x60; | 
 **symbol** | **str**| A single symbol | 
 **lang** | **str**| &#x60;en&#x60; &#x60;fr&#x60; &#x60;de&#x60; &#x60;it&#x60; &#x60;es&#x60; &#x60;zh&#x60; | [optional] 
 **region** | **str**| &#x60;US&#x60; &#x60;AU&#x60; &#x60;CA&#x60; &#x60;FR&#x60; &#x60;DE&#x60; &#x60;HK&#x60; &#x60;US&#x60; &#x60;IT&#x60; &#x60;ES&#x60; &#x60;GB&#x60; &#x60;IN&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summary**
> summary(lang=lang, region=region)



Get live market summary information at the request time

### Example
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
lang = 'lang_example' # str | `en` `fr` `de` `it` `es` `zh` (optional)
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN` (optional)

try:
    api_instance.summary(lang=lang, region=region)
except ApiException as e:
    print("Exception when calling APIApi->summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| &#x60;en&#x60; &#x60;fr&#x60; &#x60;de&#x60; &#x60;it&#x60; &#x60;es&#x60; &#x60;zh&#x60; | [optional] 
 **region** | **str**| &#x60;US&#x60; &#x60;AU&#x60; &#x60;CA&#x60; &#x60;FR&#x60; &#x60;DE&#x60; &#x60;HK&#x60; &#x60;US&#x60; &#x60;IT&#x60; &#x60;ES&#x60; &#x60;GB&#x60; &#x60;IN&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending**
> trending(region)



Trending stocks

### Example
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
region = 'region_example' # str | `US` `AU` `CA` `FR` `DE` `HK` `US` `IT` `ES` `GB` `IN`

try:
    api_instance.trending(region)
except ApiException as e:
    print("Exception when calling APIApi->trending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| &#x60;US&#x60; &#x60;AU&#x60; &#x60;CA&#x60; &#x60;FR&#x60; &#x60;DE&#x60; &#x60;HK&#x60; &#x60;US&#x60; &#x60;IT&#x60; &#x60;ES&#x60; &#x60;GB&#x60; &#x60;IN&#x60; | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

