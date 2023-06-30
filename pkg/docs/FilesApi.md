# apteco_api.FilesApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_delete_file**](FilesApi.md#files_delete_file) | **DELETE** /{dataViewName}/Files/{systemName}/{filePath} | Deletes file at location
[**files_get_file**](FilesApi.md#files_get_file) | **GET** /{dataViewName}/Files/{systemName}/{filePath} | Returns the contents for a file
[**files_upsert_file**](FilesApi.md#files_upsert_file) | **PUT** /{dataViewName}/Files/{systemName}/{filePath} | Creates or updates a file at a location


# **files_delete_file**
> files_delete_file(data_view_name, system_name, file_path, timeout_in_seconds=timeout_in_seconds)

Deletes file at location

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
    api_instance = apteco_api.FilesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
file_path = 'file_path_example' # str | The path to the file to be deleted
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)

    try:
        # Deletes file at location
        api_instance.files_delete_file(data_view_name, system_name, file_path, timeout_in_seconds=timeout_in_seconds)
    except ApiException as e:
        print("Exception when calling FilesApi->files_delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **file_path** | **str**| The path to the file to be deleted | 
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
**200** | The file was deleted |  -  |
**204** | Success |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file |  -  |
**404** | The system name or specified directory/file couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get_file**
> file files_get_file(data_view_name, system_name, file_path, timeout_in_seconds=timeout_in_seconds)

Returns the contents for a file

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
    api_instance = apteco_api.FilesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
file_path = 'file_path_example' # str | The path of the file to return the contents for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)

    try:
        # Returns the contents for a file
        api_response = api_instance.files_get_file(data_view_name, system_name, file_path, timeout_in_seconds=timeout_in_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->files_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **file_path** | **str**| The path of the file to return the contents for | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service&#39;s configuration | [optional] 

### Return type

**file**

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contents of the file |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file |  -  |
**404** | The system name or specified directory couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_upsert_file**
> FileEntry files_upsert_file(data_view_name, system_name, file_path, file, timeout_in_seconds=timeout_in_seconds)

Creates or updates a file at a location

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
    api_instance = apteco_api.FilesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
file_path = 'file_path_example' # str | The path in the system where the file will be put
file = '/path/to/file' # file | The file to upload.
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration (optional)

    try:
        # Creates or updates a file at a location
        api_response = api_instance.files_upsert_file(data_view_name, system_name, file_path, file, timeout_in_seconds=timeout_in_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->files_upsert_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **file_path** | **str**| The path in the system where the file will be put | 
 **file** | **file**| The file to upload. | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service&#39;s configuration | [optional] 

### Return type

[**FileEntry**](FileEntry.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Details of the created file |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given file |  -  |
**404** | The system name or specified directory couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

