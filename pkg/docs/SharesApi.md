# apteco_api.SharesApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shares_create_share**](SharesApi.md#shares_create_share) | **POST** /{dataViewName}/Shares | Creates a new share from the given details, sharing from the logged in user.
[**shares_create_share_update**](SharesApi.md#shares_create_share_update) | **POST** /{dataViewName}/Shares/{shareId}/Updates | Creates a new share update from the given details, sharing from the logged in user.
[**shares_delete_share**](SharesApi.md#shares_delete_share) | **DELETE** /{dataViewName}/Shares/{shareId} | Deletes the specified share
[**shares_get_share**](SharesApi.md#shares_get_share) | **GET** /{dataViewName}/Shares/{shareId} | Returns the details of a particular share
[**shares_get_share_groups**](SharesApi.md#shares_get_share_groups) | **GET** /{dataViewName}/Shares/{shareId}/Groups | Returns the list of groups that are associated with a particular share
[**shares_get_share_update**](SharesApi.md#shares_get_share_update) | **GET** /{dataViewName}/Shares/{shareId}/Updates/{shareUpdateId} | Returns a specific update that is associated with a particular share
[**shares_get_share_update_added_users**](SharesApi.md#shares_get_share_update_added_users) | **GET** /{dataViewName}/Shares/{shareId}/Updates/{shareUpdateId}/AddedUsers | Returns the list of the users added to a share as part of a specific update
[**shares_get_share_update_removed_users**](SharesApi.md#shares_get_share_update_removed_users) | **GET** /{dataViewName}/Shares/{shareId}/Updates/{shareUpdateId}/RemovedUsers | Returns the list of the users removed from a share as part of a specific update
[**shares_get_share_updates**](SharesApi.md#shares_get_share_updates) | **GET** /{dataViewName}/Shares/{shareId}/Updates | Returns the updates that are associated with a particular share
[**shares_get_share_users**](SharesApi.md#shares_get_share_users) | **GET** /{dataViewName}/Shares/{shareId}/Users | Returns the list of users that are associated with a particular share
[**shares_get_shares**](SharesApi.md#shares_get_shares) | **GET** /{dataViewName}/Shares | Requires OrbitAdmin: Gets summary information about each share in the DataView.


# **shares_create_share**
> ShareDetail shares_create_share(data_view_name, share_detail=share_detail)

Creates a new share from the given details, sharing from the logged in user.

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_detail = apteco_api.CreateShareDetail() # CreateShareDetail | The details of the shareable item (collection, audience, etc) to share and who to share it with (optional)

    try:
        # Creates a new share from the given details, sharing from the logged in user.
        api_response = api_instance.shares_create_share(data_view_name, share_detail=share_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_create_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_detail** | [**CreateShareDetail**](CreateShareDetail.md)| The details of the shareable item (collection, audience, etc) to share and who to share it with | [optional] 

### Return type

[**ShareDetail**](ShareDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The shareable was shared successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_create_share_update**
> CreatedShareUpdateDetail shares_create_share_update(data_view_name, share_id, share_update=share_update)

Creates a new share update from the given details, sharing from the logged in user.

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share to update
share_update = apteco_api.CreateShareUpdate() # CreateShareUpdate | The details of the share update, including who to add and remove from the share and notification settings (optional)

    try:
        # Creates a new share update from the given details, sharing from the logged in user.
        api_response = api_instance.shares_create_share_update(data_view_name, share_id, share_update=share_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_create_share_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share to update | 
 **share_update** | [**CreateShareUpdate**](CreateShareUpdate.md)| The details of the share update, including who to add and remove from the share and notification settings | [optional] 

### Return type

[**CreatedShareUpdateDetail**](CreatedShareUpdateDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The share was updated successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_delete_share**
> shares_delete_share(data_view_name, share_id)

Deletes the specified share

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share to delete

    try:
        # Deletes the specified share
        api_instance.shares_delete_share(data_view_name, share_id)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_delete_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share to delete | 

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
**204** | The share was deleted successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete this share.  Only owners of the shared item or admins can delete shares |  -  |
**404** | The DataView or share couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_share**
> ShareDetail shares_get_share(data_view_name, share_id)

Returns the details of a particular share

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share to view

    try:
        # Returns the details of a particular share
        api_response = api_instance.shares_get_share(data_view_name, share_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share to view | 

### Return type

[**ShareDetail**](ShareDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The share details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this share |  -  |
**404** | The DataView or share couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_share_groups**
> PagedResultsGroupDetail shares_get_share_groups(data_view_name, share_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of groups that are associated with a particular share

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share to view the groups for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, Name. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, Name. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns the list of groups that are associated with a particular share
        api_response = api_instance.shares_get_share_groups(data_view_name, share_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_share_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share to view the groups for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, Name. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, Name. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsGroupDetail**](PagedResultsGroupDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current list of groups that the shareable item is shared with |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this share |  -  |
**404** | The DataView or share couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_share_update**
> ShareUpdate shares_get_share_update(data_view_name, share_id, share_update_id)

Returns a specific update that is associated with a particular share

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share the update is associated with
share_update_id = 56 # int | The id of the share update to view

    try:
        # Returns a specific update that is associated with a particular share
        api_response = api_instance.shares_get_share_update(data_view_name, share_id, share_update_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_share_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share the update is associated with | 
 **share_update_id** | **int**| The id of the share update to view | 

### Return type

[**ShareUpdate**](ShareUpdate.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified update that are associated with the particular share |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this share |  -  |
**404** | The DataView, share or the update couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_share_update_added_users**
> PagedResultsUserDisplayDetails shares_get_share_update_added_users(data_view_name, share_id, share_update_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of the users added to a share as part of a specific update

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share the update is associated with
share_update_id = 56 # int | The id of the share update to view
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Firstname, Surname. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Firstname, Surname. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns the list of the users added to a share as part of a specific update
        api_response = api_instance.shares_get_share_update_added_users(data_view_name, share_id, share_update_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_share_update_added_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share the update is associated with | 
 **share_update_id** | **int**| The id of the share update to view | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Firstname, Surname. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Firstname, Surname. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserDisplayDetails**](PagedResultsUserDisplayDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of the users added to a share as part of a specific update |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this share |  -  |
**404** | The DataView, share or the update couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_share_update_removed_users**
> PagedResultsUserDisplayDetails shares_get_share_update_removed_users(data_view_name, share_id, share_update_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of the users removed from a share as part of a specific update

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share the update is associated with
share_update_id = 56 # int | The id of the share update to view
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Firstname, Surname. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Firstname, Surname. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns the list of the users removed from a share as part of a specific update
        api_response = api_instance.shares_get_share_update_removed_users(data_view_name, share_id, share_update_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_share_update_removed_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share the update is associated with | 
 **share_update_id** | **int**| The id of the share update to view | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Firstname, Surname. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Firstname, Surname. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserDisplayDetails**](PagedResultsUserDisplayDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of the users removed from a share for a specific update |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this share |  -  |
**404** | The DataView, share or the update couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_share_updates**
> PagedResultsShareUpdate shares_get_share_updates(data_view_name, share_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the updates that are associated with a particular share

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share to view
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Timestamp, Notes. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Timestamp, Notes. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns the updates that are associated with a particular share
        api_response = api_instance.shares_get_share_updates(data_view_name, share_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_share_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share to view | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Timestamp, Notes. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Timestamp, Notes. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsShareUpdate**](PagedResultsShareUpdate.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all updates that have happened to the share |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this share |  -  |
**404** | The DataView or share couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_share_users**
> PagedResultsUserDisplayDetails shares_get_share_users(data_view_name, share_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of users that are associated with a particular share

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
share_id = 56 # int | The id of the share to view the users for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns the list of users that are associated with a particular share
        api_response = api_instance.shares_get_share_users(data_view_name, share_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_share_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **share_id** | **int**| The id of the share to view the users for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, EmailAddress. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserDisplayDetails**](PagedResultsUserDisplayDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current list of users that the shareable item is shared with |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this share |  -  |
**404** | The DataView or share couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get_shares**
> PagedResultsShareSummary shares_get_shares(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Gets summary information about each share in the DataView.

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
    api_instance = apteco_api.SharesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are ShareableId, ShareableType, NumberOfUsersSharedWith. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are ShareableId, ShareableType, NumberOfUsersSharedWith. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Requires OrbitAdmin: Gets summary information about each share in the DataView.
        api_response = api_instance.shares_get_shares(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SharesApi->shares_get_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are ShareableId, ShareableType, NumberOfUsersSharedWith. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are ShareableId, ShareableType, NumberOfUsersSharedWith. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsShareSummary**](PagedResultsShareSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all shares |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

