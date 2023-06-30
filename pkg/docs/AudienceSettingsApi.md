# apteco_api.AudienceSettingsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_settings_get_audience_settings_for_system**](AudienceSettingsApi.md#audience_settings_get_audience_settings_for_system) | **GET** /{dataViewName}/AudienceSettings/{systemName} | SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level settings for the specified FastStats system available for use with audiences
[**audience_settings_get_audience_settings_for_systems**](AudienceSettingsApi.md#audience_settings_get_audience_settings_for_systems) | **GET** /{dataViewName}/AudienceSettings | SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for using audiences


# **audience_settings_get_audience_settings_for_system**
> AudienceSettingsDetail audience_settings_get_audience_settings_for_system(data_view_name, system_name)

SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level settings for the specified FastStats system available for use with audiences

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
    api_instance = apteco_api.AudienceSettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to return details for

    try:
        # SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level settings for the specified FastStats system available for use with audiences
        api_response = api_instance.audience_settings_get_audience_settings_for_system(data_view_name, system_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudienceSettingsApi->audience_settings_get_audience_settings_for_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to return details for | 

### Return type

[**AudienceSettingsDetail**](AudienceSettingsDetail.md)

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

# **audience_settings_get_audience_settings_for_systems**
> PagedResultsAudienceSettingsSummary audience_settings_get_audience_settings_for_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for using audiences

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
    api_instance = apteco_api.AudienceSettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are SystemName. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are SystemName. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for using audiences
        api_response = api_instance.audience_settings_get_audience_settings_for_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudienceSettingsApi->audience_settings_get_audience_settings_for_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are SystemName. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are SystemName. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAudienceSettingsSummary**](PagedResultsAudienceSettingsSummary.md)

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

