# apteco_api.CubesApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cubes_calculate_cube_synchronously**](CubesApi.md#cubes_calculate_cube_synchronously) | **POST** /{dataViewName}/Cubes/{systemName}/CalculateSync | EXPERIMENTAL: Calcaultes a cube using the given definition and returns the results.  The data to build the cube from is defined by the base query provided.


# **cubes_calculate_cube_synchronously**
> CubeResult cubes_calculate_cube_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, cube=cube)

EXPERIMENTAL: Calcaultes a cube using the given definition and returns the results.  The data to build the cube from is defined by the base query provided.

EXPERIMENTAL  Requires licence flags [Cube]

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
api_instance = apteco_api.CubesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration (optional)
return_definition = True # bool | Whether to include the cube's definition in the results (optional)
cube = apteco_api.Cube() # Cube | The cube definition to use (optional)

try:
    # EXPERIMENTAL: Calcaultes a cube using the given definition and returns the results.  The data to build the cube from is defined by the base query provided.
    api_response = api_instance.cubes_calculate_cube_synchronously(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, return_definition=return_definition, cube=cube)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CubesApi->cubes_calculate_cube_synchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service&#39;s configuration | [optional] 
 **return_definition** | **bool**| Whether to include the cube&#39;s definition in the results | [optional] 
 **cube** | [**Cube**](Cube.md)| The cube definition to use | [optional] 

### Return type

[**CubeResult**](CubeResult.md)

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

