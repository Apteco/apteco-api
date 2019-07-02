# apteco_api.SessionsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessions_convert_session_to_access_token**](SessionsApi.md#sessions_convert_session_to_access_token) | **POST** /{dataViewName}/Sessions/ConvertSession | Creates an API session token from a traditional FastStats session id
[**sessions_create_login_parameters**](SessionsApi.md#sessions_create_login_parameters) | **POST** /{dataViewName}/Sessions/LoginParameters | Creates a new set of parameters to use when creating a new session via the salted login method.
[**sessions_create_session_salted**](SessionsApi.md#sessions_create_session_salted) | **POST** /{dataViewName}/Sessions/SaltedLogin | Creates a session to use for other API requests
[**sessions_create_session_simple**](SessionsApi.md#sessions_create_session_simple) | **POST** /{dataViewName}/Sessions/SimpleLogin | Creates a session to use for other API requests
[**sessions_get_session_details**](SessionsApi.md#sessions_get_session_details) | **GET** /{dataViewName}/Sessions/{sessionId} | Gets some simple user details for the given session id
[**sessions_get_session_details_list**](SessionsApi.md#sessions_get_session_details_list) | **GET** /{dataViewName}/Sessions | Requires OrbitAdmin: Gets some simple user details for all currently valid sessions.
[**sessions_logout_session**](SessionsApi.md#sessions_logout_session) | **DELETE** /{dataViewName}/Sessions/{sessionId} | Logs out the specified session


# **sessions_convert_session_to_access_token**
> SessionDetails sessions_convert_session_to_access_token(data_view_name, session_id)

Creates an API session token from a traditional FastStats session id

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.SessionsApi()
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
session_id = 'session_id_example' # str | An existing valid session id

try:
    # Creates an API session token from a traditional FastStats session id
    api_response = api_instance.sessions_convert_session_to_access_token(data_view_name, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_convert_session_to_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **session_id** | **str**| An existing valid session id | 

### Return type

[**SessionDetails**](SessionDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Session created |  -  |
**400** | Bad request |  -  |
**401** | Bad login credentials |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_create_login_parameters**
> CreateSessionParameters sessions_create_login_parameters(data_view_name, user_name=user_name)

Creates a new set of parameters to use when creating a new session via the salted login method.

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.SessionsApi()
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
user_name = 'user_name_example' # str | The name of the user to create the session for (optional)

try:
    # Creates a new set of parameters to use when creating a new session via the salted login method.
    api_response = api_instance.sessions_create_login_parameters(data_view_name, user_name=user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_create_login_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **user_name** | **str**| The name of the user to create the session for | [optional] 

### Return type

[**CreateSessionParameters**](CreateSessionParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the login salt has been created successfully |  -  |
**400** | The DataView name or username are not valid |  -  |
**404** | The DataView or username aren&#39;t recognised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_create_session_salted**
> SessionDetails sessions_create_session_salted(data_view_name, username, login_salt, password_hash)

Creates a session to use for other API requests

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.SessionsApi()
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username of the user
login_salt = 'login_salt_example' # str | The salt to use when loging in
password_hash = 'password_hash_example' # str | The password hash for the user.  Depending on the settings for the user this will be generated in a complicated way

try:
    # Creates a session to use for other API requests
    api_response = api_instance.sessions_create_session_salted(data_view_name, username, login_salt, password_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_create_session_salted: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username of the user | 
 **login_salt** | **str**| The salt to use when loging in | 
 **password_hash** | **str**| The password hash for the user.  Depending on the settings for the user this will be generated in a complicated way | 

### Return type

[**SessionDetails**](SessionDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Session created |  -  |
**400** | Bad request |  -  |
**401** | Bad login credentials |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_create_session_simple**
> SessionDetails sessions_create_session_simple(data_view_name, user_login, password)

Creates a session to use for other API requests

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.SessionsApi()
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
user_login = 'user_login_example' # str | The piece of information used to identify the user.  This always be a username, and  if the option has been configured an email address can also be used.  Note that a  user can only successfully log on with their email address if no other user has  the same email address registered in the system.
password = 'password_example' # str | The password for the user.

try:
    # Creates a session to use for other API requests
    api_response = api_instance.sessions_create_session_simple(data_view_name, user_login, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_create_session_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **user_login** | **str**| The piece of information used to identify the user.  This always be a username, and  if the option has been configured an email address can also be used.  Note that a  user can only successfully log on with their email address if no other user has  the same email address registered in the system. | 
 **password** | **str**| The password for the user. | 

### Return type

[**SessionDetails**](SessionDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Session created |  -  |
**400** | Bad request |  -  |
**401** | Bad login credentials |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_get_session_details**
> SessionAndUserDetails sessions_get_session_details(data_view_name, session_id)

Gets some simple user details for the given session id

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
api_instance = apteco_api.SessionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
session_id = 'session_id_example' # str | The session id to look up

try:
    # Gets some simple user details for the given session id
    api_response = api_instance.sessions_get_session_details(data_view_name, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_get_session_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **session_id** | **str**| The session id to look up | 

### Return type

[**SessionAndUserDetails**](SessionAndUserDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the session id is valid |  -  |
**400** | The session id is not valid or the sessionId doesn&#39;t match the authenticated session |  -  |
**404** | The DataView or the details associated with the given session id can&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_get_session_details_list**
> PagedResultsSessionAndUserDetails sessions_get_session_details_list(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Gets some simple user details for all currently valid sessions.

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
api_instance = apteco_api.SessionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Gets some simple user details for all currently valid sessions.
    api_response = api_instance.sessions_get_session_details_list(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_get_session_details_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsSessionAndUserDetails**](PagedResultsSessionAndUserDetails.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all currently valid sessions |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_logout_session**
> sessions_logout_session(data_view_name, session_id)

Logs out the specified session

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
api_instance = apteco_api.SessionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
session_id = 'session_id_example' # str | The session id to log out from

try:
    # Logs out the specified session
    api_instance.sessions_logout_session(data_view_name, session_id)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_logout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **session_id** | **str**| The session id to log out from | 

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
**204** | The session was successfully invalidated |  -  |
**400** | The session id is not valid or the sessionId doesn&#39;t match the authenticated session |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

