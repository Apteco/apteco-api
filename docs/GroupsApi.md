# apteco_api.GroupsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_get_group_details**](GroupsApi.md#groups_get_group_details) | **GET** /{dataViewName}/Groups/{groupId} | Requires OrbitAdmin: Returns details for the given group
[**groups_get_groups**](GroupsApi.md#groups_get_groups) | **GET** /{dataViewName}/Groups | Requires OrbitAdmin: Returns all groups in the DataView.
[**groups_get_user_details_for_group**](GroupsApi.md#groups_get_user_details_for_group) | **GET** /{dataViewName}/Groups/{groupId}/Users | Requires OrbitAdmin: Returns all users in the given group.
[**groups_get_user_details_for_unallocated_group**](GroupsApi.md#groups_get_user_details_for_unallocated_group) | **GET** /{dataViewName}/Groups/Unallocated/Users | Requires OrbitAdmin: Returns all users that haven&#39;t been allocated to a group.


# **groups_get_group_details**
> UserDetail groups_get_group_details(data_view_name, group_id)

Requires OrbitAdmin: Returns details for the given group

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
api_instance = apteco_api.GroupsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
group_id = 56 # int | The id of the group to view the details for

try:
    # Requires OrbitAdmin: Returns details for the given group
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

[**UserDetail**](UserDetail.md)

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
> PagedResultsGroupSummary groups_get_groups(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns all groups in the DataView.

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
api_instance = apteco_api.GroupsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Returns all groups in the DataView.
    api_response = api_instance.groups_get_groups(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name | [optional] 
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
> PagedResultsUserSummary groups_get_user_details_for_group(data_view_name, group_id, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns all users in the given group.

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
api_instance = apteco_api.GroupsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
group_id = 56 # int | The id of the group to get users for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Returns all users in the given group.
    api_response = api_instance.groups_get_user_details_for_group(data_view_name, group_id, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_get_user_details_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **group_id** | **int**| The id of the group to get users for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate | [optional] 
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
> PagedResultsUserSummary groups_get_user_details_for_unallocated_group(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns all users that haven't been allocated to a group.

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
api_instance = apteco_api.GroupsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Returns all users that haven't been allocated to a group.
    api_response = api_instance.groups_get_user_details_for_unallocated_group(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_get_user_details_for_unallocated_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate | [optional] 
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

