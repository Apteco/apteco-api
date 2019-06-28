# apteco_api.StaticResourcesApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**static_resources_get_static_resource_categories**](StaticResourcesApi.md#static_resources_get_static_resource_categories) | **GET** /{dataViewName}/StaticResources | Requires OrbitAdmin: Returns a list of categories of resource files for the given system
[**static_resources_get_static_resource_category**](StaticResourcesApi.md#static_resources_get_static_resource_category) | **GET** /{dataViewName}/StaticResources/{resourceCategory} | Requires OrbitAdmin: Returns details of a resource category for a given category name and system
[**static_resources_get_static_resource_file**](StaticResourcesApi.md#static_resources_get_static_resource_file) | **GET** /{dataViewName}/StaticResources/{resourceCategory}/Resources/{resourceName} | Returns a resource file (such as an image file) for the given category and system
[**static_resources_get_static_resource_file_details**](StaticResourcesApi.md#static_resources_get_static_resource_file_details) | **GET** /{dataViewName}/StaticResources/{resourceCategory}/Resources/{resourceName}/Details | Requires OrbitAdmin: Returns the details of a resource file (such as an image file) for the given category and system
[**static_resources_get_static_resources_for_category**](StaticResourcesApi.md#static_resources_get_static_resources_for_category) | **GET** /{dataViewName}/StaticResources/{resourceCategory}/Resources | Requires OrbitAdmin: Returns a list of details for the resource files (such as image files) in the given resource category and system


# **static_resources_get_static_resource_categories**
> PagedResultsResourceCategorySummary static_resources_get_static_resource_categories(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns a list of categories of resource files for the given system

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
api_instance = apteco_api.StaticResourcesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to list resource categories for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Description (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Description (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Returns a list of categories of resource files for the given system
    api_response = api_instance.static_resources_get_static_resource_categories(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticResourcesApi->static_resources_get_static_resource_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to list resource categories for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Description | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Description | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsResourceCategorySummary**](PagedResultsResourceCategorySummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource categories |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_resources_get_static_resource_category**
> ResourceCategoryDetails static_resources_get_static_resource_category(data_view_name, resource_category)

Requires OrbitAdmin: Returns details of a resource category for a given category name and system

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
api_instance = apteco_api.StaticResourcesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to list resources
resource_category = 'resource_category_example' # str | The category to return the details for

try:
    # Requires OrbitAdmin: Returns details of a resource category for a given category name and system
    api_response = api_instance.static_resources_get_static_resource_category(data_view_name, resource_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticResourcesApi->static_resources_get_static_resource_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to list resources | 
 **resource_category** | **str**| The category to return the details for | 

### Return type

[**ResourceCategoryDetails**](ResourceCategoryDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the resource category |  -  |
**400** | A bad request |  -  |
**404** | The DataView or category couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_resources_get_static_resource_file**
> static_resources_get_static_resource_file(data_view_name, resource_category, resource_name)

Returns a resource file (such as an image file) for the given category and system

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.StaticResourcesApi()
data_view_name = 'data_view_name_example' # str | The name of the DataView to find the resource for
resource_category = 'resource_category_example' # str | The category of the resource to return
resource_name = 'resource_name_example' # str | The name of the resource to return

try:
    # Returns a resource file (such as an image file) for the given category and system
    api_instance.static_resources_get_static_resource_file(data_view_name, resource_category, resource_name)
except ApiException as e:
    print("Exception when calling StaticResourcesApi->static_resources_get_static_resource_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to find the resource for | 
 **resource_category** | **str**| The category of the resource to return | 
 **resource_name** | **str**| The name of the resource to return | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource file |  -  |
**400** | A bad request |  -  |
**404** | The DataView, category or resource couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_resources_get_static_resource_file_details**
> ResourceDetails static_resources_get_static_resource_file_details(data_view_name, resource_category, resource_name)

Requires OrbitAdmin: Returns the details of a resource file (such as an image file) for the given category and system

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
api_instance = apteco_api.StaticResourcesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to find the resource for
resource_category = 'resource_category_example' # str | The category of the resource to return
resource_name = 'resource_name_example' # str | The name of the resource to return

try:
    # Requires OrbitAdmin: Returns the details of a resource file (such as an image file) for the given category and system
    api_response = api_instance.static_resources_get_static_resource_file_details(data_view_name, resource_category, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticResourcesApi->static_resources_get_static_resource_file_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to find the resource for | 
 **resource_category** | **str**| The category of the resource to return | 
 **resource_name** | **str**| The name of the resource to return | 

### Return type

[**ResourceDetails**](ResourceDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of a resource file |  -  |
**400** | A bad request |  -  |
**404** | The DataView, category or resource couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_resources_get_static_resources_for_category**
> PagedResultsResourceSummary static_resources_get_static_resources_for_category(data_view_name, resource_category, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns a list of details for the resource files (such as image files) in the given resource category and system

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
api_instance = apteco_api.StaticResourcesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to list resources
resource_category = 'resource_category_example' # str | The category to return resources for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Size, LastModified (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Size, LastModified (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Returns a list of details for the resource files (such as image files) in the given resource category and system
    api_response = api_instance.static_resources_get_static_resources_for_category(data_view_name, resource_category, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticResourcesApi->static_resources_get_static_resources_for_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to list resources | 
 **resource_category** | **str**| The category to return resources for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Size, LastModified | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Size, LastModified | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsResourceSummary**](PagedResultsResourceSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource files |  -  |
**400** | A bad request |  -  |
**404** | The DataView or category couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

