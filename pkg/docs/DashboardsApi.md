# apteco_api.DashboardsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboards_batch_get_dashboard_job_results**](DashboardsApi.md#dashboards_batch_get_dashboard_job_results) | **POST** /{dataViewName}/Dashboards/{dashboardId}/Items/CalculateJobs/Results | Return data needed to render visualisation for dashboard item(s) or the status of the job(s) if not complete
[**dashboards_calculate_dashboard_data**](DashboardsApi.md#dashboards_calculate_dashboard_data) | **POST** /{dataViewName}/Dashboards/{dashboardId}/Items/CalculateJobs | Aysyncrounously request data needed to render an array of dashboard items
[**dashboards_cancel_calculate_dashboard_data_job**](DashboardsApi.md#dashboards_cancel_calculate_dashboard_data_job) | **DELETE** /{dataViewName}/Dashboards/{dashboardId}/Items/CalculateJobs/{jobId} | Cancel a running calculate dashboard data job
[**dashboards_cancel_dashboard_item_preview_data_job**](DashboardsApi.md#dashboards_cancel_dashboard_item_preview_data_job) | **DELETE** /{dataViewName}/Dashboards/{systemName}/DashboardItemPreviewJobs/{jobId} | Cancel a running dashboard item preview job
[**dashboards_convert_to_audience**](DashboardsApi.md#dashboards_convert_to_audience) | **POST** /{dataViewName}/Dashboards/{dashboardId}/ConvertToAudience | Converts a dashboard (including any global filters applied) to an Audience
[**dashboards_copy_dashboard**](DashboardsApi.md#dashboards_copy_dashboard) | **POST** /{dataViewName}/Dashboards/{dashboardId}/Copy | Copies an existing dashboard for the logged in user.
[**dashboards_create_dashboard**](DashboardsApi.md#dashboards_create_dashboard) | **POST** /{dataViewName}/Dashboards | Creates a new dashboard from the given details for the logged in user.
[**dashboards_create_dashboard_item_preview_data_jobs**](DashboardsApi.md#dashboards_create_dashboard_item_preview_data_jobs) | **POST** /{dataViewName}/Dashboards/{systemName}/DashboardItemPreviewJobs | Submit an array of jobs to calculate the data needed to render visualisation previews
[**dashboards_create_dashboard_update**](DashboardsApi.md#dashboards_create_dashboard_update) | **POST** /{dataViewName}/Dashboards/{dashboardId}/Updates | Updates the details of a particular dashboard.  If you don&#39;t have an id for the  dashboard then POST to the /Dashboards URL to create a new dashboard.
[**dashboards_delete_dashboard**](DashboardsApi.md#dashboards_delete_dashboard) | **DELETE** /{dataViewName}/Dashboards/{dashboardId} | Deletes the specified dashboard
[**dashboards_get_dashboard_export_sync**](DashboardsApi.md#dashboards_get_dashboard_export_sync) | **POST** /{dataViewName}/Dashboards/{dashboardId}/ExportSync | Return export data needed to view the underlying data for a dashboard
[**dashboards_get_dashboard_item_data_sync**](DashboardsApi.md#dashboards_get_dashboard_item_data_sync) | **POST** /{dataViewName}/Dashboards/{dashboardId}/Items/{dashboardItemId}/CalculateSync | Return data needed to render visualisation for dashboard item
[**dashboards_get_dashboard_item_preview_data_job**](DashboardsApi.md#dashboards_get_dashboard_item_preview_data_job) | **GET** /{dataViewName}/Dashboards/{systemName}/DashboardItemPreviewJobs/{jobId} | Return data needed to render visualisation for dashboard item when previewing
[**dashboards_get_dashboard_item_preview_data_jobs**](DashboardsApi.md#dashboards_get_dashboard_item_preview_data_jobs) | **POST** /{dataViewName}/Dashboards/{systemName}/Items/DashboardItemPreviewJobs/Results | Return data needed to render visualisation for dashboard preview item (s) or the status of the job(s) if not complete
[**dashboards_get_dashboard_job_results**](DashboardsApi.md#dashboards_get_dashboard_job_results) | **GET** /{dataViewName}/Dashboards/{dashboardId}/Items/CalculateJobs/{jobId} | Return data needed to render visualisation for dashboard item


# **dashboards_batch_get_dashboard_job_results**
> list[DashboardItemDataJobDetail] dashboards_batch_get_dashboard_job_results(data_view_name, dashboard_id, job_ids=job_ids)

Return data needed to render visualisation for dashboard item(s) or the status of the job(s) if not complete

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to get the results for
job_ids = [56] # list[int] | An array of the jobIds to get the results for (optional)

    try:
        # Return data needed to render visualisation for dashboard item(s) or the status of the job(s) if not complete
        api_response = api_instance.dashboards_batch_get_dashboard_job_results(data_view_name, dashboard_id, job_ids=job_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_batch_get_dashboard_job_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to get the results for | 
 **job_ids** | [**list[int]**](int.md)| An array of the jobIds to get the results for | [optional] 

### Return type

[**list[DashboardItemDataJobDetail]**](DashboardItemDataJobDetail.md)

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
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_calculate_dashboard_data**
> list[CalculateDashboardItemJobCreatedResult] dashboards_calculate_dashboard_data(data_view_name, dashboard_id, timeout_in_seconds=timeout_in_seconds, request_data=request_data)

Aysyncrounously request data needed to render an array of dashboard items

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to calculate the result for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out. Leave unspecified to use the default value given in the dashboards service's configuration (optional)
request_data = apteco_api.CalculateDashboardData() # CalculateDashboardData | Used to filter the data on the dashboard item and define the drill down level (optional)

    try:
        # Aysyncrounously request data needed to render an array of dashboard items
        api_response = api_instance.dashboards_calculate_dashboard_data(data_view_name, dashboard_id, timeout_in_seconds=timeout_in_seconds, request_data=request_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_calculate_dashboard_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to calculate the result for | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out. Leave unspecified to use the default value given in the dashboards service&#39;s configuration | [optional] 
 **request_data** | [**CalculateDashboardData**](CalculateDashboardData.md)| Used to filter the data on the dashboard item and define the drill down level | [optional] 

### Return type

[**list[CalculateDashboardItemJobCreatedResult]**](CalculateDashboardItemJobCreatedResult.md)

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
**404** | The DataView or dashboard couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_cancel_calculate_dashboard_data_job**
> dashboards_cancel_calculate_dashboard_data_job(data_view_name, dashboard_id, job_id)

Cancel a running calculate dashboard data job

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to calculate the result for
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running calculate dashboard data job
        api_instance.dashboards_cancel_calculate_dashboard_data_job(data_view_name, dashboard_id, job_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_cancel_calculate_dashboard_data_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to calculate the result for | 
 **job_id** | **int**| The id of the job to cancel | 

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
**204** | The job was cancelled successful |  -  |
**400** | A bad request |  -  |
**404** | The DataView, system or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_cancel_dashboard_item_preview_data_job**
> dashboards_cancel_dashboard_item_preview_data_job(data_view_name, system_name, job_id)

Cancel a running dashboard item preview job

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running dashboard item preview job
        api_instance.dashboards_cancel_dashboard_item_preview_data_job(data_view_name, system_name, job_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_cancel_dashboard_item_preview_data_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **job_id** | **int**| The id of the job to cancel | 

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
**204** | The job was cancelled successful |  -  |
**400** | A bad request |  -  |
**404** | The DataView, system or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_convert_to_audience**
> ConvertDashboardToAudienceResult dashboards_convert_to_audience(data_view_name, dashboard_id, request_data=request_data)

Converts a dashboard (including any global filters applied) to an Audience

Requires licence flags [AudienceSelection]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to calculate the result for
request_data = apteco_api.ConvertDashboardToAudience() # ConvertDashboardToAudience | Used to pass additional filter query and the name for the new audience (optional)

    try:
        # Converts a dashboard (including any global filters applied) to an Audience
        api_response = api_instance.dashboards_convert_to_audience(data_view_name, dashboard_id, request_data=request_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_convert_to_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to calculate the result for | 
 **request_data** | [**ConvertDashboardToAudience**](ConvertDashboardToAudience.md)| Used to pass additional filter query and the name for the new audience | [optional] 

### Return type

[**ConvertDashboardToAudienceResult**](ConvertDashboardToAudienceResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The calculation completed successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView or dashboard couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_copy_dashboard**
> DashboardDetail dashboards_copy_dashboard(data_view_name, dashboard_id, dashboard_detail=dashboard_detail)

Copies an existing dashboard for the logged in user.

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to copy
dashboard_detail = apteco_api.CopyDashboardDetail() # CopyDashboardDetail | The details used to create the new dashboard (optional)

    try:
        # Copies an existing dashboard for the logged in user.
        api_response = api_instance.dashboards_copy_dashboard(data_view_name, dashboard_id, dashboard_detail=dashboard_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_copy_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to copy | 
 **dashboard_detail** | [**CopyDashboardDetail**](CopyDashboardDetail.md)| The details used to create the new dashboard | [optional] 

### Return type

[**DashboardDetail**](DashboardDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The copy of the specified dashboard was created successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_create_dashboard**
> DashboardDetail dashboards_create_dashboard(data_view_name, dashboard_detail=dashboard_detail)

Creates a new dashboard from the given details for the logged in user.

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_detail = apteco_api.CreateDashboardDetail() # CreateDashboardDetail | The details for the dashboard to create.  If you want              to update a specific dashboard then POST to the /Dashboards/{dashboardId} URL (optional)

    try:
        # Creates a new dashboard from the given details for the logged in user.
        api_response = api_instance.dashboards_create_dashboard(data_view_name, dashboard_detail=dashboard_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_create_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_detail** | [**CreateDashboardDetail**](CreateDashboardDetail.md)| The details for the dashboard to create.  If you want              to update a specific dashboard then POST to the /Dashboards/{dashboardId} URL | [optional] 

### Return type

[**DashboardDetail**](DashboardDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The dashboard was created successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_create_dashboard_item_preview_data_jobs**
> dashboards_create_dashboard_item_preview_data_jobs(data_view_name, system_name, request_data=request_data)

Submit an array of jobs to calculate the data needed to render visualisation previews

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
request_data = [apteco_api.DashboardItemPreviewData()] # list[DashboardItemPreviewData] | The data required to process the request (optional)

    try:
        # Submit an array of jobs to calculate the data needed to render visualisation previews
        api_instance.dashboards_create_dashboard_item_preview_data_jobs(data_view_name, system_name, request_data=request_data)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_create_dashboard_item_preview_data_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **request_data** | [**list[DashboardItemPreviewData]**](DashboardItemPreviewData.md)| The data required to process the request | [optional] 

### Return type

void (empty response body)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculation completed successfully |  -  |
**201** | Success |  -  |
**400** | A bad request |  -  |
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_create_dashboard_update**
> DashboardDetail dashboards_create_dashboard_update(data_view_name, dashboard_id, dashboard_detail=dashboard_detail)

Updates the details of a particular dashboard.  If you don't have an id for the  dashboard then POST to the /Dashboards URL to create a new dashboard.

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to add/update
dashboard_detail = apteco_api.CreateDashboardUpdateDetail() # CreateDashboardUpdateDetail | The details for the dashboard to add/update (optional)

    try:
        # Updates the details of a particular dashboard.  If you don't have an id for the  dashboard then POST to the /Dashboards URL to create a new dashboard.
        api_response = api_instance.dashboards_create_dashboard_update(data_view_name, dashboard_id, dashboard_detail=dashboard_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_create_dashboard_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to add/update | 
 **dashboard_detail** | [**CreateDashboardUpdateDetail**](CreateDashboardUpdateDetail.md)| The details for the dashboard to add/update | [optional] 

### Return type

[**DashboardDetail**](DashboardDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The dashboard details were added/updated successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView or dashboard couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_delete_dashboard**
> dashboards_delete_dashboard(data_view_name, dashboard_id)

Deletes the specified dashboard

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to delete

    try:
        # Deletes the specified dashboard
        api_instance.dashboards_delete_dashboard(data_view_name, dashboard_id)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to delete | 

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
**204** | The dashboard was deleted successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete this dashboard.  Only dashboard owners or admins can delete their dashboards |  -  |
**404** | The DataView or dashboard couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_get_dashboard_export_sync**
> DashboardExportDataResult dashboards_get_dashboard_export_sync(data_view_name, dashboard_id, timeout_in_seconds=timeout_in_seconds, request_data=request_data)

Return export data needed to view the underlying data for a dashboard

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to calculate the result for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out. Leave unspecified to use the default value given in the dashboards service's configuration (optional)
request_data = apteco_api.DashboardExportData() # DashboardExportData | Used to filter the data on the dashboard (optional)

    try:
        # Return export data needed to view the underlying data for a dashboard
        api_response = api_instance.dashboards_get_dashboard_export_sync(data_view_name, dashboard_id, timeout_in_seconds=timeout_in_seconds, request_data=request_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_get_dashboard_export_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to calculate the result for | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out. Leave unspecified to use the default value given in the dashboards service&#39;s configuration | [optional] 
 **request_data** | [**DashboardExportData**](DashboardExportData.md)| Used to filter the data on the dashboard | [optional] 

### Return type

[**DashboardExportDataResult**](DashboardExportDataResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The export completed successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_get_dashboard_item_data_sync**
> DashboardItemDataResultDetail dashboards_get_dashboard_item_data_sync(data_view_name, dashboard_id, dashboard_item_id, timeout_in_seconds=timeout_in_seconds, request_data=request_data)

Return data needed to render visualisation for dashboard item

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to calculate the result for
dashboard_item_id = 'dashboard_item_id_example' # str | The id of the dashboard item to calculate the results for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out. Leave unspecified to use the default value given in the dashboards service's configuration (optional)
request_data = apteco_api.DashboardItemData() # DashboardItemData | Used to filter the data on the dashboard item and define the drill down level (optional)

    try:
        # Return data needed to render visualisation for dashboard item
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

[**DashboardItemDataResultDetail**](DashboardItemDataResultDetail.md)

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
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_get_dashboard_item_preview_data_job**
> DashboardItemDataJobDetail dashboards_get_dashboard_item_preview_data_job(data_view_name, system_name, job_id)

Return data needed to render visualisation for dashboard item when previewing

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the dashboard item to calculate the results for

    try:
        # Return data needed to render visualisation for dashboard item when previewing
        api_response = api_instance.dashboards_get_dashboard_item_preview_data_job(data_view_name, system_name, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_get_dashboard_item_preview_data_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **job_id** | **int**| The id of the dashboard item to calculate the results for | 

### Return type

[**DashboardItemDataJobDetail**](DashboardItemDataJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculation completed successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_get_dashboard_item_preview_data_jobs**
> list[DashboardItemDataJobDetail] dashboards_get_dashboard_item_preview_data_jobs(data_view_name, system_name, job_ids=job_ids)

Return data needed to render visualisation for dashboard preview item (s) or the status of the job(s) if not complete

Requires licence flags [Dashboards]

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_ids = [56] # list[int] | An array of the jobIds to get the results for (optional)

    try:
        # Return data needed to render visualisation for dashboard preview item (s) or the status of the job(s) if not complete
        api_response = api_instance.dashboards_get_dashboard_item_preview_data_jobs(data_view_name, system_name, job_ids=job_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_get_dashboard_item_preview_data_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **job_ids** | [**list[int]**](int.md)| An array of the jobIds to get the results for | [optional] 

### Return type

[**list[DashboardItemDataJobDetail]**](DashboardItemDataJobDetail.md)

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
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_get_dashboard_job_results**
> DashboardItemDataJobDetail dashboards_get_dashboard_job_results(data_view_name, dashboard_id, job_id)

Return data needed to render visualisation for dashboard item

### Example

* Api Key Authentication (faststats_auth):
```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/OrbitAPI
# See configuration.py for a list of all supported configuration parameters.
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: faststats_auth
configuration = apteco_api.Configuration(
    host = "http://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.DashboardsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
dashboard_id = 56 # int | The id of the dashboard to calculate the result for
job_id = 56 # int | The id of the dashboard item to calculate the results for

    try:
        # Return data needed to render visualisation for dashboard item
        api_response = api_instance.dashboards_get_dashboard_job_results(data_view_name, dashboard_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->dashboards_get_dashboard_job_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **dashboard_id** | **int**| The id of the dashboard to calculate the result for | 
 **job_id** | **int**| The id of the dashboard item to calculate the results for | 

### Return type

[**DashboardItemDataJobDetail**](DashboardItemDataJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculation completed successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView or dashboard item couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

