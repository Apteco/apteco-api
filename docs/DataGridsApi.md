# apteco_api.DataGridsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_grids_get_data_grid_result**](DataGridsApi.md#data_grids_get_data_grid_result) | **POST** /{dataViewName}/DataGrids/{systemName}/Files/{filePath} | EXPERIMENTAL: Returns the DataGrid from a saved file.


# **data_grids_get_data_grid_result**
> DataGridResult data_grids_get_data_grid_result(data_view_name, system_name, file_path, timeout_in_seconds=timeout_in_seconds)

EXPERIMENTAL: Returns the DataGrid from a saved file.

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
api_instance = apteco_api.DataGridsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
file_path = 'file_path_example' # str | The path of the file to return the contents for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)

try:
    # EXPERIMENTAL: Returns the DataGrid from a saved file.
    api_response = api_instance.data_grids_get_data_grid_result(data_view_name, system_name, file_path, timeout_in_seconds=timeout_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataGridsApi->data_grids_get_data_grid_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **file_path** | **str**| The path of the file to return the contents for | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service&#39;s configuration | [optional] 

### Return type

[**DataGridResult**](DataGridResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contents of the file |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file |  -  |
**404** | The system name or specified directory couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

