# apteco_api.VisualisationsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**visualisations_cancel_visualisation_render_data_refresh_job**](VisualisationsApi.md#visualisations_cancel_visualisation_render_data_refresh_job) | **DELETE** /{dataViewName}/Visualisations/{visualisationId}/RenderData/RefreshJobs/{refreshRequestId} | Cancel a job refreshing the render data for a particular visualisation
[**visualisations_create_visualisation_render_data_refresh_job**](VisualisationsApi.md#visualisations_create_visualisation_render_data_refresh_job) | **POST** /{dataViewName}/Visualisations/{visualisationId}/RenderData/RefreshJobs | Creates a job to refresh the render data for a particular visualisation
[**visualisations_get_visualisation**](VisualisationsApi.md#visualisations_get_visualisation) | **GET** /{dataViewName}/Visualisations/{visualisationId} | Returns the details of a particular visualisation
[**visualisations_get_visualisation_render_data**](VisualisationsApi.md#visualisations_get_visualisation_render_data) | **GET** /{dataViewName}/Visualisations/{visualisationId}/RenderData | Returns the render data for a particular visualisation
[**visualisations_get_visualisation_render_data_refresh_job**](VisualisationsApi.md#visualisations_get_visualisation_render_data_refresh_job) | **GET** /{dataViewName}/Visualisations/{visualisationId}/RenderData/RefreshJobs/{refreshRequestId} | Returns the details of a job to refresh the render data for a particular visualisation
[**visualisations_perform_visualisation_render_data_refresh_synchronously**](VisualisationsApi.md#visualisations_perform_visualisation_render_data_refresh_synchronously) | **POST** /{dataViewName}/Visualisations/{visualisationId}/RenderData/RefreshSync | Performs a synchronous refresh of the render data for a particular visualisation


# **visualisations_cancel_visualisation_render_data_refresh_job**
> visualisations_cancel_visualisation_render_data_refresh_job(data_view_name, visualisation_id, refresh_request_id)

Cancel a job refreshing the render data for a particular visualisation

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
    api_instance = apteco_api.VisualisationsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
visualisation_id = 'visualisation_id_example' # str | The id of the visualisation that the job is refreshing
refresh_request_id = 56 # int | The id of the refresh job to cancel

    try:
        # Cancel a job refreshing the render data for a particular visualisation
        api_instance.visualisations_cancel_visualisation_render_data_refresh_job(data_view_name, visualisation_id, refresh_request_id)
    except ApiException as e:
        print("Exception when calling VisualisationsApi->visualisations_cancel_visualisation_render_data_refresh_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **visualisation_id** | **str**| The id of the visualisation that the job is refreshing | 
 **refresh_request_id** | **int**| The id of the refresh job to cancel | 

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
**204** | The refresh job was cancelled successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this visualisation |  -  |
**404** | The DataView, visualisation or refresh job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualisations_create_visualisation_render_data_refresh_job**
> RenderDataRefreshJobDetail visualisations_create_visualisation_render_data_refresh_job(data_view_name, visualisation_id)

Creates a job to refresh the render data for a particular visualisation

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
    api_instance = apteco_api.VisualisationsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
visualisation_id = 'visualisation_id_example' # str | The id of the visualisation that the job is to refresh

    try:
        # Creates a job to refresh the render data for a particular visualisation
        api_response = api_instance.visualisations_create_visualisation_render_data_refresh_job(data_view_name, visualisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VisualisationsApi->visualisations_create_visualisation_render_data_refresh_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **visualisation_id** | **str**| The id of the visualisation that the job is to refresh | 

### Return type

[**RenderDataRefreshJobDetail**](RenderDataRefreshJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The refresh job was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this visualisation |  -  |
**404** | The DataView or visualisation couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualisations_get_visualisation**
> VisualisationDetail visualisations_get_visualisation(data_view_name, visualisation_id)

Returns the details of a particular visualisation

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
    api_instance = apteco_api.VisualisationsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
visualisation_id = 'visualisation_id_example' # str | The id of the visualisation to view

    try:
        # Returns the details of a particular visualisation
        api_response = api_instance.visualisations_get_visualisation(data_view_name, visualisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VisualisationsApi->visualisations_get_visualisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **visualisation_id** | **str**| The id of the visualisation to view | 

### Return type

[**VisualisationDetail**](VisualisationDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visualisation details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this visualisation |  -  |
**404** | The DataView or visualisation couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualisations_get_visualisation_render_data**
> AbstractRenderSpec visualisations_get_visualisation_render_data(data_view_name, visualisation_id)

Returns the render data for a particular visualisation

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
    api_instance = apteco_api.VisualisationsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
visualisation_id = 'visualisation_id_example' # str | The id of the visualisation to generate the render data for

    try:
        # Returns the render data for a particular visualisation
        api_response = api_instance.visualisations_get_visualisation_render_data(data_view_name, visualisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VisualisationsApi->visualisations_get_visualisation_render_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **visualisation_id** | **str**| The id of the visualisation to generate the render data for | 

### Return type

[**AbstractRenderSpec**](AbstractRenderSpec.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visualisation render data |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this visualisation |  -  |
**404** | The DataView or visualisation couldn&#39;t be found or the visualisation hasn&#39;t been rendered yet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualisations_get_visualisation_render_data_refresh_job**
> RenderDataRefreshJobDetail visualisations_get_visualisation_render_data_refresh_job(data_view_name, visualisation_id, refresh_request_id)

Returns the details of a job to refresh the render data for a particular visualisation

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
    api_instance = apteco_api.VisualisationsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
visualisation_id = 'visualisation_id_example' # str | The id of the visualisation that the job is refreshing
refresh_request_id = 56 # int | The id of the refresh job to view

    try:
        # Returns the details of a job to refresh the render data for a particular visualisation
        api_response = api_instance.visualisations_get_visualisation_render_data_refresh_job(data_view_name, visualisation_id, refresh_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VisualisationsApi->visualisations_get_visualisation_render_data_refresh_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **visualisation_id** | **str**| The id of the visualisation that the job is refreshing | 
 **refresh_request_id** | **int**| The id of the refresh job to view | 

### Return type

[**RenderDataRefreshJobDetail**](RenderDataRefreshJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The refresh job details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this visualisation |  -  |
**404** | The DataView, visualisation or refresh job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualisations_perform_visualisation_render_data_refresh_synchronously**
> AbstractRenderSpec visualisations_perform_visualisation_render_data_refresh_synchronously(data_view_name, visualisation_id, timeout_in_seconds=timeout_in_seconds)

Performs a synchronous refresh of the render data for a particular visualisation

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
    api_instance = apteco_api.VisualisationsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
visualisation_id = 'visualisation_id_example' # str | The id of the visualisation to generate the render data for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the visualisation service's configuration (optional)

    try:
        # Performs a synchronous refresh of the render data for a particular visualisation
        api_response = api_instance.visualisations_perform_visualisation_render_data_refresh_synchronously(data_view_name, visualisation_id, timeout_in_seconds=timeout_in_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VisualisationsApi->visualisations_perform_visualisation_render_data_refresh_synchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **visualisation_id** | **str**| The id of the visualisation to generate the render data for | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the visualisation service&#39;s configuration | [optional] 

### Return type

[**AbstractRenderSpec**](AbstractRenderSpec.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visualisation render data |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this visualisation |  -  |
**404** | The DataView or visualisation couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

