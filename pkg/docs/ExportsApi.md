# apteco_api.ExportsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exports_get_export_system**](ExportsApi.md#exports_get_export_system) | **GET** /{dataViewName}/Exports/{systemName} | Returns some top-level details for the specified FastStats system to export from
[**exports_get_export_systems**](ExportsApi.md#exports_get_export_systems) | **GET** /{dataViewName}/Exports | Returns the list of FastStats systems available for exporting data from
[**exports_perform_export_synchronously**](ExportsApi.md#exports_perform_export_synchronously) | **POST** /{dataViewName}/Exports/{systemName}/ExportSync | EXPERIMENTAL: Exports data using the given export definition and returns the results.  The results might contain the actual data in the \&quot;rows\&quot; part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.


# **exports_get_export_system**
> ExportSystemDetail exports_get_export_system(data_view_name, system_name)

Returns some top-level details for the specified FastStats system to export from

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.ExportsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to return details for

    try:
        # Returns some top-level details for the specified FastStats system to export from
        api_response = api_instance.exports_get_export_system(data_view_name, system_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportsApi->exports_get_export_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to return details for | 

### Return type

[**ExportSystemDetail**](ExportSystemDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Some metadata for the specified FastStats system |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the specified system |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_export_systems**
> PagedResultsExportSystemSummary exports_get_export_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of FastStats systems available for exporting data from

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.ExportsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns the list of FastStats systems available for exporting data from
        api_response = api_instance.exports_get_export_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportsApi->exports_get_export_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsExportSystemSummary**](PagedResultsExportSystemSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of systems |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the list of systems |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_perform_export_synchronously**
> ExportResult exports_perform_export_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, export=export)

EXPERIMENTAL: Exports data using the given export definition and returns the results.  The results might contain the actual data in the \"rows\" part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.

EXPERIMENTAL  Requires licence flags [Export]

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.ExportsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration (optional)
return_definition = True # bool | Whether to include the export's definition in the results.  Default is false. (optional)
export = apteco_api.Export() # Export | The export definition to use (optional)

    try:
        # EXPERIMENTAL: Exports data using the given export definition and returns the results.  The results might contain the actual data in the \"rows\" part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.
        api_response = api_instance.exports_perform_export_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, export=export)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportsApi->exports_perform_export_synchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service&#39;s configuration | [optional] 
 **return_definition** | **bool**| Whether to include the export&#39;s definition in the results.  Default is false. | [optional] 
 **export** | [**Export**](Export.md)| The export definition to use | [optional] 

### Return type

[**ExportResult**](ExportResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The export result for the given definition |  -  |
**400** | A bad request |  -  |
**403** | Forbidden |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

