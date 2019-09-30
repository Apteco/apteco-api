# apteco_api.ExportsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exports_perform_export_synchronously**](ExportsApi.md#exports_perform_export_synchronously) | **POST** /{dataViewName}/Exports/{systemName}/ExportSync | EXPERIMENTAL: Exports data using the given export definition and returns the results.  The results might contain the actual data in the \&quot;rows\&quot; part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.


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
configuration = apteco_api.Configuration()
# Configure API key authorization: faststats_auth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = apteco_api.ExportsApi(apteco_api.ApiClient(configuration))
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

