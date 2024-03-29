# apteco_api.GroupsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_get_group_details**](GroupsApi.md#groups_get_group_details) | **GET** /{dataViewName}/Groups/{groupId} | Returns details for the given group
[**groups_get_groups**](GroupsApi.md#groups_get_groups) | **GET** /{dataViewName}/Groups | Returns all groups in the DataView.
[**groups_get_user_details_for_group**](GroupsApi.md#groups_get_user_details_for_group) | **GET** /{dataViewName}/Groups/{groupId}/Users | Returns all users in the given group.
[**groups_get_user_details_for_unallocated_group**](GroupsApi.md#groups_get_user_details_for_unallocated_group) | **GET** /{dataViewName}/Groups/Unallocated/Users | Returns all users that haven&#39;t been allocated to a group.


# **groups_get_group_details**
> GroupDetail groups_get_group_details(data_view_name, group_id)

Returns details for the given group

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
    api_instance = apteco_api.GroupsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
group_id = 56 # int | The id of the group to view the details for

    try:
        # Returns details for the given group
        api_response = api_instance.groups_get_group_details(data_view_name, group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->groups_get_group_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **group_id** | **int**| The id of the group to view the details for | 

### Return type

[**GroupDetail**](GroupDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group&#39;s details |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t allowed to see the group details |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_groups**
> PagedResultsGroupSummary groups_get_groups(data_view_name, system_name=system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns all groups in the DataView.

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
    api_instance = apteco_api.GroupsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | If specified, whether to limit to only groups attached to the system name (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns all groups in the DataView.
        api_response = api_instance.groups_get_groups(data_view_name, system_name=system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->groups_get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| If specified, whether to limit to only groups attached to the system name | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsGroupSummary**](PagedResultsGroupSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all groups |  -  |
**400** | Bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_user_details_for_group**
> PagedResultsUserSummary groups_get_user_details_for_group(data_view_name, group_id, include_disabled=include_disabled, filter=filter, order_by=order_by, offset=offset, count=count)

Returns all users in the given group.

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
    api_instance = apteco_api.GroupsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
group_id = 56 # int | The id of the group to get users for
include_disabled = 'include_disabled_example' # str | If specified, whether to include disabled users, not disabled users or both.  Defaults to not disabled only (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns all users in the given group.
        api_response = api_instance.groups_get_user_details_for_group(data_view_name, group_id, include_disabled=include_disabled, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->groups_get_user_details_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **group_id** | **int**| The id of the group to get users for | 
 **include_disabled** | **str**| If specified, whether to include disabled users, not disabled users or both.  Defaults to not disabled only | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserSummary**](PagedResultsUserSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all users in the given group |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_user_details_for_unallocated_group**
> PagedResultsUserSummary groups_get_user_details_for_unallocated_group(data_view_name, include_disabled=include_disabled, filter=filter, order_by=order_by, offset=offset, count=count)

Returns all users that haven't been allocated to a group.

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
    api_instance = apteco_api.GroupsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
include_disabled = 'include_disabled_example' # str | If specified, whether to include disabled users, not disabled users or both.  Defaults to not disabled only (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns all users that haven't been allocated to a group.
        api_response = api_instance.groups_get_user_details_for_unallocated_group(data_view_name, include_disabled=include_disabled, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->groups_get_user_details_for_unallocated_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **include_disabled** | **str**| If specified, whether to include disabled users, not disabled users or both.  Defaults to not disabled only | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserSummary**](PagedResultsUserSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all users |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

