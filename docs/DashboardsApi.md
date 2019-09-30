# apteco_api.DashboardsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboards_create_test_dashboard**](DashboardsApi.md#dashboards_create_test_dashboard) | **POST** /{dataViewName}/Dashboards | EXPERIMENTAL: Test function: Removes all dashboards from the DB and creates a new one


# **dashboards_create_test_dashboard**
> dashboards_create_test_dashboard(data_view_name)

EXPERIMENTAL: Test function: Removes all dashboards from the DB and creates a new one

EXPERIMENTAL

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
api_instance = apteco_api.DashboardsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on

try:
    # EXPERIMENTAL: Test function: Removes all dashboards from the DB and creates a new one
    api_instance.dashboards_create_test_dashboard(data_view_name)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboards_create_test_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 

### Return type

void (empty response body)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | The test dashboard was created successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

