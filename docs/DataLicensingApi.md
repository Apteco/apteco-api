# apteco_api.DataLicensingApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_licensing_cancel_data_purchase_job**](DataLicensingApi.md#data_licensing_cancel_data_purchase_job) | **DELETE** /{dataViewName}/DataLicensing/{systemName}/DataPurchaseJobs/{jobId} | UNDER DEVELOPMENT: Cancel a running data purchasing job
[**data_licensing_create_purchase_data_licensing_job**](DataLicensingApi.md#data_licensing_create_purchase_data_licensing_job) | **POST** /{dataViewName}/DataLicensing/{systemName}/DataPurchaseJobs | UNDER DEVELOPMENT: Create a new job to purchase data licensing information
[**data_licensing_get_data_purchase_job**](DataLicensingApi.md#data_licensing_get_data_purchase_job) | **GET** /{dataViewName}/DataLicensing/{systemName}/DataPurchaseJobs/{jobId} | UNDER DEVELOPMENT: Get the status of a running purchase job
[**data_licensing_get_licensing_sets_sync**](DataLicensingApi.md#data_licensing_get_licensing_sets_sync) | **GET** /{dataViewName}/DataLicensing/{systemName}/LicensingSets | UNDER DEVELOPMENT: Get the licensing sets for a system
[**data_licensing_purchase_data_licensing_sync**](DataLicensingApi.md#data_licensing_purchase_data_licensing_sync) | **POST** /{dataViewName}/DataLicensing/{systemName}/PurchaseSync | UNDER DEVELOPMENT: Purchase data licensing information


# **data_licensing_cancel_data_purchase_job**
> data_licensing_cancel_data_purchase_job(data_view_name, system_name, job_id)

UNDER DEVELOPMENT: Cancel a running data purchasing job

UNDER DEVELOPMENT

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
api_instance = apteco_api.DataLicensingApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to cancel

try:
    # UNDER DEVELOPMENT: Cancel a running data purchasing job
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

# **data_licensing_create_purchase_data_licensing_job**
> DataPurchaseJobDetail data_licensing_create_purchase_data_licensing_job(data_view_name, system_name, purchase_detail=purchase_detail)

UNDER DEVELOPMENT: Create a new job to purchase data licensing information

UNDER DEVELOPMENT

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
api_instance = apteco_api.DataLicensingApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
purchase_detail = apteco_api.DataPurchaseDetail() # DataPurchaseDetail | The details for the data licensing purchase (optional)

try:
    # UNDER DEVELOPMENT: Create a new job to purchase data licensing information
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

# **data_licensing_get_data_purchase_job**
> DataPurchaseJobDetail data_licensing_get_data_purchase_job(data_view_name, system_name, job_id)

UNDER DEVELOPMENT: Get the status of a running purchase job

UNDER DEVELOPMENT

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
api_instance = apteco_api.DataLicensingApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
job_id = 56 # int | The id of the job to get the status for.

try:
    # UNDER DEVELOPMENT: Get the status of a running purchase job
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

# **data_licensing_get_licensing_sets_sync**
> PagedResultsLicensingSet data_licensing_get_licensing_sets_sync(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count)

UNDER DEVELOPMENT: Get the licensing sets for a system

UNDER DEVELOPMENT

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
api_instance = apteco_api.DataLicensingApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # UNDER DEVELOPMENT: Get the licensing sets for a system
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
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name | [optional] 
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

UNDER DEVELOPMENT: Purchase data licensing information

UNDER DEVELOPMENT

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
api_instance = apteco_api.DataLicensingApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
purchase_detail = apteco_api.DataPurchaseDetail() # DataPurchaseDetail | The details for the data licensing purchase (optional)

try:
    # UNDER DEVELOPMENT: Purchase data licensing information
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

