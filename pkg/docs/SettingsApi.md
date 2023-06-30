# apteco_api.SettingsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_delete_data_view_settings**](SettingsApi.md#settings_delete_data_view_settings) | **DELETE** /{dataViewName}/Settings/DataView/{settingsPath} | Deletes DataView settings at the given path
[**settings_delete_data_view_settings_root**](SettingsApi.md#settings_delete_data_view_settings_root) | **DELETE** /{dataViewName}/Settings/DataView | Deletes the complete DataView settings
[**settings_get_data_view_settings**](SettingsApi.md#settings_get_data_view_settings) | **GET** /{dataViewName}/Settings/DataView/{settingsPath} | Gets DataView settings at the given path
[**settings_get_data_view_settings_root**](SettingsApi.md#settings_get_data_view_settings_root) | **GET** /{dataViewName}/Settings/DataView | Gets the complete DataView settings object
[**settings_update_data_view_settings**](SettingsApi.md#settings_update_data_view_settings) | **PUT** /{dataViewName}/Settings/DataView/{settingsPath} | Updates DataView settings at the given path
[**settings_update_data_view_settings_root**](SettingsApi.md#settings_update_data_view_settings_root) | **PUT** /{dataViewName}/Settings/DataView | Updates the complete DataView settings


# **settings_delete_data_view_settings**
> settings_delete_data_view_settings(data_view_name, settings_path)

Deletes DataView settings at the given path

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
    api_instance = apteco_api.SettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
settings_path = 'settings_path_example' # str | The path of the DataView settings

    try:
        # Deletes DataView settings at the given path
        api_instance.settings_delete_data_view_settings(data_view_name, settings_path)
    except ApiException as e:
        print("Exception when calling SettingsApi->settings_delete_data_view_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **settings_path** | **str**| The path of the DataView settings | 

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
**200** | The DataView settings were deleted |  -  |
**204** | Success |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete the contents of the given DataView settings |  -  |
**404** | The DataView settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_delete_data_view_settings_root**
> settings_delete_data_view_settings_root(data_view_name)

Deletes the complete DataView settings

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
    api_instance = apteco_api.SettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on

    try:
        # Deletes the complete DataView settings
        api_instance.settings_delete_data_view_settings_root(data_view_name)
    except ApiException as e:
        print("Exception when calling SettingsApi->settings_delete_data_view_settings_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 

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
**200** | The DataView settings were deleted |  -  |
**204** | Success |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete the contents of the given DataView settings |  -  |
**404** | The DataView settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_get_data_view_settings**
> object settings_get_data_view_settings(data_view_name, settings_path)

Gets DataView settings at the given path

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
    api_instance = apteco_api.SettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
settings_path = 'settings_path_example' # str | The path of the settings

    try:
        # Gets DataView settings at the given path
        api_response = api_instance.settings_get_data_view_settings(data_view_name, settings_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->settings_get_data_view_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **settings_path** | **str**| The path of the settings | 

### Return type

**object**

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contents of the DataView settings |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the DataView settings |  -  |
**404** | The DataView settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_get_data_view_settings_root**
> object settings_get_data_view_settings_root(data_view_name)

Gets the complete DataView settings object

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
    api_instance = apteco_api.SettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on

    try:
        # Gets the complete DataView settings object
        api_response = api_instance.settings_get_data_view_settings_root(data_view_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->settings_get_data_view_settings_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 

### Return type

**object**

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contents of the DataView settings |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the DataView settings |  -  |
**404** | The DataView settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_update_data_view_settings**
> object settings_update_data_view_settings(data_view_name, settings_path, settings=settings)

Updates DataView settings at the given path

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
    api_instance = apteco_api.SettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
settings_path = 'settings_path_example' # str | The path of the DataView settings
settings = None # object | The contents of the DataView settings (optional)

    try:
        # Updates DataView settings at the given path
        api_response = api_instance.settings_update_data_view_settings(data_view_name, settings_path, settings=settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->settings_update_data_view_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **settings_path** | **str**| The path of the DataView settings | 
 **settings** | **object**| The contents of the DataView settings | [optional] 

### Return type

**object**

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Details of the created DataView settings |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given DataView settings |  -  |
**404** | The DataView settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_update_data_view_settings_root**
> object settings_update_data_view_settings_root(data_view_name, settings=settings)

Updates the complete DataView settings

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
    api_instance = apteco_api.SettingsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
settings = None # object | The contents of the DataView settings (optional)

    try:
        # Updates the complete DataView settings
        api_response = api_instance.settings_update_data_view_settings_root(data_view_name, settings=settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->settings_update_data_view_settings_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **settings** | **object**| The contents of the DataView settings | [optional] 

### Return type

**object**

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Details of the created DataView settings |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given DataView settings |  -  |
**404** | The DataView settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

