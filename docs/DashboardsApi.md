# apteco_api.DashboardsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboards_get_dashboard_item_data_sync**](DashboardsApi.md#dashboards_get_dashboard_item_data_sync) | **POST** /{dataViewName}/Dashboards/{dashboardId}/Items/{dashboardItemId}/CalculateSync | EXPERIMENTAL: Return data needed to render visualisation for dashboard item


# **dashboards_get_dashboard_item_data_sync**
> DashboardItemDataResult dashboards_get_dashboard_item_data_sync(data_view_name, dashboard_id, dashboard_item_id, timeout_in_seconds=timeout_in_seconds, request_data=request_data)

EXPERIMENTAL: Return data needed to render visualisation for dashboard item

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
dashboard_id = 56 # int | The id of the dashboard to calculate the result for
dashboard_item_id = 'dashboard_item_id_example' # str | The id of the dashboard item to calculate the results for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out. Leave unspecified to use the default value given in the dashboards service's configuration (optional)
request_data = apteco_api.DashboardItemData() # DashboardItemData | Used to filter the data on the dashboard item and define the drill down level (optional)

try:
    # EXPERIMENTAL: Return data needed to render visualisation for dashboard item
    api_response = api_instance.dashboards_get_dashboard_item_data_sync(data_view_name, dashboard_id, dashboard_item_id, timeout_in_seconds=timeout_in_seconds, request_data=request_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboards_get_dashboard_item_data_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to calculate the result for | 
 **dashboard_item_id** | **str**| The id of the dashboard item to calculate the results for | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out. Leave unspecified to use the default value given in the dashboards service&#39;s configuration | [optional] 
 **request_data** | [**DashboardItemData**](DashboardItemData.md)| Used to filter the data on the dashboard item and define the drill down level | [optional] 

### Return type

[**DashboardItemDataResult**](DashboardItemDataResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculation completed successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to access this dashboard. |  -  |
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

