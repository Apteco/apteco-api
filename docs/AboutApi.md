# apteco_api.AboutApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**about_example_experimental_resource**](AboutApi.md#about_example_experimental_resource) | **GET** /About/ExampleExperimentalResource | EXPERIMENTAL: Returns a sample string if experimental endpoints are enabled
[**about_force_process_garbage_collection**](AboutApi.md#about_force_process_garbage_collection) | **POST** /About/Process/ForceGarbageCollection | Requires OrbitAdmin: Forces a garbage collection in the API&#39;s process and then returns details about the API&#39;s .Net process
[**about_get_data_view**](AboutApi.md#about_get_data_view) | **GET** /About/DataViews/{dataViewName} | Get details for a particular DataView.
[**about_get_data_views**](AboutApi.md#about_get_data_views) | **GET** /About/DataViews | Get the list of DataViews that are available.
[**about_get_data_views_for_domain**](AboutApi.md#about_get_data_views_for_domain) | **GET** /About/DataViews/Domains/{domain} | Get the list of DataViews that are available to users with the specified email domain.
[**about_get_data_views_for_system_name**](AboutApi.md#about_get_data_views_for_system_name) | **GET** /About/DataViews/Systems/{systemName} | Get the list of DataViews that are configured with the given FastStats system.
[**about_get_endpoints**](AboutApi.md#about_get_endpoints) | **GET** /About/Endpoints | Returns details of all the endpoints in the API
[**about_get_language_details**](AboutApi.md#about_get_language_details) | **GET** /About/Language | Returns information about the current language the API is operating in (based on details in the request)
[**about_get_orbit_settings**](AboutApi.md#about_get_orbit_settings) | **GET** /About/Orbit/Settings/{settingsPath} | Gets Orbit settings at the given path
[**about_get_orbit_settings_root**](AboutApi.md#about_get_orbit_settings_root) | **GET** /About/Orbit/Settings | Gets the complete Orbit settings object
[**about_get_process_details**](AboutApi.md#about_get_process_details) | **GET** /About/Process | Requires OrbitAdmin: Returns details about the API&#39;s .Net process
[**about_get_version**](AboutApi.md#about_get_version) | **GET** /About/Version | Returns version information about the API


# **about_example_experimental_resource**
> Message about_example_experimental_resource()

EXPERIMENTAL: Returns a sample string if experimental endpoints are enabled

EXPERIMENTAL

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()

try:
    # EXPERIMENTAL: Returns a sample string if experimental endpoints are enabled
    api_response = api_instance.about_example_experimental_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_example_experimental_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A sample message |  -  |
**500** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_force_process_garbage_collection**
> ProcessDetails about_force_process_garbage_collection()

Requires OrbitAdmin: Forces a garbage collection in the API's process and then returns details about the API's .Net process

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
api_instance = apteco_api.AboutApi(apteco_api.ApiClient(configuration))

try:
    # Requires OrbitAdmin: Forces a garbage collection in the API's process and then returns details about the API's .Net process
    api_response = api_instance.about_force_process_garbage_collection()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_force_process_garbage_collection: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessDetails**](ProcessDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The valid process information |  -  |
**403** | The user isn&#39;t an admin user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_data_view**
> DataViewDetails about_get_data_view(data_view_name)

Get details for a particular DataView.

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
api_instance = apteco_api.AboutApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on

try:
    # Get details for a particular DataView.
    api_response = api_instance.about_get_data_view(data_view_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_data_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 

### Return type

[**DataViewDetails**](DataViewDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the DataView |  -  |
**400** | The specified DataView is not the one you are currently logged in to and you are not an admin user |  -  |
**403** | Forbidden |  -  |
**404** | The specified DataView can&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_data_views**
> PagedResultsDataViewSummary about_get_data_views(filter=filter, order_by=order_by, offset=offset, count=count)

Get the list of DataViews that are available.

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Get the list of DataViews that are available.
    api_response = api_instance.about_get_data_views(filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_data_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsDataViewSummary**](PagedResultsDataViewSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of DataViews |  -  |
**400** | The API has been configured not to return DataViews |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_data_views_for_domain**
> PagedResultsDataViewSummary about_get_data_views_for_domain(domain, filter=filter, order_by=order_by, offset=offset, count=count)

Get the list of DataViews that are available to users with the specified email domain.

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()
domain = 'domain_example' # str | The email domain to list DataViews for (i.e. \"example.com\")
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Get the list of DataViews that are available to users with the specified email domain.
    api_response = api_instance.about_get_data_views_for_domain(domain, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_data_views_for_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The email domain to list DataViews for (i.e. \&quot;example.com\&quot;) | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsDataViewSummary**](PagedResultsDataViewSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of DataViews |  -  |
**400** | The API has been configured not to return DataViews |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_data_views_for_system_name**
> PagedResultsDataViewSummary about_get_data_views_for_system_name(system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Get the list of DataViews that are configured with the given FastStats system.

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()
system_name = 'system_name_example' # str | The name of the system to list DataViews for (i.e. \"holidays\")
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Get the list of DataViews that are configured with the given FastStats system.
    api_response = api_instance.about_get_data_views_for_system_name(system_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_data_views_for_system_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_name** | **str**| The name of the system to list DataViews for (i.e. \&quot;holidays\&quot;) | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsDataViewSummary**](PagedResultsDataViewSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of DataViews |  -  |
**400** | The API has been configured not to return DataViews |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_endpoints**
> PagedResultsEndpointDetails about_get_endpoints(exclude_endpoints_with_no_licence_requirements=exclude_endpoints_with_no_licence_requirements, exclude_endpoints_with_no_role_requirements=exclude_endpoints_with_no_role_requirements, filter=filter, order_by=order_by, offset=offset, count=count)

Returns details of all the endpoints in the API

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()
exclude_endpoints_with_no_licence_requirements = True # bool | If specified, don't return endpoints in the output that have no licence requirements.  Defaults to false - returns all endpoints (optional)
exclude_endpoints_with_no_role_requirements = True # bool | If specified, don't return endpoints in the output that have no role requirements.  Defaults to false - returns all endpoints (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, GroupName, Method, UrlTemplate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, GroupName, Method, UrlTemplate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns details of all the endpoints in the API
    api_response = api_instance.about_get_endpoints(exclude_endpoints_with_no_licence_requirements=exclude_endpoints_with_no_licence_requirements, exclude_endpoints_with_no_role_requirements=exclude_endpoints_with_no_role_requirements, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_endpoints_with_no_licence_requirements** | **bool**| If specified, don&#39;t return endpoints in the output that have no licence requirements.  Defaults to false - returns all endpoints | [optional] 
 **exclude_endpoints_with_no_role_requirements** | **bool**| If specified, don&#39;t return endpoints in the output that have no role requirements.  Defaults to false - returns all endpoints | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, GroupName, Method, UrlTemplate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, GroupName, Method, UrlTemplate | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsEndpointDetails**](PagedResultsEndpointDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of all the endpoints in the API |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_language_details**
> LanguageDetails about_get_language_details()

Returns information about the current language the API is operating in (based on details in the request)

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()

try:
    # Returns information about the current language the API is operating in (based on details in the request)
    api_response = api_instance.about_get_language_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_language_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LanguageDetails**](LanguageDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The valid language information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_orbit_settings**
> object about_get_orbit_settings(settings_path)

Gets Orbit settings at the given path

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()
settings_path = 'settings_path_example' # str | The path of the settings

try:
    # Gets Orbit settings at the given path
    api_response = api_instance.about_get_orbit_settings(settings_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_orbit_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_path** | **str**| The path of the settings | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contents of the Orbit settings |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the Orbit settings |  -  |
**404** | The Orbit settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_orbit_settings_root**
> object about_get_orbit_settings_root()

Gets the complete Orbit settings object

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()

try:
    # Gets the complete Orbit settings object
    api_response = api_instance.about_get_orbit_settings_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_orbit_settings_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contents of the Orbit settings |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the Orbit settings |  -  |
**404** | The Orbit settings couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_process_details**
> ProcessDetails about_get_process_details()

Requires OrbitAdmin: Returns details about the API's .Net process

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
api_instance = apteco_api.AboutApi(apteco_api.ApiClient(configuration))

try:
    # Requires OrbitAdmin: Returns details about the API's .Net process
    api_response = api_instance.about_get_process_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_process_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessDetails**](ProcessDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The valid process information |  -  |
**403** | The user isn&#39;t an admin user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_get_version**
> VersionDetails about_get_version()

Returns version information about the API

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.AboutApi()

try:
    # Returns version information about the API
    api_response = api_instance.about_get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about_get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionDetails**](VersionDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The valid version information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

