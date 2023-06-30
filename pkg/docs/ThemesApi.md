# apteco_api.ThemesApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themes_create_theme**](ThemesApi.md#themes_create_theme) | **POST** /{dataViewName}/Themes | Requires OrbitAdmin: Creates a new theme from the given details for the logged in user.
[**themes_delete_theme**](ThemesApi.md#themes_delete_theme) | **DELETE** /{dataViewName}/Themes/{themeId} | Requires OrbitAdmin: Deletes the specified theme
[**themes_get_theme**](ThemesApi.md#themes_get_theme) | **GET** /{dataViewName}/Themes/{themeId} | Returns a theme for this dataview
[**themes_get_themes**](ThemesApi.md#themes_get_themes) | **GET** /{dataViewName}/Themes | Returns a list of all themes for this dataview
[**themes_get_usage**](ThemesApi.md#themes_get_usage) | **GET** /{dataViewName}/Themes/Usage | Requires OrbitAdmin: Returns a list of all themes with associated usage information
[**themes_update_theme**](ThemesApi.md#themes_update_theme) | **POST** /{dataViewName}/Themes/{themeId}/Updates | Requires OrbitAdmin: Updates the details of a particular theme.  If you don&#39;t have an id for the  theme then POST to the /Themes URL to create a new theme.


# **themes_create_theme**
> Theme themes_create_theme(data_view_name, theme_detail=theme_detail)

Requires OrbitAdmin: Creates a new theme from the given details for the logged in user.

This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.ThemesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
theme_detail = apteco_api.CreateUpdateTheme() # CreateUpdateTheme | The details for the theme to create.  If you want              to update a specific theme then POST to the /Theme/{themeId} URL (optional)

    try:
        # Requires OrbitAdmin: Creates a new theme from the given details for the logged in user.
        api_response = api_instance.themes_create_theme(data_view_name, theme_detail=theme_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThemesApi->themes_create_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **theme_detail** | [**CreateUpdateTheme**](CreateUpdateTheme.md)| The details for the theme to create.  If you want              to update a specific theme then POST to the /Theme/{themeId} URL | [optional] 

### Return type

[**Theme**](Theme.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The theme was created successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **themes_delete_theme**
> themes_delete_theme(data_view_name, theme_id)

Requires OrbitAdmin: Deletes the specified theme

This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.ThemesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
theme_id = 56 # int | The id of the theme to delete

    try:
        # Requires OrbitAdmin: Deletes the specified theme
        api_instance.themes_delete_theme(data_view_name, theme_id)
    except ApiException as e:
        print("Exception when calling ThemesApi->themes_delete_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **theme_id** | **int**| The id of the theme to delete | 

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
**204** | The theme was deleted successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete this theme. Only admins can delete custom themes |  -  |
**404** | The DataView or theme couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **themes_get_theme**
> Theme themes_get_theme(data_view_name, theme_id)

Returns a theme for this dataview

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
    api_instance = apteco_api.ThemesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
theme_id = 56 # int | The themeId of the Theme to retrieve

    try:
        # Returns a theme for this dataview
        api_response = api_instance.themes_get_theme(data_view_name, theme_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThemesApi->themes_get_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **theme_id** | **int**| The themeId of the Theme to retrieve | 

### Return type

[**Theme**](Theme.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved theme |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found or no theme found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **themes_get_themes**
> list[Theme] themes_get_themes(data_view_name)

Returns a list of all themes for this dataview

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
    api_instance = apteco_api.ThemesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on

    try:
        # Returns a list of all themes for this dataview
        api_response = api_instance.themes_get_themes(data_view_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThemesApi->themes_get_themes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 

### Return type

[**list[Theme]**](Theme.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved themes |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found or no themes found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **themes_get_usage**
> ThemeUsage themes_get_usage(data_view_name)

Requires OrbitAdmin: Returns a list of all themes with associated usage information

This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.ThemesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on

    try:
        # Requires OrbitAdmin: Returns a list of all themes with associated usage information
        api_response = api_instance.themes_get_usage(data_view_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThemesApi->themes_get_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 

### Return type

[**ThemeUsage**](ThemeUsage.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved themes usage |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found or no themes found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **themes_update_theme**
> Theme themes_update_theme(data_view_name, theme_id, theme_detail=theme_detail)

Requires OrbitAdmin: Updates the details of a particular theme.  If you don't have an id for the  theme then POST to the /Themes URL to create a new theme.

This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.ThemesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
theme_id = 56 # int | The id of the theme to add/update
theme_detail = apteco_api.CreateUpdateTheme() # CreateUpdateTheme | The details for the theme to update (optional)

    try:
        # Requires OrbitAdmin: Updates the details of a particular theme.  If you don't have an id for the  theme then POST to the /Themes URL to create a new theme.
        api_response = api_instance.themes_update_theme(data_view_name, theme_id, theme_detail=theme_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThemesApi->themes_update_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **theme_id** | **int**| The id of the theme to add/update | 
 **theme_detail** | [**CreateUpdateTheme**](CreateUpdateTheme.md)| The details for the theme to update | [optional] 

### Return type

[**Theme**](Theme.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The theme details were added/updated successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to update the details for this theme.  Only admins can modify themes |  -  |
**404** | The DataView or theme couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

