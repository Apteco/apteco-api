# apteco_api.AudienceCompositionsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_compositions_create_audience_composition**](AudienceCompositionsApi.md#audience_compositions_create_audience_composition) | **POST** /{dataViewName}/AudienceCompositions/{systemName} | Requires OrbitAdmin: Create an audience composition for the given FastStats system.
[**audience_compositions_delete_audience_composition**](AudienceCompositionsApi.md#audience_compositions_delete_audience_composition) | **DELETE** /{dataViewName}/AudienceCompositions/{systemName}/{audienceCompositionId} | Requires OrbitAdmin: Deletes a given audience composition for the given FastStats system.
[**audience_compositions_get_audience_composition**](AudienceCompositionsApi.md#audience_compositions_get_audience_composition) | **GET** /{dataViewName}/AudienceCompositions/{systemName}/{audienceCompositionId} | Returns details for a given audience composition
[**audience_compositions_get_audience_compositions**](AudienceCompositionsApi.md#audience_compositions_get_audience_compositions) | **GET** /{dataViewName}/AudienceCompositions | Returns all the avaiable audience compositions.
[**audience_compositions_get_audience_compositions_for_system**](AudienceCompositionsApi.md#audience_compositions_get_audience_compositions_for_system) | **GET** /{dataViewName}/AudienceCompositions/{systemName} | Returns all the avaiable audience compositions for the given FastStats system
[**audience_compositions_update_audience_composition**](AudienceCompositionsApi.md#audience_compositions_update_audience_composition) | **PUT** /{dataViewName}/AudienceCompositions/{systemName}/{audienceCompositionId} | Requires OrbitAdmin: Update a given audience composition for the given FastStats system.


# **audience_compositions_create_audience_composition**
> audience_compositions_create_audience_composition(data_view_name, system_name, create_audience_composition_detail=create_audience_composition_detail)

Requires OrbitAdmin: Create an audience composition for the given FastStats system.

This endpoint is only available for users with the OrbitAdmin role

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudienceCompositionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to create the composition for
create_audience_composition_detail = apteco_api.CreateAudienceCompositionDetail() # CreateAudienceCompositionDetail | Details to create the audience composition with (optional)

    try:
        # Requires OrbitAdmin: Create an audience composition for the given FastStats system.
        api_instance.audience_compositions_create_audience_composition(data_view_name, system_name, create_audience_composition_detail=create_audience_composition_detail)
    except ApiException as e:
        print("Exception when calling AudienceCompositionsApi->audience_compositions_create_audience_composition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to create the composition for | 
 **create_audience_composition_detail** | [**CreateAudienceCompositionDetail**](CreateAudienceCompositionDetail.md)| Details to create the audience composition with | [optional] 

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
**200** | The details of the created audience composition |  -  |
**201** | Success |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audience_compositions_delete_audience_composition**
> audience_compositions_delete_audience_composition(data_view_name, system_name, audience_composition_id)

Requires OrbitAdmin: Deletes a given audience composition for the given FastStats system.

This endpoint is only available for users with the OrbitAdmin role

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudienceCompositionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to delete the composition for
audience_composition_id = 56 # int | The id of the audience composition

    try:
        # Requires OrbitAdmin: Deletes a given audience composition for the given FastStats system.
        api_instance.audience_compositions_delete_audience_composition(data_view_name, system_name, audience_composition_id)
    except ApiException as e:
        print("Exception when calling AudienceCompositionsApi->audience_compositions_delete_audience_composition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to delete the composition for | 
 **audience_composition_id** | **int**| The id of the audience composition | 

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
**204** | The composition was deleted successfully |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audience_compositions_get_audience_composition**
> CompositionDetail audience_compositions_get_audience_composition(data_view_name, system_name, audience_composition_id)

Returns details for a given audience composition

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudienceCompositionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to get the composition for
audience_composition_id = 56 # int | The id of the audience composition

    try:
        # Returns details for a given audience composition
        api_response = api_instance.audience_compositions_get_audience_composition(data_view_name, system_name, audience_composition_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudienceCompositionsApi->audience_compositions_get_audience_composition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to get the composition for | 
 **audience_composition_id** | **int**| The id of the audience composition | 

### Return type

[**CompositionDetail**](CompositionDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the given audience composition |  -  |
**400** | Bad request |  -  |
**404** | The DataView or audience composition couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audience_compositions_get_audience_compositions**
> PagedResultsCompositionSummary audience_compositions_get_audience_compositions(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns all the avaiable audience compositions.

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudienceCompositionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Description, Type, SystemName (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Description, Type, SystemName (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns all the avaiable audience compositions.
        api_response = api_instance.audience_compositions_get_audience_compositions(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudienceCompositionsApi->audience_compositions_get_audience_compositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Description, Type, SystemName | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Description, Type, SystemName | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsCompositionSummary**](PagedResultsCompositionSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all audience compositions |  -  |
**400** | Bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audience_compositions_get_audience_compositions_for_system**
> PagedResultsCompositionSummary audience_compositions_get_audience_compositions_for_system(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns all the avaiable audience compositions for the given FastStats system

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudienceCompositionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to get compositions for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Description, Type, SystemName (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Description, Type, SystemName (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns all the avaiable audience compositions for the given FastStats system
        api_response = api_instance.audience_compositions_get_audience_compositions_for_system(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudienceCompositionsApi->audience_compositions_get_audience_compositions_for_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to get compositions for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Description, Type, SystemName | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Description, Type, SystemName | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsCompositionSummary**](PagedResultsCompositionSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all audience compositions |  -  |
**400** | Bad request |  -  |
**404** | The DataView or system couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audience_compositions_update_audience_composition**
> audience_compositions_update_audience_composition(data_view_name, system_name, audience_composition_id, create_audience_composition_detail=create_audience_composition_detail)

Requires OrbitAdmin: Update a given audience composition for the given FastStats system.

This endpoint is only available for users with the OrbitAdmin role

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
configuration = apteco_api.Configuration(
    host = "https://example.com/OrbitAPI",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudienceCompositionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to update the composition for
audience_composition_id = 56 # int | The id of the audience composition
create_audience_composition_detail = apteco_api.CreateAudienceCompositionDetail() # CreateAudienceCompositionDetail | Details to create the audience composition with (optional)

    try:
        # Requires OrbitAdmin: Update a given audience composition for the given FastStats system.
        api_instance.audience_compositions_update_audience_composition(data_view_name, system_name, audience_composition_id, create_audience_composition_detail=create_audience_composition_detail)
    except ApiException as e:
        print("Exception when calling AudienceCompositionsApi->audience_compositions_update_audience_composition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to update the composition for | 
 **audience_composition_id** | **int**| The id of the audience composition | 
 **create_audience_composition_detail** | [**CreateAudienceCompositionDetail**](CreateAudienceCompositionDetail.md)| Details to create the audience composition with | [optional] 

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
**200** | The details of the created audience composition |  -  |
**201** | Success |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

