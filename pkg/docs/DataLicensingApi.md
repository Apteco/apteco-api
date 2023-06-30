# apteco_api.DataLicensingApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_licensing_cancel_data_purchase_job**](DataLicensingApi.md#data_licensing_cancel_data_purchase_job) | **DELETE** /{dataViewName}/DataLicensing/{systemName}/DataPurchaseJobs/{jobId} | Cancel a running data purchasing job
[**data_licensing_cancel_licensing_sets_job**](DataLicensingApi.md#data_licensing_cancel_licensing_sets_job) | **DELETE** /{dataViewName}/DataLicensing/{systemName}/LicensingSetsJobs/{jobId} | Cancel a running licensing sets job
[**data_licensing_create_get_licensing_sets_job**](DataLicensingApi.md#data_licensing_create_get_licensing_sets_job) | **POST** /{dataViewName}/DataLicensing/{systemName}/LicensingSetsJobs | Create a new job to get the available licensing sets for a system
[**data_licensing_create_purchase_data_licensing_job**](DataLicensingApi.md#data_licensing_create_purchase_data_licensing_job) | **POST** /{dataViewName}/DataLicensing/{systemName}/DataPurchaseJobs | Create a new job to purchase data licensing information
[**data_licensing_get_data_licensing_system**](DataLicensingApi.md#data_licensing_get_data_licensing_system) | **GET** /{dataViewName}/DataLicensing/{systemName} | SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level details for the specified FastStats system to license data from
[**data_licensing_get_data_licensing_systems**](DataLicensingApi.md#data_licensing_get_data_licensing_systems) | **GET** /{dataViewName}/DataLicensing | SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for licensing data from
[**data_licensing_get_data_purchase_job**](DataLicensingApi.md#data_licensing_get_data_purchase_job) | **GET** /{dataViewName}/DataLicensing/{systemName}/DataPurchaseJobs/{jobId} | Get the status of a running purchase job
[**data_licensing_get_licensing_sets_job**](DataLicensingApi.md#data_licensing_get_licensing_sets_job) | **GET** /{dataViewName}/DataLicensing/{systemName}/LicensingSetsJobs/{jobId} | Get the status of a running licensing sets job
[**data_licensing_get_licensing_sets_sync**](DataLicensingApi.md#data_licensing_get_licensing_sets_sync) | **GET** /{dataViewName}/DataLicensing/{systemName}/LicensingSets | Get the licensing sets for a system
[**data_licensing_purchase_data_licensing_sync**](DataLicensingApi.md#data_licensing_purchase_data_licensing_sync) | **POST** /{dataViewName}/DataLicensing/{systemName}/PurchaseSync | Purchase data licensing information


# **data_licensing_cancel_data_purchase_job**
> data_licensing_cancel_data_purchase_job(data_view_name, system_name, job_id)

Cancel a running data purchasing job

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running data purchasing job
        api_instance.data_licensing_cancel_data_purchase_job(data_view_name, system_name, job_id)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_cancel_data_purchase_job: %s\n" % e)
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

# **data_licensing_cancel_licensing_sets_job**
> data_licensing_cancel_licensing_sets_job(data_view_name, system_name, job_id)

Cancel a running licensing sets job

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running licensing sets job
        api_instance.data_licensing_cancel_licensing_sets_job(data_view_name, system_name, job_id)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_cancel_licensing_sets_job: %s\n" % e)
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

# **data_licensing_create_get_licensing_sets_job**
> LicensingSetsJobDetail data_licensing_create_get_licensing_sets_job(data_view_name, system_name)

Create a new job to get the available licensing sets for a system

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on

    try:
        # Create a new job to get the available licensing sets for a system
        api_response = api_instance.data_licensing_create_get_licensing_sets_job(data_view_name, system_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_create_get_licensing_sets_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 

### Return type

[**LicensingSetsJobDetail**](LicensingSetsJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The licensing sets job was successfully created |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the available licensing sets. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_licensing_create_purchase_data_licensing_job**
> DataPurchaseJobDetail data_licensing_create_purchase_data_licensing_job(data_view_name, system_name, purchase_detail=purchase_detail)

Create a new job to purchase data licensing information

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
purchase_detail = apteco_api.DataPurchaseDetail() # DataPurchaseDetail | The details for the data licensing purchase (optional)

    try:
        # Create a new job to purchase data licensing information
        api_response = api_instance.data_licensing_create_purchase_data_licensing_job(data_view_name, system_name, purchase_detail=purchase_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_create_purchase_data_licensing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **purchase_detail** | [**DataPurchaseDetail**](DataPurchaseDetail.md)| The details for the data licensing purchase | [optional] 

### Return type

[**DataPurchaseJobDetail**](DataPurchaseJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The purchase data licensing info job was successfully created |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to create a purchasing job. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_licensing_get_data_licensing_system**
> DataLicensingSystemDetail data_licensing_get_data_licensing_system(data_view_name, system_name)

SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level details for the specified FastStats system to license data from

SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to return details for

    try:
        # SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level details for the specified FastStats system to license data from
        api_response = api_instance.data_licensing_get_data_licensing_system(data_view_name, system_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_get_data_licensing_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to return details for | 

### Return type

[**DataLicensingSystemDetail**](DataLicensingSystemDetail.md)

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

# **data_licensing_get_data_licensing_systems**
> PagedResultsDataLicensingSystemSummary data_licensing_get_data_licensing_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for licensing data from

SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for licensing data from
        api_response = api_instance.data_licensing_get_data_licensing_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_get_data_licensing_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsDataLicensingSystemSummary**](PagedResultsDataLicensingSystemSummary.md)

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

# **data_licensing_get_data_purchase_job**
> DataPurchaseJobDetail data_licensing_get_data_purchase_job(data_view_name, system_name, job_id)

Get the status of a running purchase job

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to get the status for.

    try:
        # Get the status of a running purchase job
        api_response = api_instance.data_licensing_get_data_purchase_job(data_view_name, system_name, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_get_data_purchase_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **job_id** | **int**| The id of the job to get the status for. | 

### Return type

[**DataPurchaseJobDetail**](DataPurchaseJobDetail.md)

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
**403** | The given session is not allowed to get the status of this purchasing job. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_licensing_get_licensing_sets_job**
> LicensingSetsJobDetail data_licensing_get_licensing_sets_job(data_view_name, system_name, job_id)

Get the status of a running licensing sets job

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to get the status for.

    try:
        # Get the status of a running licensing sets job
        api_response = api_instance.data_licensing_get_licensing_sets_job(data_view_name, system_name, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_get_licensing_sets_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **job_id** | **int**| The id of the job to get the status for. | 

### Return type

[**LicensingSetsJobDetail**](LicensingSetsJobDetail.md)

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
**403** | The given session is not allowed to get the status of this licensing sets job. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_licensing_get_licensing_sets_sync**
> PagedResultsLicensingSet data_licensing_get_licensing_sets_sync(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count)

Get the licensing sets for a system

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Get the licensing sets for a system
        api_response = api_instance.data_licensing_get_licensing_sets_sync(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_get_licensing_sets_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service&#39;s configuration | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsLicensingSet**](PagedResultsLicensingSet.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the available licensing sets |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the available licensing sets. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_licensing_purchase_data_licensing_sync**
> PurchaseInfo data_licensing_purchase_data_licensing_sync(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, purchase_detail=purchase_detail)

Purchase data licensing information

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
    api_instance = apteco_api.DataLicensingApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
purchase_detail = apteco_api.DataPurchaseDetail() # DataPurchaseDetail | The details for the data licensing purchase (optional)

    try:
        # Purchase data licensing information
        api_response = api_instance.data_licensing_purchase_data_licensing_sync(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, purchase_detail=purchase_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataLicensingApi->data_licensing_purchase_data_licensing_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service&#39;s configuration | [optional] 
 **purchase_detail** | [**DataPurchaseDetail**](DataPurchaseDetail.md)| The details for the data licensing purchase | [optional] 

### Return type

[**PurchaseInfo**](PurchaseInfo.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The purchase completed successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to purchase records. |  -  |
**404** | The DataView or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

