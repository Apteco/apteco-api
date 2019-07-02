# apteco_api.TemporaryFilesApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temporary_files_get_temporary_file**](TemporaryFilesApi.md#temporary_files_get_temporary_file) | **GET** /{dataViewName}/TemporaryFiles/{id} | Returns the contents of a temporary file with the given id
[**temporary_files_get_temporary_file_part**](TemporaryFilesApi.md#temporary_files_get_temporary_file_part) | **GET** /{dataViewName}/TemporaryFiles/{id}/{partNumber} | Returns the contents of a temporary file part with the given id and part number
[**temporary_files_upsert_temporary_file**](TemporaryFilesApi.md#temporary_files_upsert_temporary_file) | **PUT** /{dataViewName}/TemporaryFiles/{id} | Creates or updates a temporary file with the given id
[**temporary_files_upsert_temporary_file_part**](TemporaryFilesApi.md#temporary_files_upsert_temporary_file_part) | **PUT** /{dataViewName}/TemporaryFiles/{id}/{partNumber} | Creates or updates part of a temporary file with the given id and part number


# **temporary_files_get_temporary_file**
> file temporary_files_get_temporary_file(data_view_name, id)

Returns the contents of a temporary file with the given id

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
api_instance = apteco_api.TemporaryFilesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
id = 'id_example' # str | The id of the temporary file to return the contents for

try:
    # Returns the contents of a temporary file with the given id
    api_response = api_instance.temporary_files_get_temporary_file(data_view_name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemporaryFilesApi->temporary_files_get_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **id** | **str**| The id of the temporary file to return the contents for | 

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
**200** | The contents of the temporary file |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given temporary file |  -  |
**404** | The system name or specified temporary file couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temporary_files_get_temporary_file_part**
> file temporary_files_get_temporary_file_part(data_view_name, id, part_number)

Returns the contents of a temporary file part with the given id and part number

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
api_instance = apteco_api.TemporaryFilesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
id = 'id_example' # str | The id of the temporary file
part_number = 56 # int | The number of the temporary file part to return the contents for

try:
    # Returns the contents of a temporary file part with the given id and part number
    api_response = api_instance.temporary_files_get_temporary_file_part(data_view_name, id, part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemporaryFilesApi->temporary_files_get_temporary_file_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **id** | **str**| The id of the temporary file | 
 **part_number** | **int**| The number of the temporary file part to return the contents for | 

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
**200** | The contents of the temporary file part |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the contents of the given temporary file part |  -  |
**404** | The system name, specified temporary file or part couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temporary_files_upsert_temporary_file**
> TemporaryFile temporary_files_upsert_temporary_file(data_view_name, id, file)

Creates or updates a temporary file with the given id

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
api_instance = apteco_api.TemporaryFilesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
id = 'id_example' # str | The id for the temporary file to create or update
file = '/path/to/file' # file | The file to upload.

try:
    # Creates or updates a temporary file with the given id
    api_response = api_instance.temporary_files_upsert_temporary_file(data_view_name, id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemporaryFilesApi->temporary_files_upsert_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **id** | **str**| The id for the temporary file to create or update | 
 **file** | **file**| The file to upload. | 

### Return type

[**TemporaryFile**](TemporaryFile.md)

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
**403** | The given session is not allowed to modify the contents of the given file |  -  |
**404** | The system name or couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temporary_files_upsert_temporary_file_part**
> TemporaryFilePart temporary_files_upsert_temporary_file_part(data_view_name, id, part_number, file, final_part=final_part)

Creates or updates part of a temporary file with the given id and part number

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
api_instance = apteco_api.TemporaryFilesApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
id = 'id_example' # str | The id for the temporary file
part_number = 56 # int | The number of the temporary file part to create or update.  This is zero-based
file = '/path/to/file' # file | The file to upload.
final_part = True # bool | Whether this part is the final part and the full temporary file should be assembled.  If this is not specified it defaults to false.  If this is set to true all parts from 0 up to this partIndex must already exist (optional)

try:
    # Creates or updates part of a temporary file with the given id and part number
    api_response = api_instance.temporary_files_upsert_temporary_file_part(data_view_name, id, part_number, file, final_part=final_part)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemporaryFilesApi->temporary_files_upsert_temporary_file_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **id** | **str**| The id for the temporary file | 
 **part_number** | **int**| The number of the temporary file part to create or update.  This is zero-based | 
 **file** | **file**| The file to upload. | 
 **final_part** | **bool**| Whether this part is the final part and the full temporary file should be assembled.  If this is not specified it defaults to false.  If this is set to true all parts from 0 up to this partIndex must already exist | [optional] 

### Return type

[**TemporaryFilePart**](TemporaryFilePart.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Details of the created file part or, if the final part was specified |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to modify the contents of the given file |  -  |
**404** | The system name or part couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

