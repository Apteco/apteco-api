# apteco_api.FastStatsBuildsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fast_stats_builds_cancel_fast_stats_build_job**](FastStatsBuildsApi.md#fast_stats_builds_cancel_fast_stats_build_job) | **DELETE** /{dataViewName}/FastStatsBuilds/{systemName}/BuildJobs/{jobId} | EXPERIMENTAL: Requires OrbitAdmin: Cancel a running data purchasing job
[**fast_stats_builds_create_fast_stats_build_job**](FastStatsBuildsApi.md#fast_stats_builds_create_fast_stats_build_job) | **POST** /{dataViewName}/FastStatsBuilds/{systemName}/BuildJobs | EXPERIMENTAL: Requires OrbitAdmin: Create a new job to builds a FastStats system from the given definition
[**fast_stats_builds_fast_stats_build_sync**](FastStatsBuildsApi.md#fast_stats_builds_fast_stats_build_sync) | **POST** /{dataViewName}/FastStatsBuilds/{systemName}/BuildSync | EXPERIMENTAL: Requires OrbitAdmin: Builds a FastStats system from the given definition
[**fast_stats_builds_get_fast_stats_build_job**](FastStatsBuildsApi.md#fast_stats_builds_get_fast_stats_build_job) | **GET** /{dataViewName}/FastStatsBuilds/{systemName}/BuildJobs/{jobId} | EXPERIMENTAL: Requires OrbitAdmin: Get the status of a running FastStats build job


# **fast_stats_builds_cancel_fast_stats_build_job**
> fast_stats_builds_cancel_fast_stats_build_job(data_view_name, system_name, job_id)

EXPERIMENTAL: Requires OrbitAdmin: Cancel a running data purchasing job

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
    api_instance = apteco_api.FastStatsBuildsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to cancel

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Cancel a running data purchasing job
        api_instance.fast_stats_builds_cancel_fast_stats_build_job(data_view_name, system_name, job_id)
    except ApiException as e:
        print("Exception when calling FastStatsBuildsApi->fast_stats_builds_cancel_fast_stats_build_job: %s\n" % e)
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
**403** | The given session is not allowed to cancel this purchasing job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_builds_create_fast_stats_build_job**
> BuildJobDetail fast_stats_builds_create_fast_stats_build_job(data_view_name, system_name, build_definition=build_definition)

EXPERIMENTAL: Requires OrbitAdmin: Create a new job to builds a FastStats system from the given definition

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
    api_instance = apteco_api.FastStatsBuildsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
build_definition = apteco_api.BuildDefinition() # BuildDefinition | The details needed to build the system (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Create a new job to builds a FastStats system from the given definition
        api_response = api_instance.fast_stats_builds_create_fast_stats_build_job(data_view_name, system_name, build_definition=build_definition)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsBuildsApi->fast_stats_builds_create_fast_stats_build_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **build_definition** | [**BuildDefinition**](BuildDefinition.md)| The details needed to build the system | [optional] 

### Return type

[**BuildJobDetail**](BuildJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The build job job was successfully created |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to build systems. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_builds_fast_stats_build_sync**
> BuildResult fast_stats_builds_fast_stats_build_sync(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, build_definition=build_definition)

EXPERIMENTAL: Requires OrbitAdmin: Builds a FastStats system from the given definition

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
    api_instance = apteco_api.FastStatsBuildsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the build service's configuration (optional)
build_definition = apteco_api.BuildDefinition() # BuildDefinition | The details needed to build the system (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Builds a FastStats system from the given definition
        api_response = api_instance.fast_stats_builds_fast_stats_build_sync(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, build_definition=build_definition)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsBuildsApi->fast_stats_builds_fast_stats_build_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the build service&#39;s configuration | [optional] 
 **build_definition** | [**BuildDefinition**](BuildDefinition.md)| The details needed to build the system | [optional] 

### Return type

[**BuildResult**](BuildResult.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | The build job completed |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to build systems. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_builds_get_fast_stats_build_job**
> BuildJobDetail fast_stats_builds_get_fast_stats_build_job(data_view_name, system_name, job_id)

EXPERIMENTAL: Requires OrbitAdmin: Get the status of a running FastStats build job

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
    api_instance = apteco_api.FastStatsBuildsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to get the status for.

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Get the status of a running FastStats build job
        api_response = api_instance.fast_stats_builds_get_fast_stats_build_job(data_view_name, system_name, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsBuildsApi->fast_stats_builds_get_fast_stats_build_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **job_id** | **int**| The id of the job to get the status for. | 

### Return type

[**BuildJobDetail**](BuildJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job status details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the status of this FastStats build job. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

