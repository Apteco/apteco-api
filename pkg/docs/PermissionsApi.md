# apteco_api.PermissionsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_create_permission_for_group**](PermissionsApi.md#permissions_create_permission_for_group) | **POST** /{dataViewName}/Permissions/{systemName}/Group/{groupId} | EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the group.
[**permissions_create_permission_for_system**](PermissionsApi.md#permissions_create_permission_for_system) | **POST** /{dataViewName}/Permissions/{systemName}/System | EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the system.
[**permissions_create_permission_for_team**](PermissionsApi.md#permissions_create_permission_for_team) | **POST** /{dataViewName}/Permissions/{systemName}/Team/{teamId} | EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the team.
[**permissions_create_permission_for_user**](PermissionsApi.md#permissions_create_permission_for_user) | **POST** /{dataViewName}/Permissions/{systemName}/User/{userId} | EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the user.
[**permissions_delete_permission**](PermissionsApi.md#permissions_delete_permission) | **DELETE** /{dataViewName}/Permissions/{systemName}/{permissionId} | EXPERIMENTAL: Requires OrbitAdmin: Deletes the specified permission
[**permissions_get_permissions_for_group**](PermissionsApi.md#permissions_get_permissions_for_group) | **GET** /{dataViewName}/Permissions/{systemName}/Group/{groupId} | EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular group
[**permissions_get_permissions_for_permission_set**](PermissionsApi.md#permissions_get_permissions_for_permission_set) | **GET** /{dataViewName}/Permissions/{systemName}/PermissionSet/{permissionSetId} | EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular permission set
[**permissions_get_permissions_for_system**](PermissionsApi.md#permissions_get_permissions_for_system) | **GET** /{dataViewName}/Permissions/{systemName}/System | EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular system
[**permissions_get_permissions_for_team**](PermissionsApi.md#permissions_get_permissions_for_team) | **GET** /{dataViewName}/Permissions/{systemName}/Team/{teamId} | EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular team
[**permissions_get_permissions_for_user**](PermissionsApi.md#permissions_get_permissions_for_user) | **GET** /{dataViewName}/Permissions/{systemName}/User/{userId} | EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular user
[**permissions_is_authorised**](PermissionsApi.md#permissions_is_authorised) | **GET** /{dataViewName}/Permissions/{systemName}/{permissionType}/{permission}/{resourceType}/{resource} | EXPERIMENTAL: Returns whether the current user is authorised to access a particular resource for a particular permission
[**permissions_modify_permission**](PermissionsApi.md#permissions_modify_permission) | **PUT** /{dataViewName}/Permissions/{systemName}/{permissionId} | EXPERIMENTAL: Requires OrbitAdmin: Modify the specified permission


# **permissions_create_permission_for_group**
> AuthorisedPermissionWithLookups permissions_create_permission_for_group(data_view_name, system_name, group_id, permission=permission)

EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the group.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
group_id = 56 # int | The id of the group to apply the permission to
permission = apteco_api.Permission() # Permission | The details of the permission to create (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the group.
        api_response = api_instance.permissions_create_permission_for_group(data_view_name, system_name, group_id, permission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_create_permission_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **group_id** | **int**| The id of the group to apply the permission to | 
 **permission** | [**Permission**](Permission.md)| The details of the permission to create | [optional] 

### Return type

[**AuthorisedPermissionWithLookups**](AuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The permission was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to create this permission.  Only admins can create permissions |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_create_permission_for_system**
> AuthorisedPermissionWithLookups permissions_create_permission_for_system(data_view_name, system_name, permission=permission)

EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the system.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
permission = apteco_api.Permission() # Permission | The details of the permission to create (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the system.
        api_response = api_instance.permissions_create_permission_for_system(data_view_name, system_name, permission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_create_permission_for_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **permission** | [**Permission**](Permission.md)| The details of the permission to create | [optional] 

### Return type

[**AuthorisedPermissionWithLookups**](AuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The permission was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to create this permission.  Only admins can create permissions |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_create_permission_for_team**
> AuthorisedPermissionWithLookups permissions_create_permission_for_team(data_view_name, system_name, team_id, permission=permission)

EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the team.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
team_id = 56 # int | The id of the team to apply the permission to
permission = apteco_api.Permission() # Permission | The details of the permission to create (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the team.
        api_response = api_instance.permissions_create_permission_for_team(data_view_name, system_name, team_id, permission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_create_permission_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **team_id** | **int**| The id of the team to apply the permission to | 
 **permission** | [**Permission**](Permission.md)| The details of the permission to create | [optional] 

### Return type

[**AuthorisedPermissionWithLookups**](AuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The permission was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to create this permission.  Only admins can create permissions |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_create_permission_for_user**
> AuthorisedPermissionWithLookups permissions_create_permission_for_user(data_view_name, system_name, user_id, permission=permission)

EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the user.

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
user_id = 56 # int | The id of the user to apply the permission to
permission = apteco_api.Permission() # Permission | The details of the permission to create (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Creates a new permission from the given details, using the default permission set for the user.
        api_response = api_instance.permissions_create_permission_for_user(data_view_name, system_name, user_id, permission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_create_permission_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **user_id** | **int**| The id of the user to apply the permission to | 
 **permission** | [**Permission**](Permission.md)| The details of the permission to create | [optional] 

### Return type

[**AuthorisedPermissionWithLookups**](AuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The permission was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to create this permission.  Only admins can create permissions |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_delete_permission**
> permissions_delete_permission(data_view_name, system_name, permission_id)

EXPERIMENTAL: Requires OrbitAdmin: Deletes the specified permission

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
permission_id = 56 # int | The id of the permission to delete

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Deletes the specified permission
        api_instance.permissions_delete_permission(data_view_name, system_name, permission_id)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_delete_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **permission_id** | **int**| The id of the permission to delete | 

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
**204** | The permission was deleted successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete this permission.  Only admins can delete permissions |  -  |
**404** | The DataView or permission couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_get_permissions_for_group**
> PagedResultsAuthorisedPermissionWithLookups permissions_get_permissions_for_group(data_view_name, system_name, group_id, filter=filter, order_by=order_by, offset=offset, count=count)

EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular group

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
group_id = 56 # int | The id of the group to get the permissions for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are ResourceType, Resource, PermissionType. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular group
        api_response = api_instance.permissions_get_permissions_for_group(data_view_name, system_name, group_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_get_permissions_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **group_id** | **int**| The id of the group to get the permissions for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAuthorisedPermissionWithLookups**](PagedResultsAuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | A list of valid permissions |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to request permissions.  Only admins can request permissions |  -  |
**404** | The DataView or system couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_get_permissions_for_permission_set**
> PagedResultsAuthorisedPermissionWithLookups permissions_get_permissions_for_permission_set(data_view_name, system_name, permission_set_id, filter=filter, order_by=order_by, offset=offset, count=count)

EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular permission set

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
permission_set_id = 56 # int | The id of the permission set to get the permissions for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are ResourceType, Resource, PermissionType. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular permission set
        api_response = api_instance.permissions_get_permissions_for_permission_set(data_view_name, system_name, permission_set_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_get_permissions_for_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **permission_set_id** | **int**| The id of the permission set to get the permissions for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAuthorisedPermissionWithLookups**](PagedResultsAuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | A list of valid permissions |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to request permissions.  Only admins can request permissions |  -  |
**404** | The DataView or system couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_get_permissions_for_system**
> PagedResultsAuthorisedPermissionWithLookups permissions_get_permissions_for_system(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)

EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular system

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are ResourceType, Resource, PermissionType. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular system
        api_response = api_instance.permissions_get_permissions_for_system(data_view_name, system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_get_permissions_for_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAuthorisedPermissionWithLookups**](PagedResultsAuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | A list of valid permissions |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to request permissions.  Only admins can request permissions |  -  |
**404** | The DataView or system couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_get_permissions_for_team**
> PagedResultsAuthorisedPermissionWithLookups permissions_get_permissions_for_team(data_view_name, system_name, team_id, filter=filter, order_by=order_by, offset=offset, count=count)

EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular team

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
team_id = 56 # int | The id of the team to get the permissions for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are ResourceType, Resource, PermissionType. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular team
        api_response = api_instance.permissions_get_permissions_for_team(data_view_name, system_name, team_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_get_permissions_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **team_id** | **int**| The id of the team to get the permissions for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAuthorisedPermissionWithLookups**](PagedResultsAuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | A list of valid permissions |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to request permissions.  Only admins can request permissions |  -  |
**404** | The DataView or system couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_get_permissions_for_user**
> PagedResultsAuthorisedPermissionWithLookups permissions_get_permissions_for_user(data_view_name, system_name, user_id, filter=filter, order_by=order_by, offset=offset, count=count)

EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular user

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
user_id = 56 # int | The id of the user to get the permissions for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are ResourceType, Resource, PermissionType. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Returns the permissions for a particular user
        api_response = api_instance.permissions_get_permissions_for_user(data_view_name, system_name, user_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_get_permissions_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **user_id** | **int**| The id of the user to get the permissions for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are ResourceType, Resource, PermissionType. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAuthorisedPermissionWithLookups**](PagedResultsAuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | A list of valid permissions |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to request permissions.  Only admins can request permissions |  -  |
**404** | The DataView or system couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_is_authorised**
> bool permissions_is_authorised(data_view_name, system_name, permission_type, permission, resource_type, resource)

EXPERIMENTAL: Returns whether the current user is authorised to access a particular resource for a particular permission

EXPERIMENTAL

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
permission_type = 'permission_type_example' # str | The type of permission to get the permissions for
permission = 'permission_example' # str | The permission to test for
resource_type = 'resource_type_example' # str | The type of resource to get the permissions for
resource = 'resource_example' # str | The path for the particular type of resource

    try:
        # EXPERIMENTAL: Returns whether the current user is authorised to access a particular resource for a particular permission
        api_response = api_instance.permissions_is_authorised(data_view_name, system_name, permission_type, permission, resource_type, resource)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_is_authorised: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **permission_type** | **str**| The type of permission to get the permissions for | 
 **permission** | **str**| The permission to test for | 
 **resource_type** | **str**| The type of resource to get the permissions for | 
 **resource** | **str**| The path for the particular type of resource | 

### Return type

**bool**

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Whether the user is authorised |  -  |
**400** | A bad request |  -  |
**404** | The DataView or system couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_modify_permission**
> AuthorisedPermissionWithLookups permissions_modify_permission(data_view_name, system_name, permission_id, permission=permission)

EXPERIMENTAL: Requires OrbitAdmin: Modify the specified permission

EXPERIMENTAL  This endpoint is only available for users with the OrbitAdmin role

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
    api_instance = apteco_api.PermissionsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The name of the FastStats system to act on
permission_id = 56 # int | The permission id of the permission
permission = apteco_api.AuthorisedPermission() # AuthorisedPermission | The permission to modify (optional)

    try:
        # EXPERIMENTAL: Requires OrbitAdmin: Modify the specified permission
        api_response = api_instance.permissions_modify_permission(data_view_name, system_name, permission_id, permission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->permissions_modify_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The name of the FastStats system to act on | 
 **permission_id** | **int**| The permission id of the permission | 
 **permission** | [**AuthorisedPermission**](AuthorisedPermission.md)| The permission to modify | [optional] 

### Return type

[**AuthorisedPermissionWithLookups**](AuthorisedPermissionWithLookups.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The permission was modified successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to modify this permission.  Only admins can modify permissions |  -  |
**404** | The DataView or permission couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

