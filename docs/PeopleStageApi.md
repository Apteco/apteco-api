# apteco_api.PeopleStageApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**people_stage_get_people_stage_channel**](PeopleStageApi.md#people_stage_get_people_stage_channel) | **GET** /{dataViewName}/PeopleStage/{systemName}/Channels/{channelId} | Returns the details of a particular PeopleStage channel
[**people_stage_get_people_stage_channels**](PeopleStageApi.md#people_stage_get_people_stage_channels) | **GET** /{dataViewName}/PeopleStage/{systemName}/Channels | Returns the list of PeopleStage channels available in this FastStats system
[**people_stage_get_people_stage_element**](PeopleStageApi.md#people_stage_get_people_stage_element) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId} | Returns the details of a particular PeopleStage element
[**people_stage_get_people_stage_element_channel_statistics**](PeopleStageApi.md#people_stage_get_people_stage_element_channel_statistics) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/ChannelStats | Returns statistics for the total number of communications sent per channel for a particular PeopleStage element
[**people_stage_get_people_stage_element_children**](PeopleStageApi.md#people_stage_get_people_stage_element_children) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/Children | Returns the list of children for a particular PeopleStage element
[**people_stage_get_people_stage_element_communication_statistics**](PeopleStageApi.md#people_stage_get_people_stage_element_communication_statistics) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/CommunicationStats | Returns statistics for the number of communications sent over time for a particular PeopleStage element
[**people_stage_get_people_stage_element_response_statistics**](PeopleStageApi.md#people_stage_get_people_stage_element_response_statistics) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/ResponseStats | Returns statistics for the total number of responses received per channel for a particular PeopleStage element
[**people_stage_get_people_stage_element_status**](PeopleStageApi.md#people_stage_get_people_stage_element_status) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/Status | Returns the status for a PeopleStage element, where status information is available
[**people_stage_get_people_stage_element_status_for_descendants**](PeopleStageApi.md#people_stage_get_people_stage_element_status_for_descendants) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/Status/Descendants | Returns the status for all the descendant elements of a PeopleStage element where status information is available
[**people_stage_get_people_stage_elements**](PeopleStageApi.md#people_stage_get_people_stage_elements) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements | Returns the list of PeopleStage elements available in this FastStats system
[**people_stage_get_people_stage_range_statistics_for_descendants_sync**](PeopleStageApi.md#people_stage_get_people_stage_range_statistics_for_descendants_sync) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/RangeStats/Descendants/Sync | Returns some statistics for a given date range for a particular PeopleStage element.  This call may take a long time and will block until the information is available.
[**people_stage_get_people_stage_range_statistics_sync**](PeopleStageApi.md#people_stage_get_people_stage_range_statistics_sync) | **GET** /{dataViewName}/PeopleStage/{systemName}/Elements/{elementId}/RangeStats/Sync | Returns some statistics for a given date range for a particular PeopleStage element.  This call may take a long time and will block until the information is available.
[**people_stage_get_people_stage_system**](PeopleStageApi.md#people_stage_get_people_stage_system) | **GET** /{dataViewName}/PeopleStage/{systemName} | Returns details of the PeopleStage system for the given system name
[**people_stage_get_people_stage_systems**](PeopleStageApi.md#people_stage_get_people_stage_systems) | **GET** /{dataViewName}/PeopleStage | Returns the list of systems configured to support PeopleStage


# **people_stage_get_people_stage_channel**
> ChannelDetail people_stage_get_people_stage_channel(data_view_name, system_name, channel_id)

Returns the details of a particular PeopleStage channel

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
channel_id = 'channel_id_example' # str | The id of the PeopleStage channel to view

try:
    # Returns the details of a particular PeopleStage channel
    api_response = api_instance.people_stage_get_people_stage_channel(data_view_name, system_name, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **channel_id** | **str**| The id of the PeopleStage channel to view | 

### Return type

[**ChannelDetail**](ChannelDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PeopleStage channel details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this channel |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_channels**
> PagedResultsChannelSummary people_stage_get_people_stage_channels(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of PeopleStage channels available in this FastStats system

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Description, Type (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Description, Type (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of PeopleStage channels available in this FastStats system
    api_response = api_instance.people_stage_get_people_stage_channels(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Description, Type | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Description, Type | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsChannelSummary**](PagedResultsChannelSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of PeopleStage channels |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to access PeopleStage channels |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_element**
> ElementDetail people_stage_get_people_stage_element(data_view_name, system_name, element_id)

Returns the details of a particular PeopleStage element

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view

try:
    # Returns the details of a particular PeopleStage element
    api_response = api_instance.people_stage_get_people_stage_element(data_view_name, system_name, element_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 

### Return type

[**ElementDetail**](ElementDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PeopleStage element details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_element_channel_statistics**
> ChannelStatistics people_stage_get_people_stage_element_channel_statistics(data_view_name, system_name, element_id)

Returns statistics for the total number of communications sent per channel for a particular PeopleStage element

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view

try:
    # Returns statistics for the total number of communications sent per channel for a particular PeopleStage element
    api_response = api_instance.people_stage_get_people_stage_element_channel_statistics(data_view_name, system_name, element_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_element_channel_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 

### Return type

[**ChannelStatistics**](ChannelStatistics.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PeopleStage element channel statistics |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_element_children**
> PagedResultsElementSummary people_stage_get_people_stage_element_children(data_view_name, system_name, element_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of children for a particular PeopleStage element

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Description, Type (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Description, Type (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of children for a particular PeopleStage element
    api_response = api_instance.people_stage_get_people_stage_element_children(data_view_name, system_name, element_id, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_element_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Description, Type | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Description, Type | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsElementSummary**](PagedResultsElementSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of children for a particular PeopleStage element |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_element_communication_statistics**
> CommunicationStatistics people_stage_get_people_stage_element_communication_statistics(data_view_name, system_name, element_id)

Returns statistics for the number of communications sent over time for a particular PeopleStage element

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view

try:
    # Returns statistics for the number of communications sent over time for a particular PeopleStage element
    api_response = api_instance.people_stage_get_people_stage_element_communication_statistics(data_view_name, system_name, element_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_element_communication_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 

### Return type

[**CommunicationStatistics**](CommunicationStatistics.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PeopleStage element details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_element_response_statistics**
> ResponseStatistics people_stage_get_people_stage_element_response_statistics(data_view_name, system_name, element_id)

Returns statistics for the total number of responses received per channel for a particular PeopleStage element

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view

try:
    # Returns statistics for the total number of responses received per channel for a particular PeopleStage element
    api_response = api_instance.people_stage_get_people_stage_element_response_statistics(data_view_name, system_name, element_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_element_response_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 

### Return type

[**ResponseStatistics**](ResponseStatistics.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PeopleStage element response statistics |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_element_status**
> ElementStatus people_stage_get_people_stage_element_status(data_view_name, system_name, element_id)

Returns the status for a PeopleStage element, where status information is available

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view

try:
    # Returns the status for a PeopleStage element, where status information is available
    api_response = api_instance.people_stage_get_people_stage_element_status(data_view_name, system_name, element_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_element_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 

### Return type

[**ElementStatus**](ElementStatus.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PeopleStage element status information |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the status information for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_element_status_for_descendants**
> PagedResultsElementStatus people_stage_get_people_stage_element_status_for_descendants(data_view_name, system_name, element_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the status for all the descendant elements of a PeopleStage element where status information is available

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, Description, Type, SuccessfulCampaignsCount, ErroredCampaignsCount, InactiveCampaignsCount, NeedsApprovalCampaignsCount, TotalCommunicationsCount, TotalDeliveriesCount, TotalMessagesCount, TotalCampaignsCount, FirstRan, LastRan (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, Description, Type, SuccessfulCampaignsCount, ErroredCampaignsCount, InactiveCampaignsCount, NeedsApprovalCampaignsCount, TotalCommunicationsCount, TotalDeliveriesCount, TotalMessagesCount, TotalCampaignsCount, FirstRan, LastRan (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the status for all the descendant elements of a PeopleStage element where status information is available
    api_response = api_instance.people_stage_get_people_stage_element_status_for_descendants(data_view_name, system_name, element_id, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_element_status_for_descendants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, Description, Type, SuccessfulCampaignsCount, ErroredCampaignsCount, InactiveCampaignsCount, NeedsApprovalCampaignsCount, TotalCommunicationsCount, TotalDeliveriesCount, TotalMessagesCount, TotalCampaignsCount, FirstRan, LastRan | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, Description, Type, SuccessfulCampaignsCount, ErroredCampaignsCount, InactiveCampaignsCount, NeedsApprovalCampaignsCount, TotalCommunicationsCount, TotalDeliveriesCount, TotalMessagesCount, TotalCampaignsCount, FirstRan, LastRan | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsElementStatus**](PagedResultsElementStatus.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PeopleStage element status information |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the status information for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_elements**
> PagedResultsElementSummary people_stage_get_people_stage_elements(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of PeopleStage elements available in this FastStats system

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Description, Type (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Description, Type (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of PeopleStage elements available in this FastStats system
    api_response = api_instance.people_stage_get_people_stage_elements(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Description, Type | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Description, Type | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsElementSummary**](PagedResultsElementSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of PeopleStage elements |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to access PeopleStage elements |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_range_statistics_for_descendants_sync**
> RangeStatistics people_stage_get_people_stage_range_statistics_for_descendants_sync(data_view_name, system_name, element_id, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count, date_range=date_range)

Returns some statistics for a given date range for a particular PeopleStage element.  This call may take a long time and will block until the information is available.

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the PeopleStage service's configuration (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, CommunicationsCount, DeliveriesCount, MessagesCount, CampaignsCount, FirstRan, LastRan (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, CommunicationsCount, DeliveriesCount, MessagesCount, CampaignsCount, FirstRan, LastRan (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)
date_range = 'date_range_example' # str | Limit the date range of the returned data using a simple expression language.  The name of the field to use is Date (optional)

try:
    # Returns some statistics for a given date range for a particular PeopleStage element.  This call may take a long time and will block until the information is available.
    api_response = api_instance.people_stage_get_people_stage_range_statistics_for_descendants_sync(data_view_name, system_name, element_id, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count, date_range=date_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_range_statistics_for_descendants_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the PeopleStage service&#39;s configuration | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, CommunicationsCount, DeliveriesCount, MessagesCount, CampaignsCount, FirstRan, LastRan | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, CommunicationsCount, DeliveriesCount, MessagesCount, CampaignsCount, FirstRan, LastRan | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 
 **date_range** | **str**| Limit the date range of the returned data using a simple expression language.  The name of the field to use is Date | [optional] 

### Return type

[**RangeStatistics**](RangeStatistics.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Range statistics for the given PeopleStage element |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the range statistics for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_range_statistics_sync**
> RangeStatistics people_stage_get_people_stage_range_statistics_sync(data_view_name, system_name, element_id, timeout_in_seconds=timeout_in_seconds, date_range=date_range)

Returns some statistics for a given date range for a particular PeopleStage element.  This call may take a long time and will block until the information is available.

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
element_id = 'element_id_example' # str | The id of the PeopleStage element to view
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the PeopleStage service's configuration (optional)
date_range = 'date_range_example' # str | Limit the date range of the returned data using a simple expression language.  The name of the field to use is Date (optional)

try:
    # Returns some statistics for a given date range for a particular PeopleStage element.  This call may take a long time and will block until the information is available.
    api_response = api_instance.people_stage_get_people_stage_range_statistics_sync(data_view_name, system_name, element_id, timeout_in_seconds=timeout_in_seconds, date_range=date_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_range_statistics_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **element_id** | **str**| The id of the PeopleStage element to view | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the PeopleStage service&#39;s configuration | [optional] 
 **date_range** | **str**| Limit the date range of the returned data using a simple expression language.  The name of the field to use is Date | [optional] 

### Return type

[**RangeStatistics**](RangeStatistics.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Range statistics for the given PeopleStage element |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the range statistics for this element |  -  |
**404** | The element or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_system**
> PeopleStageSystemDetail people_stage_get_people_stage_system(data_view_name, system_name)

Returns details of the PeopleStage system for the given system name

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on

try:
    # Returns details of the PeopleStage system for the given system name
    api_response = api_instance.people_stage_get_people_stage_system(data_view_name, system_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 

### Return type

[**PeopleStageSystemDetail**](PeopleStageSystemDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the PeopleStage system |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the information for the given system |  -  |
**404** | The DataView or system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_stage_get_people_stage_systems**
> PagedResultsPeopleStageSystemSummary people_stage_get_people_stage_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of systems configured to support PeopleStage

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
api_instance = apteco_api.PeopleStageApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are SystemName, ProgrammeDescription (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are SystemName, ProgrammeDescription (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of systems configured to support PeopleStage
    api_response = api_instance.people_stage_get_people_stage_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleStageApi->people_stage_get_people_stage_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are SystemName, ProgrammeDescription | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are SystemName, ProgrammeDescription | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsPeopleStageSystemSummary**](PagedResultsPeopleStageSystemSummary.md)

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

