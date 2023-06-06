# apteco_api.FastStatsSystemsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fast_stats_systems_get_all_fast_stats_system_items**](FastStatsSystemsApi.md#fast_stats_systems_get_all_fast_stats_system_items) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/All | Gets all FastStats systems items - variables, var codes, tables and folders
[**fast_stats_systems_get_fast_stats_folder**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_folder) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/Folders/{path} | Gets the folder structure for the FastStats system
[**fast_stats_systems_get_fast_stats_root_folder**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_root_folder) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/Folders | Gets the items in the root of the FastStats system folder structure
[**fast_stats_systems_get_fast_stats_system**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_system) | **GET** /{dataViewName}/FastStatsSystems/{systemName} | Returns some top-level details for the specified FastStats system
[**fast_stats_systems_get_fast_stats_systems**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_systems) | **GET** /{dataViewName}/FastStatsSystems | Returns the list of FastStats systems available
[**fast_stats_systems_get_fast_stats_table**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_table) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/Tables/{tableName} | Gets the details for a particular table in the FastStats system
[**fast_stats_systems_get_fast_stats_tables**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_tables) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/Tables | Gets all the tables present in the FastStats system
[**fast_stats_systems_get_fast_stats_variable**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_variable) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/Variables/{variableName} | Gets the details for a particular variable in the FastStats system
[**fast_stats_systems_get_fast_stats_variable_codes**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_variable_codes) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/Variables/{variableName}/Codes | Gets all the categories (var codes) for the specified variable in the FastStats system if it is a selector variable
[**fast_stats_systems_get_fast_stats_variables**](FastStatsSystemsApi.md#fast_stats_systems_get_fast_stats_variables) | **GET** /{dataViewName}/FastStatsSystems/{systemName}/Variables | Gets all the variables present in the FastStats system
[**fast_stats_systems_refresh_system_information_sync**](FastStatsSystemsApi.md#fast_stats_systems_refresh_system_information_sync) | **POST** /{dataViewName}/FastStatsSystems/{systemName}/RefreshInformationSync | Requires OrbitAdmin: An endpoint to request the API refresh any information it holds on the given FastStats system.  This endpoint will wait until the refresh has completed before returning.


# **fast_stats_systems_get_all_fast_stats_system_items**
> PagedResultsFastStatsSystemItem fast_stats_systems_get_all_fast_stats_system_items(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Gets all FastStats systems items - variables, var codes, tables and folders

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Key, Type, TableName, VariableType (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Key, Type, TableName, VariableType (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Gets all FastStats systems items - variables, var codes, tables and folders
        api_response = api_instance.fast_stats_systems_get_all_fast_stats_system_items(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_all_fast_stats_system_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Key, Type, TableName, VariableType | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Key, Type, TableName, VariableType | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsFastStatsSystemItem**](PagedResultsFastStatsSystemItem.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all parts of the FastStats system |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this system |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_get_fast_stats_folder**
> Folder fast_stats_systems_get_fast_stats_folder(data_view_name, system_name, path, filter=filter, order_by=order_by, offset=offset, count=count)

Gets the folder structure for the FastStats system

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
path = 'path_example' # str | The path to the folder that should be retrieved
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Description, Type, TableName, VariableType (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Description, Type, TableName, VariableType (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Gets the folder structure for the FastStats system
        api_response = api_instance.fast_stats_systems_get_fast_stats_folder(data_view_name, system_name, path, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **path** | **str**| The path to the folder that should be retrieved | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Description, Type, TableName, VariableType | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Description, Type, TableName, VariableType | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The FastStats system folder structure |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the folder structure for this system |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_get_fast_stats_root_folder**
> PagedResultsFolderStructureNode fast_stats_systems_get_fast_stats_root_folder(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Gets the items in the root of the FastStats system folder structure

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Description, Type, TableName, VariableType (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Description, Type, TableName, VariableType (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Gets the items in the root of the FastStats system folder structure
        api_response = api_instance.fast_stats_systems_get_fast_stats_root_folder(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_root_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Description, Type, TableName, VariableType | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Description, Type, TableName, VariableType | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsFolderStructureNode**](PagedResultsFolderStructureNode.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The items in the root of the FastStats system folder structure |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the folder structure for this system |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_get_fast_stats_system**
> FastStatsSystemDetail fast_stats_systems_get_fast_stats_system(data_view_name, system_name)

Returns some top-level details for the specified FastStats system

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to return details for

    try:
        # Returns some top-level details for the specified FastStats system
        api_response = api_instance.fast_stats_systems_get_fast_stats_system(data_view_name, system_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to return details for | 

### Return type

[**FastStatsSystemDetail**](FastStatsSystemDetail.md)

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

# **fast_stats_systems_get_fast_stats_systems**
> PagedResultsFastStatsSystemSummary fast_stats_systems_get_fast_stats_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of FastStats systems available

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Description, FastStatsBuildDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Description, FastStatsBuildDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns the list of FastStats systems available
        api_response = api_instance.fast_stats_systems_get_fast_stats_systems(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Description, FastStatsBuildDate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Description, FastStatsBuildDate | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsFastStatsSystemSummary**](PagedResultsFastStatsSystemSummary.md)

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

# **fast_stats_systems_get_fast_stats_table**
> Table fast_stats_systems_get_fast_stats_table(data_view_name, system_name, table_name)

Gets the details for a particular table in the FastStats system

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
table_name = 'table_name_example' # str | The name of the table to get the details for

    try:
        # Gets the details for a particular table in the FastStats system
        api_response = api_instance.fast_stats_systems_get_fast_stats_table(data_view_name, system_name, table_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **table_name** | **str**| The name of the table to get the details for | 

### Return type

[**Table**](Table.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the specified table |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the particular table for this system |  -  |
**404** | The system name or specified variable couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_get_fast_stats_tables**
> PagedResultsTable fast_stats_systems_get_fast_stats_tables(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Gets all the tables present in the FastStats system

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, SingularDisplayName, PluralDisplayName, TotalRecords (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, SingularDisplayName, PluralDisplayName, TotalRecords (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Gets all the tables present in the FastStats system
        api_response = api_instance.fast_stats_systems_get_fast_stats_tables(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, SingularDisplayName, PluralDisplayName, TotalRecords | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, SingularDisplayName, PluralDisplayName, TotalRecords | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsTable**](PagedResultsTable.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of FastStats tables |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see tables for this system |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_get_fast_stats_variable**
> Variable fast_stats_systems_get_fast_stats_variable(data_view_name, system_name, variable_name)

Gets the details for a particular variable in the FastStats system

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
variable_name = 'variable_name_example' # str | The name of the variable to get the details for

    try:
        # Gets the details for a particular variable in the FastStats system
        api_response = api_instance.fast_stats_systems_get_fast_stats_variable(data_view_name, system_name, variable_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **variable_name** | **str**| The name of the variable to get the details for | 

### Return type

[**Variable**](Variable.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the specified variable |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the particular variable for this system |  -  |
**404** | The system name or specified variable couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_get_fast_stats_variable_codes**
> PagedResultsVarCode fast_stats_systems_get_fast_stats_variable_codes(data_view_name, system_name, variable_name, filter=filter, order_by=order_by, offset=offset, count=count)

Gets all the categories (var codes) for the specified variable in the FastStats system if it is a selector variable

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
variable_name = 'variable_name_example' # str | The name of the variable to get the var codes for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Code, Description, Count (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Code, Description, Count (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Gets all the categories (var codes) for the specified variable in the FastStats system if it is a selector variable
        api_response = api_instance.fast_stats_systems_get_fast_stats_variable_codes(data_view_name, system_name, variable_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_variable_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **variable_name** | **str**| The name of the variable to get the var codes for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Code, Description, Count | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Code, Description, Count | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsVarCode**](PagedResultsVarCode.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The var codes of the specified variable |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the particular variable for this system |  -  |
**404** | The system name or specified variable couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_get_fast_stats_variables**
> PagedResultsVariable fast_stats_systems_get_fast_stats_variables(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Gets all the variables present in the FastStats system

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name, Description, Type, SelectorType, TableName, NumberOfCodes, FolderName (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name, Description, Type, SelectorType, TableName, NumberOfCodes, FolderName (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Gets all the variables present in the FastStats system
        api_response = api_instance.fast_stats_systems_get_fast_stats_variables(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_get_fast_stats_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name, Description, Type, SelectorType, TableName, NumberOfCodes, FolderName | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name, Description, Type, SelectorType, TableName, NumberOfCodes, FolderName | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsVariable**](PagedResultsVariable.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of FastStats variables |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see variables for this system |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_stats_systems_refresh_system_information_sync**
> fast_stats_systems_refresh_system_information_sync(data_view_name, system_name)

Requires OrbitAdmin: An endpoint to request the API refresh any information it holds on the given FastStats system.  This endpoint will wait until the refresh has completed before returning.

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
    api_instance = apteco_api.FastStatsSystemsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on

    try:
        # Requires OrbitAdmin: An endpoint to request the API refresh any information it holds on the given FastStats system.  This endpoint will wait until the refresh has completed before returning.
        api_instance.fast_stats_systems_refresh_system_information_sync(data_view_name, system_name)
    except ApiException as e:
        print("Exception when calling FastStatsSystemsApi->fast_stats_systems_refresh_system_information_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 

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
**201** | The system successfully refreshed |  -  |
**204** | Success |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this system |  -  |
**404** | The system name couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

