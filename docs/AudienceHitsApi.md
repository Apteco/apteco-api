# apteco_api.AudienceHitsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_hits_get_audience_hit**](AudienceHitsApi.md#audience_hits_get_audience_hit) | **GET** /{dataViewName}/AudienceHits/{audienceHitId} | Requires OrbitAdmin: Returns details for a given audience hit
[**audience_hits_get_audience_hits**](AudienceHitsApi.md#audience_hits_get_audience_hits) | **GET** /{dataViewName}/AudienceHits | Requires OrbitAdmin: Returns all the hit information for all audiences.


# **audience_hits_get_audience_hit**
> AudienceHitDetail audience_hits_get_audience_hit(data_view_name, audience_hit_id)

Requires OrbitAdmin: Returns details for a given audience hit

This endpoint is only available for users with the OrbitAdmin role

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
api_instance = apteco_api.AudienceHitsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_hit_id = 56 # int | The id of the hit

try:
    # Requires OrbitAdmin: Returns details for a given audience hit
    api_response = api_instance.audience_hits_get_audience_hit(data_view_name, audience_hit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceHitsApi->audience_hits_get_audience_hit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_hit_id** | **int**| The id of the hit | 

### Return type

[**AudienceHitDetail**](AudienceHitDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the given audience hit |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView or audience hit couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audience_hits_get_audience_hits**
> PagedResultsAudienceHitSummary audience_hits_get_audience_hits(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns all the hit information for all audiences.

This endpoint is only available for users with the OrbitAdmin role

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
api_instance = apteco_api.AudienceHitsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, Timestamp, UserAgentDetails (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Returns all the hit information for all audiences.
    api_response = api_instance.audience_hits_get_audience_hits(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceHitsApi->audience_hits_get_audience_hits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, Timestamp, UserAgentDetails | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAudienceHitSummary**](PagedResultsAudienceHitSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all audiences hits |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

