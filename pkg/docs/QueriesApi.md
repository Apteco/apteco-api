# apteco_api.QueriesApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queries_perform_get_query_file_definition_synchronously**](QueriesApi.md#queries_perform_get_query_file_definition_synchronously) | **POST** /{dataViewName}/Queries/{systemName}/GetFileSync | EXPERIMENTAL: Get the query definition in the specified file
[**queries_perform_query_count_synchronously**](QueriesApi.md#queries_perform_query_count_synchronously) | **POST** /{dataViewName}/Queries/{systemName}/CountSync | EXPERIMENTAL: Counts the given query and returns the results
[**queries_perform_query_file_count_synchronously**](QueriesApi.md#queries_perform_query_file_count_synchronously) | **POST** /{dataViewName}/Queries/{systemName}/CountFileSync | EXPERIMENTAL: Counts the query in the specified file and returns the results
[**queries_perform_save_query_file_definition_synchronously**](QueriesApi.md#queries_perform_save_query_file_definition_synchronously) | **POST** /{dataViewName}/Queries/{systemName}/SaveFileSync | EXPERIMENTAL: Get the query definition in the specified file


# **queries_perform_get_query_file_definition_synchronously**
> QueryResult queries_perform_get_query_file_definition_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, query_file=query_file)

EXPERIMENTAL: Get the query definition in the specified file

EXPERIMENTAL  Requires licence flags [AdvancedQuery]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration.api_key['faststats_auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['faststats_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.QueriesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration (optional)
query_file = apteco_api.QueryFile() # QueryFile | The file that holds the query definition (optional)

    try:
        # EXPERIMENTAL: Get the query definition in the specified file
        api_response = api_instance.queries_perform_get_query_file_definition_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, query_file=query_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueriesApi->queries_perform_get_query_file_definition_synchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service&#39;s configuration | [optional] 
 **query_file** | [**QueryFile**](QueryFile.md)| The file that holds the query definition | [optional] 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The definition in the given query file |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file |  -  |
**404** | The system name or specified query couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queries_perform_query_count_synchronously**
> QueryResult queries_perform_query_count_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, query=query)

EXPERIMENTAL: Counts the given query and returns the results

EXPERIMENTAL  Requires licence flags [AdvancedQuery]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration.api_key['faststats_auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['faststats_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.QueriesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration (optional)
return_definition = True # bool | Whether to include the query's definition in the results.  Default is false. (optional)
query = apteco_api.Query() # Query | The query definition to count (optional)

    try:
        # EXPERIMENTAL: Counts the given query and returns the results
        api_response = api_instance.queries_perform_query_count_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueriesApi->queries_perform_query_count_synchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service&#39;s configuration | [optional] 
 **return_definition** | **bool**| Whether to include the query&#39;s definition in the results.  Default is false. | [optional] 
 **query** | [**Query**](Query.md)| The query definition to count | [optional] 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The count result for the given query |  -  |
**400** | A bad request |  -  |
**403** | Forbidden |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queries_perform_query_file_count_synchronously**
> QueryResult queries_perform_query_file_count_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, query_file=query_file)

EXPERIMENTAL: Counts the query in the specified file and returns the results

EXPERIMENTAL  Requires licence flags [AdvancedQuery]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration.api_key['faststats_auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['faststats_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.QueriesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration (optional)
return_definition = True # bool | Whether to include the query's definition in the results.  Default is false. (optional)
query_file = apteco_api.QueryFile() # QueryFile | The file that holds the query definition to count (optional)

    try:
        # EXPERIMENTAL: Counts the query in the specified file and returns the results
        api_response = api_instance.queries_perform_query_file_count_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, query_file=query_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueriesApi->queries_perform_query_file_count_synchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service&#39;s configuration | [optional] 
 **return_definition** | **bool**| Whether to include the query&#39;s definition in the results.  Default is false. | [optional] 
 **query_file** | [**QueryFile**](QueryFile.md)| The file that holds the query definition to count | [optional] 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The count result for the given query file |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file |  -  |
**404** | The system name or specified query couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queries_perform_save_query_file_definition_synchronously**
> queries_perform_save_query_file_definition_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, save_query_file=save_query_file)

EXPERIMENTAL: Get the query definition in the specified file

EXPERIMENTAL  Requires licence flags [AdvancedQuery]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration.api_key['faststats_auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['faststats_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.QueriesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration (optional)
save_query_file = apteco_api.SaveQueryFile() # SaveQueryFile | The file that holds the query definition (optional)

    try:
        # EXPERIMENTAL: Get the query definition in the specified file
        api_instance.queries_perform_save_query_file_definition_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, save_query_file=save_query_file)
    except ApiException as e:
        print("Exception when calling QueriesApi->queries_perform_save_query_file_definition_synchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service&#39;s configuration | [optional] 
 **save_query_file** | [**SaveQueryFile**](SaveQueryFile.md)| The file that holds the query definition | [optional] 

### Return type

void (empty response body)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The definition in the given query file |  -  |
**204** | Success |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file |  -  |
**404** | The system name or specified query couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

