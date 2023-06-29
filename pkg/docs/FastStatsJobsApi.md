# apteco_api.FastStatsJobsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fast_stats_jobs_calculate_processing_time_stats_for_system_sync**](FastStatsJobsApi.md#fast_stats_jobs_calculate_processing_time_stats_for_system_sync) | **POST** /{dataViewName}/FastStatsJobs/{systemName}/CalculateProcessingTimeStatsSync | EXPERIMENTAL: Requires OrbitAdmin: Calculate processing statistics for the specified jobs in the FastStats job queue for the given system.
[**fast_stats_jobs_calculate_processing_time_stats_sync**](FastStatsJobsApi.md#fast_stats_jobs_calculate_processing_time_stats_sync) | **POST** /{dataViewName}/FastStatsJobs/CalculateProcessingTimeStatsSync | EXPERIMENTAL: Requires OrbitAdmin: Calculate processing statistics for the specified jobs in the FastStats job queue for all systems in a particular DataView.
[**fast_stats_jobs_get_fast_stats_job**](FastStatsJobsApi.md#fast_stats_jobs_get_fast_stats_job) | **GET** /{dataViewName}/FastStatsJobs/{systemName}/{jobId} | EXPERIMENTAL: Requires OrbitAdmin: Gets details for a particular job in the FastStats job queue for the given system.
[**fast_stats_jobs_get_fast_stats_jobs**](FastStatsJobsApi.md#fast_stats_jobs_get_fast_stats_jobs) | **GET** /{dataViewName}/FastStatsJobs | EXPERIMENTAL: Requires OrbitAdmin: Gets all the jobs in the FastStats job queue for all systems in a particular DataView.
[**fast_stats_jobs_get_fast_stats_jobs_for_system**](FastStatsJobsApi.md#fast_stats_jobs_get_fast_stats_jobs_for_system) | **GET** /{dataViewName}/FastStatsJobs/{systemName} | EXPERIMENTAL: Requires OrbitAdmin: Gets all the jobs in the FastStats job queue for the given system.


# **fast_stats_jobs_calculate_processing_time_stats_for_system_sync**
> ProcessingTimeStatistics fast_stats_jobs_calculate_processing_time_stats_for_system_sync(data_view_name, system_name, processing_time_statistics_details=processing_time_statistics_details)

EXPERIMENTAL: Requires OrbitAdmin: Calculate processing statistics for the specified jobs in the FastStats job queue for the given system.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.FastStatsJobsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
processing_time_statistics_details = apteco_api.ProcessingTimeStatisticsDetails() # ProcessingTimeStatisticsDetails | The details to calcuate the stats with (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Calculate processing statistics for the specified jobs in the FastStats job queue for the given system.
        api_response = api_instance.fast_stats_jobs_calculate_processing_time_stats_for_system_sync(data_view_name, system_name, processing_time_statistics_details=processing_time_statistics_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsJobsApi->fast_stats_jobs_calculate_processing_time_stats_for_system_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **processing_time_statistics_details** | [**ProcessingTimeStatisticsDetails**](ProcessingTimeStatisticsDetails.md)| The details to calcuate the stats with | [optional] 

### Return type

[**ProcessingTimeStatistics**](ProcessingTimeStatistics.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics about the distribution of job times for the specified jobs |  -  |
**400** | A bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | No jobs could be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_jobs_calculate_processing_time_stats_sync**
> ProcessingTimeStatistics fast_stats_jobs_calculate_processing_time_stats_sync(data_view_name, processing_time_statistics_details=processing_time_statistics_details)

EXPERIMENTAL: Requires OrbitAdmin: Calculate processing statistics for the specified jobs in the FastStats job queue for all systems in a particular DataView.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.FastStatsJobsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
processing_time_statistics_details = apteco_api.ProcessingTimeStatisticsDetails() # ProcessingTimeStatisticsDetails | The details to calcuate the stats with (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Calculate processing statistics for the specified jobs in the FastStats job queue for all systems in a particular DataView.
        api_response = api_instance.fast_stats_jobs_calculate_processing_time_stats_sync(data_view_name, processing_time_statistics_details=processing_time_statistics_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsJobsApi->fast_stats_jobs_calculate_processing_time_stats_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **processing_time_statistics_details** | [**ProcessingTimeStatisticsDetails**](ProcessingTimeStatisticsDetails.md)| The details to calcuate the stats with | [optional] 

### Return type

[**ProcessingTimeStatistics**](ProcessingTimeStatistics.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics about the distribution of job times for the specified jobs |  -  |
**400** | A bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | No jobs could be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_jobs_get_fast_stats_job**
> JobDetail fast_stats_jobs_get_fast_stats_job(data_view_name, system_name, job_id, return_request=return_request, return_results=return_results)

EXPERIMENTAL: Requires OrbitAdmin: Gets details for a particular job in the FastStats job queue for the given system.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.FastStatsJobsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the system the job is in
job_id = 56 # int | The id of the FastStats job
return_request = True # bool | Whether to return the request XML for the job.  Defaults to false (optional)
return_results = True # bool | Whether to return the result XML for the job.  Defaults to false (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Gets details for a particular job in the FastStats job queue for the given system.
        api_response = api_instance.fast_stats_jobs_get_fast_stats_job(data_view_name, system_name, job_id, return_request=return_request, return_results=return_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsJobsApi->fast_stats_jobs_get_fast_stats_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the system the job is in | 
 **job_id** | **int**| The id of the FastStats job | 
 **return_request** | **bool**| Whether to return the request XML for the job.  Defaults to false | [optional] 
 **return_results** | **bool**| Whether to return the result XML for the job.  Defaults to false | [optional] 

### Return type

[**JobDetail**](JobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of jobs |  -  |
**400** | A bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | No jobs could be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_jobs_get_fast_stats_jobs**
> PagedResultsJobSummary fast_stats_jobs_get_fast_stats_jobs(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

EXPERIMENTAL: Requires OrbitAdmin: Gets all the jobs in the FastStats job queue for all systems in a particular DataView.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.FastStatsJobsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Gets all the jobs in the FastStats job queue for all systems in a particular DataView.
        api_response = api_instance.fast_stats_jobs_get_fast_stats_jobs(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsJobsApi->fast_stats_jobs_get_fast_stats_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsJobSummary**](PagedResultsJobSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of jobs |  -  |
**400** | A bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | No jobs could be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_jobs_get_fast_stats_jobs_for_system**
> PagedResultsJobSummary fast_stats_jobs_get_fast_stats_jobs_for_system(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

EXPERIMENTAL: Requires OrbitAdmin: Gets all the jobs in the FastStats job queue for the given system.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.FastStatsJobsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the system to return jobs for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Gets all the jobs in the FastStats job queue for the given system.
        api_response = api_instance.fast_stats_jobs_get_fast_stats_jobs_for_system(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsJobsApi->fast_stats_jobs_get_fast_stats_jobs_for_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the system to return jobs for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsJobSummary**](PagedResultsJobSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of jobs |  -  |
**400** | A bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | No jobs could be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

