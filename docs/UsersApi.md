# apteco_api.UsersApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_change_user_password**](UsersApi.md#users_change_user_password) | **POST** /{dataViewName}/Users/{username}/ChangePassword | Change the password for the user with the given username
[**users_get_dashboard**](UsersApi.md#users_get_dashboard) | **GET** /{dataViewName}/Users/{username}/Dashboards/{dashboardId} | EXPERIMENTAL: Gets a dashboard in the DataView.
[**users_get_previous_login_history**](UsersApi.md#users_get_previous_login_history) | **GET** /{dataViewName}/Users/{username}/LoginHistory | Gets a list of users last login history
[**users_get_user_audience**](UsersApi.md#users_get_user_audience) | **GET** /{dataViewName}/Users/{username}/Audiences/{audienceId} | Returns the details of a particular audience
[**users_get_user_audiences**](UsersApi.md#users_get_user_audiences) | **GET** /{dataViewName}/Users/{username}/Audiences | Returns the list of audiences associated with the given user
[**users_get_user_collection**](UsersApi.md#users_get_user_collection) | **GET** /{dataViewName}/Users/{username}/Collections/{collectionId} | Returns the details of a particular collection
[**users_get_user_collections**](UsersApi.md#users_get_user_collections) | **GET** /{dataViewName}/Users/{username}/Collections | Returns the list of collections associated with the given user
[**users_get_user_configuration**](UsersApi.md#users_get_user_configuration) | **GET** /{dataViewName}/Users/Configuration | Gets the user configuration
[**users_get_user_details**](UsersApi.md#users_get_user_details) | **GET** /{dataViewName}/Users/{username} | Returns details for the given username
[**users_get_user_details_list**](UsersApi.md#users_get_user_details_list) | **GET** /{dataViewName}/Users | Returns all users in the system.
[**users_modify_user_audiences**](UsersApi.md#users_modify_user_audiences) | **POST** /{dataViewName}/Users/{username}/Audiences/Modify | Updates one or more audiences
[**users_modify_user_collections**](UsersApi.md#users_modify_user_collections) | **POST** /{dataViewName}/Users/{username}/Collections/Modify | Updates one or more collections
[**users_patch_user_collection**](UsersApi.md#users_patch_user_collection) | **PATCH** /{dataViewName}/Users/{username}/Collections/{collectionId} | EXPERIMENTAL: Update some properties of a collection
[**users_update_user_collection**](UsersApi.md#users_update_user_collection) | **PUT** /{dataViewName}/Users/{username}/Collections/{collectionId} | EXPERIMENTAL: Updates a collection
[**users_update_user_details**](UsersApi.md#users_update_user_details) | **POST** /{dataViewName}/Users/{username} | Updates user details for the given username


# **users_change_user_password**
> users_change_user_password(data_view_name, username, change_password_details=change_password_details)

Change the password for the user with the given username

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username of the user to update
change_password_details = apteco_api.ChangePasswordDetails() # ChangePasswordDetails | The user's current and new password (optional)

try:
    # Change the password for the user with the given username
    api_instance.users_change_user_password(data_view_name, username, change_password_details=change_password_details)
except ApiException as e:
    print("Exception when calling UsersApi->users_change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username of the user to update | 
 **change_password_details** | [**ChangePasswordDetails**](ChangePasswordDetails.md)| The user&#39;s current and new password | [optional] 

### Return type

void (empty response body)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user&#39;s password has been successfully updated |  -  |
**400** | Bad request or supplied old password doesn&#39;t match user&#39;s current password |  -  |
**403** | The user doesn&#39;t match the authenticated session or isn&#39;t an admin |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_dashboard**
> DashboardDetail users_get_dashboard(data_view_name, username, dashboard_id)

EXPERIMENTAL: Gets a dashboard in the DataView.

EXPERIMENTAL

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | 
dashboard_id = 56 # int | 

try:
    # EXPERIMENTAL: Gets a dashboard in the DataView.
    api_response = api_instance.users_get_dashboard(data_view_name, username, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**|  | 
 **dashboard_id** | **int**|  | 

### Return type

[**DashboardDetail**](DashboardDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dashboard |  -  |
**400** | A bad request |  -  |
**403** | Forbidden |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_previous_login_history**
> PagedResultsUserLogin users_get_previous_login_history(data_view_name, username, filter=filter, order_by=order_by, offset=offset, count=count)

Gets a list of users last login history

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | 
username = 'username_example' # str | The user to get login history for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, ClientType, SystemName, Timestamp (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, ClientType, SystemName, Timestamp (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Gets a list of users last login history
    api_response = api_instance.users_get_previous_login_history(data_view_name, username, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_previous_login_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**|  | 
 **username** | **str**| The user to get login history for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, ClientType, SystemName, Timestamp | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, ClientType, SystemName, Timestamp | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserLogin**](PagedResultsUserLogin.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the username is valid |  -  |
**400** | The username is not valid or the user id doesn&#39;t match the authenticated session |  -  |
**404** | The DataView or the details associated with the given session id can&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user_audience**
> UserAudienceDetail users_get_user_audience(data_view_name, username, audience_id, include_queries=include_queries, include_brief=include_brief)

Returns the details of a particular audience

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to get the audience for
audience_id = 56 # int | The id of the audience to view
include_queries = True # bool | If specified, whether to include the query definitions for this audience or not.  Defaults to true - to return query definitions (optional)
include_brief = True # bool | If specified, whether to include the brief for this audience or not.  Defaults to true - to return the brief (optional)

try:
    # Returns the details of a particular audience
    api_response = api_instance.users_get_user_audience(data_view_name, username, audience_id, include_queries=include_queries, include_brief=include_brief)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to get the audience for | 
 **audience_id** | **int**| The id of the audience to view | 
 **include_queries** | **bool**| If specified, whether to include the query definitions for this audience or not.  Defaults to true - to return query definitions | [optional] 
 **include_brief** | **bool**| If specified, whether to include the brief for this audience or not.  Defaults to true - to return the brief | [optional] 

### Return type

[**UserAudienceDetail**](UserAudienceDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The audience, username or DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user_audiences**
> PagedResultsUserAudienceSummary users_get_user_audiences(data_view_name, username, include_deleted=include_deleted, apply_pinned_sort=apply_pinned_sort, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of audiences associated with the given user

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to view the audiences for
include_deleted = 'include_deleted_example' # str | If specified, whether to include deleted audiences, not deleted audiences or both.  Defaults to not deleted only (optional)
apply_pinned_sort = True # bool | If specified, whether to ensure that pinned audiences are returned first in the list.  Defaults to true (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, BriefText, Status, SharedToMe, SharedByMe, LastUpdatedUsername, LastUpdatedOn (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, BriefText, Status, SharedToMe, SharedByMe, LastUpdatedUsername, LastUpdatedOn (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of audiences associated with the given user
    api_response = api_instance.users_get_user_audiences(data_view_name, username, include_deleted=include_deleted, apply_pinned_sort=apply_pinned_sort, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_audiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to view the audiences for | 
 **include_deleted** | **str**| If specified, whether to include deleted audiences, not deleted audiences or both.  Defaults to not deleted only | [optional] 
 **apply_pinned_sort** | **bool**| If specified, whether to ensure that pinned audiences are returned first in the list.  Defaults to true | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, BriefText, Status, SharedToMe, SharedByMe, LastUpdatedUsername, LastUpdatedOn | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, BriefText, Status, SharedToMe, SharedByMe, LastUpdatedUsername, LastUpdatedOn | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserAudienceSummary**](PagedResultsUserAudienceSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of the user&#39;s audiences (both owned or shared with) |  -  |
**400** | Bad request |  -  |
**403** | The user doesn&#39;t match the authenticated session or isn&#39;t an admin |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user_collection**
> UserCollectionDetail users_get_user_collection(data_view_name, username, collection_id)

Returns the details of a particular collection

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to get the collection for
collection_id = 56 # int | The id of the collection to view

try:
    # Returns the details of a particular collection
    api_response = api_instance.users_get_user_collection(data_view_name, username, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to get the collection for | 
 **collection_id** | **int**| The id of the collection to view | 

### Return type

[**UserCollectionDetail**](UserCollectionDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The collection details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this collection |  -  |
**404** | The collection, username or DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user_collections**
> PagedResultsUserCollectionSummary users_get_user_collections(data_view_name, username, include_deleted=include_deleted, apply_pinned_sort=apply_pinned_sort, filter=filter, order_by=order_by, offset=offset, count=count)

Returns the list of collections associated with the given user

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to view the collections for
include_deleted = 'include_deleted_example' # str | If specified, whether to include deleted collections, not deleted collections or both.  Defaults to not deleted only (optional)
apply_pinned_sort = True # bool | If specified, whether to ensure that pinned collections are returned first in the list.  Defaults to true (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, Status, DeletionDate, SharedToMe, SharedByMe (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, Status, DeletionDate, SharedToMe, SharedByMe (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns the list of collections associated with the given user
    api_response = api_instance.users_get_user_collections(data_view_name, username, include_deleted=include_deleted, apply_pinned_sort=apply_pinned_sort, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to view the collections for | 
 **include_deleted** | **str**| If specified, whether to include deleted collections, not deleted collections or both.  Defaults to not deleted only | [optional] 
 **apply_pinned_sort** | **bool**| If specified, whether to ensure that pinned collections are returned first in the list.  Defaults to true | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, Status, DeletionDate, SharedToMe, SharedByMe | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, Status, DeletionDate, SharedToMe, SharedByMe | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserCollectionSummary**](PagedResultsUserCollectionSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of the user&#39;s collections (both owned or shared with) |  -  |
**400** | Bad request |  -  |
**403** | The user doesn&#39;t match the authenticated session or isn&#39;t an admin |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user_configuration**
> UserConfigurationDetails users_get_user_configuration(data_view_name)

Gets the user configuration

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.UsersApi()
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on

try:
    # Gets the user configuration
    api_response = api_instance.users_get_user_configuration(data_view_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 

### Return type

[**UserConfigurationDetails**](UserConfigurationDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The valid configuration information |  -  |
**400** | Bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user_details**
> UserDetail users_get_user_details(data_view_name, username)

Returns details for the given username

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to view the details for

try:
    # Returns details for the given username
    api_response = api_instance.users_get_user_details(data_view_name, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to view the details for | 

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
**200** | The user&#39;s details |  -  |
**400** | Bad request |  -  |
**403** | The user doesn&#39;t match the authenticated session or isn&#39;t an admin |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user_details_list**
> PagedResultsUserSummary users_get_user_details_list(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns all users in the system.

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns all users in the system.
    api_response = api_instance.users_get_user_details_list(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_details_list: %s\n" % e)
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

# **users_modify_user_audiences**
> PagedResultsModifyUserAudienceDetailResults users_modify_user_audiences(data_view_name, username, include_queries=include_queries, include_brief=include_brief, updates=updates)

Updates one or more audiences

Requires licence flags [AudienceSelection]

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to update the audiences for
include_queries = True # bool | If specified, whether to include the query definitions for any returned audiences or not.  Defaults to true - to return query definitions (optional)
include_brief = True # bool | If specified, whether to include the brief for any returned audiences or not.  Defaults to true - to return briefs (optional)
updates = apteco_api.ModifyItemsModifyUserAudience() # ModifyItemsModifyUserAudience | The details of the audiences to update.  Any value omitted for a audience will be left unchanged (optional)

try:
    # Updates one or more audiences
    api_response = api_instance.users_modify_user_audiences(data_view_name, username, include_queries=include_queries, include_brief=include_brief, updates=updates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_modify_user_audiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to update the audiences for | 
 **include_queries** | **bool**| If specified, whether to include the query definitions for any returned audiences or not.  Defaults to true - to return query definitions | [optional] 
 **include_brief** | **bool**| If specified, whether to include the brief for any returned audiences or not.  Defaults to true - to return briefs | [optional] 
 **updates** | [**ModifyItemsModifyUserAudience**](ModifyItemsModifyUserAudience.md)| The details of the audiences to update.  Any value omitted for a audience will be left unchanged | [optional] 

### Return type

[**PagedResultsModifyUserAudienceDetailResults**](PagedResultsModifyUserAudienceDetailResults.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries of the updated audiences |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for the specified audiences |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_modify_user_collections**
> PagedResultsModifyUserCollectionDetailResults users_modify_user_collections(data_view_name, username, updates=updates)

Updates one or more collections

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to update the collections for
updates = apteco_api.ModifyItemsModifyUserCollection() # ModifyItemsModifyUserCollection | The details of the collections to update.  Any value omitted for a collection will be left unchanged (optional)

try:
    # Updates one or more collections
    api_response = api_instance.users_modify_user_collections(data_view_name, username, updates=updates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_modify_user_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to update the collections for | 
 **updates** | [**ModifyItemsModifyUserCollection**](ModifyItemsModifyUserCollection.md)| The details of the collections to update.  Any value omitted for a collection will be left unchanged | [optional] 

### Return type

[**PagedResultsModifyUserCollectionDetailResults**](PagedResultsModifyUserCollectionDetailResults.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries of the updated collections |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for the specified collections |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_patch_user_collection**
> UserCollectionDetail users_patch_user_collection(data_view_name, username, collection_id, patch=patch)

EXPERIMENTAL: Update some properties of a collection

EXPERIMENTAL

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to update the collection for
collection_id = 56 # int | The id of the collection to update
patch = None # list[Operation] | The JSON patch specification of how to update some of the properties of the collection (optional)

try:
    # EXPERIMENTAL: Update some properties of a collection
    api_response = api_instance.users_patch_user_collection(data_view_name, username, collection_id, patch=patch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_patch_user_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to update the collection for | 
 **collection_id** | **int**| The id of the collection to update | 
 **patch** | [**list[Operation]**](list.md)| The JSON patch specification of how to update some of the properties of the collection | [optional] 

### Return type

[**UserCollectionDetail**](UserCollectionDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of the updated collection |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to update the details for the specified collection |  -  |
**404** | The collection, username or DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_user_collection**
> UserCollectionDetail users_update_user_collection(data_view_name, username, collection_id, collection_detail=collection_detail)

EXPERIMENTAL: Updates a collection

EXPERIMENTAL

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username to update the collection for
collection_id = 56 # int | The id of the collection to update
collection_detail = apteco_api.UpsertUserCollectionDetail() # UpsertUserCollectionDetail | The new details of the collection (optional)

try:
    # EXPERIMENTAL: Updates a collection
    api_response = api_instance.users_update_user_collection(data_view_name, username, collection_id, collection_detail=collection_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update_user_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username to update the collection for | 
 **collection_id** | **int**| The id of the collection to update | 
 **collection_detail** | [**UpsertUserCollectionDetail**](UpsertUserCollectionDetail.md)| The new details of the collection | [optional] 

### Return type

[**UserCollectionDetail**](UserCollectionDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of the updated collection |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to update the details for the specified collection |  -  |
**404** | The collection, username or DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_user_details**
> UserSummary users_update_user_details(data_view_name, username, update_user_details=update_user_details)

Updates user details for the given username

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
api_instance = apteco_api.UsersApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username of the user to update
update_user_details = apteco_api.UpdateUserDetails() # UpdateUserDetails | The details to update the user with (optional)

try:
    # Updates user details for the given username
    api_response = api_instance.users_update_user_details(data_view_name, username, update_user_details=update_user_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update_user_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username of the user to update | 
 **update_user_details** | [**UpdateUserDetails**](UpdateUserDetails.md)| The details to update the user with | [optional] 

### Return type

[**UserSummary**](UserSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user&#39;s details have been successfully updated |  -  |
**400** | Bad request |  -  |
**403** | The user doesn&#39;t match the authenticated session or isn&#39;t an admin |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

