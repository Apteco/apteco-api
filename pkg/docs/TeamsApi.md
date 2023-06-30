# apteco_api.TeamsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_create_team**](TeamsApi.md#teams_create_team) | **POST** /{dataViewName}/Teams | Requires OrbitAdmin: Creates a new team.
[**teams_delete_team**](TeamsApi.md#teams_delete_team) | **DELETE** /{dataViewName}/Teams/{teamId} | Requires OrbitAdmin: Deletes the specified team
[**teams_get_team**](TeamsApi.md#teams_get_team) | **GET** /{dataViewName}/Teams/{teamId} | Requires OrbitAdmin: Returns the detail for a team.
[**teams_get_teams**](TeamsApi.md#teams_get_teams) | **GET** /{dataViewName}/Teams | Returns all teams in the DataView.
[**teams_modify_team**](TeamsApi.md#teams_modify_team) | **PUT** /{dataViewName}/Teams/{teamId} | Requires OrbitAdmin: Modify the specified team


# **teams_create_team**
> TeamSummary teams_create_team(data_view_name, system_name=system_name, team_details=team_details)

Requires OrbitAdmin: Creates a new team.

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
    api_instance = apteco_api.TeamsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | The system name for the team to be associated with. (optional)
team_details = apteco_api.CreateTeamDetails() # CreateTeamDetails | The details for the team to create. (optional)

    try:
        # Requires OrbitAdmin: Creates a new team.
        api_response = api_instance.teams_create_team(data_view_name, system_name=system_name, team_details=team_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| The system name for the team to be associated with. | [optional] 
 **team_details** | [**CreateTeamDetails**](CreateTeamDetails.md)| The details for the team to create. | [optional] 

### Return type

[**TeamSummary**](TeamSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The team was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to create a team.  Only admins can create teams |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_delete_team**
> teams_delete_team(data_view_name, team_id)

Requires OrbitAdmin: Deletes the specified team

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
    api_instance = apteco_api.TeamsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
team_id = 56 # int | The id of the team to delete

    try:
        # Requires OrbitAdmin: Deletes the specified team
        api_instance.teams_delete_team(data_view_name, team_id)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **team_id** | **int**| The id of the team to delete | 

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
**204** | The team was deleted successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete this user.  Only admins can delete teams |  -  |
**404** | The DataView or team couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_team**
> TeamDetail teams_get_team(data_view_name, team_id)

Requires OrbitAdmin: Returns the detail for a team.

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
    api_instance = apteco_api.TeamsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
team_id = 56 # int | The id of the team

    try:
        # Requires OrbitAdmin: Returns the detail for a team.
        api_response = api_instance.teams_get_team(data_view_name, team_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **team_id** | **int**| The id of the team | 

### Return type

[**TeamDetail**](TeamDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The team detail |  -  |
**400** | Bad request |  -  |
**403** | The given session is not allowed to get details for a team.  Only admins can get the details of teams |  -  |
**404** | The DataView or team couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_teams**
> PagedResultsTeamSummary teams_get_teams(data_view_name, system_name=system_name, filter=filter, order_by=order_by, offset=offset, count=count)

Returns all teams in the DataView.

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
    api_instance = apteco_api.TeamsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
system_name = 'system_name_example' # str | If specified, whether to limit to only teams attached to the system name (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Name. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns all teams in the DataView.
        api_response = api_instance.teams_get_teams(data_view_name, system_name=system_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_get_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **system_name** | **str**| If specified, whether to limit to only teams attached to the system name | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Name. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Name. | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsTeamSummary**](PagedResultsTeamSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all teams |  -  |
**400** | Bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_modify_team**
> TeamSummary teams_modify_team(data_view_name, team_id, team_details=team_details)

Requires OrbitAdmin: Modify the specified team

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
    api_instance = apteco_api.TeamsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
team_id = 56 # int | The id of the team
team_details = apteco_api.UpdateTeamDetails() # UpdateTeamDetails | The team to modify (optional)

    try:
        # Requires OrbitAdmin: Modify the specified team
        api_response = api_instance.teams_modify_team(data_view_name, team_id, team_details=team_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_modify_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **team_id** | **int**| The id of the team | 
 **team_details** | [**UpdateTeamDetails**](UpdateTeamDetails.md)| The team to modify | [optional] 

### Return type

[**TeamSummary**](TeamSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The team was modified successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to modify this team.  Only admins can modify teams |  -  |
**404** | The DataView or team couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

