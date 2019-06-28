# apteco_api.DirectoriesApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directories_delete_directory**](DirectoriesApi.md#directories_delete_directory) | **DELETE** /{dataViewName}/Directories/{systemName}/{directoryPath} | Deletes directory at location
[**directories_get_file_entries**](DirectoriesApi.md#directories_get_file_entries) | **GET** /{dataViewName}/Directories/{systemName}/{directoryPath} | Returns the list of files and subdirectories under the given directory
[**directories_get_file_systems**](DirectoriesApi.md#directories_get_file_systems) | **GET** /{dataViewName}/Directories | Returns the list of systems that have access to a filesystem
[**directories_get_root_file_entries**](DirectoriesApi.md#directories_get_root_file_entries) | **GET** /{dataViewName}/Directories/{systemName} | Returns the list of root directories configured in this FastStats system
[**directories_upsert_directory**](DirectoriesApi.md#directories_upsert_directory) | **PUT** /{dataViewName}/Directories/{systemName}/{directoryPath} | Ensure that a directory exists in a location


# **directories_delete_directory**
> directories_delete_directory(data_view_name, system_name, directory_path, timeout_in_seconds=timeout_in_seconds)

Deletes directory at location

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
api_instance = apteco_api.DirectoriesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
directory_path = 'directory_path_example' # str | The path to the directory to be deleted
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)

try:
    # Deletes directory at location
    api_instance.directories_delete_directory(data_view_name, system_name, directory_path, timeout_in_seconds=timeout_in_seconds)
except ApiException as e:
    print("Exception when calling DirectoriesApi->directories_delete_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **directory_path** | **str**| The path to the directory to be deleted | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service&#39;s configuration | [optional] 

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
**200** | The directory was deleted |  -  |
**204** | Success |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file/directory |  -  |
**404** | The system name or specified directory/file couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directories_get_file_entries**
> PagedResultsFileEntry directories_get_file_entries(data_view_name, system_name, directory_path, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of files and subdirectories under the given directory

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
api_instance = apteco_api.DirectoriesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
directory_path = 'directory_path_example' # str | The path of the directory to list the contents of
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Type (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Type (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of files and subdirectories under the given directory
    api_response = api_instance.directories_get_file_entries(data_view_name, system_name, directory_path, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoriesApi->directories_get_file_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **directory_path** | **str**| The path of the directory to list the contents of | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service&#39;s configuration | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Type | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Type | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsFileEntry**](PagedResultsFileEntry.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of files and subdirectories under the given directory |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given directory |  -  |
**404** | The system name or specified directory couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directories_get_file_systems**
> PagedResultsFileSystemSummary directories_get_file_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of systems that have access to a filesystem

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
api_instance = apteco_api.DirectoriesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are SystemName (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are SystemName (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of systems that have access to a filesystem
    api_response = api_instance.directories_get_file_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoriesApi->directories_get_file_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are SystemName | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are SystemName | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsFileSystemSummary**](PagedResultsFileSystemSummary.md)

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

# **directories_get_root_file_entries**
> PagedResultsFileEntry directories_get_root_file_entries(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of root directories configured in this FastStats system

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
api_instance = apteco_api.DirectoriesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Type (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Type (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of root directories configured in this FastStats system
    api_response = api_instance.directories_get_root_file_entries(data_view_name, system_name, timeout_in_seconds=timeout_in_seconds, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoriesApi->directories_get_root_file_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service&#39;s configuration | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Type | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Type | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsFileEntry**](PagedResultsFileEntry.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of root directories |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the root directories |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directories_upsert_directory**
> FileEntry directories_upsert_directory(data_view_name, system_name, directory_path, timeout_in_seconds=timeout_in_seconds)

Ensure that a directory exists in a location

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
api_instance = apteco_api.DirectoriesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
directory_path = 'directory_path_example' # str | The path to the directory that should exist
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)

try:
    # Ensure that a directory exists in a location
    api_response = api_instance.directories_upsert_directory(data_view_name, system_name, directory_path, timeout_in_seconds=timeout_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoriesApi->directories_upsert_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **directory_path** | **str**| The path to the directory that should exist | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service&#39;s configuration | [optional] 

### Return type

[**FileEntry**](FileEntry.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Info on the new directory |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given directory |  -  |
**404** | The system name or specified directory couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

