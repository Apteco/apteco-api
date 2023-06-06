# apteco_api.UserRegistrationRequestsApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_registration_requests_confirm_registration_request**](UserRegistrationRequestsApi.md#user_registration_requests_confirm_registration_request) | **POST** /{dataViewName}/UserRegistrationRequests/{token} | Confirms a given user registration request and creates the user
[**user_registration_requests_create_registration_request**](UserRegistrationRequestsApi.md#user_registration_requests_create_registration_request) | **POST** /{dataViewName}/UserRegistrationRequests | Creates a new user registration requests, which will check the sign-up details and then issue a confirmation notification
[**user_registration_requests_get_registration_request**](UserRegistrationRequestsApi.md#user_registration_requests_get_registration_request) | **GET** /{dataViewName}/UserRegistrationRequests/{token} | Requires OrbitAdmin: Returns details for a given user registration request
[**user_registration_requests_get_registration_requests**](UserRegistrationRequestsApi.md#user_registration_requests_get_registration_requests) | **GET** /{dataViewName}/UserRegistrationRequests | Requires OrbitAdmin: Returns all the current user regisration requests in the system.


# **user_registration_requests_confirm_registration_request**
> UserSummary user_registration_requests_confirm_registration_request(data_view_name, token)

Confirms a given user registration request and creates the user

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with apteco_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.UserRegistrationRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
token = 'token_example' # str | The token of the request

    try:
        # Confirms a given user registration request and creates the user
        api_response = api_instance.user_registration_requests_confirm_registration_request(data_view_name, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRegistrationRequestsApi->user_registration_requests_confirm_registration_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **token** | **str**| The token of the request | 

### Return type

[**UserSummary**](UserSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The details of the created user |  -  |
**400** | Bad request |  -  |
**404** | The DataView or registration request couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_registration_requests_create_registration_request**
> UserRegistrationRequestDetail user_registration_requests_create_registration_request(data_view_name, create_user_registration_request=create_user_registration_request)

Creates a new user registration requests, which will check the sign-up details and then issue a confirmation notification

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with apteco_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.UserRegistrationRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
create_user_registration_request = apteco_api.CreateUserRegistrationRequest() # CreateUserRegistrationRequest | The details needed to create the registration request (optional)

    try:
        # Creates a new user registration requests, which will check the sign-up details and then issue a confirmation notification
        api_response = api_instance.user_registration_requests_create_registration_request(data_view_name, create_user_registration_request=create_user_registration_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRegistrationRequestsApi->user_registration_requests_create_registration_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **create_user_registration_request** | [**CreateUserRegistrationRequest**](CreateUserRegistrationRequest.md)| The details needed to create the registration request | [optional] 

### Return type

[**UserRegistrationRequestDetail**](UserRegistrationRequestDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created request details |  -  |
**400** | Bad request or registering new users is not allowed in this system |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_registration_requests_get_registration_request**
> UserRegistrationRequestDetail user_registration_requests_get_registration_request(data_view_name, token)

Requires OrbitAdmin: Returns details for a given user registration request

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

# Defining host is optional and default to https://example.com/OrbitAPI
configuration.host = "https://example.com/OrbitAPI"
# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.UserRegistrationRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
token = 'token_example' # str | The token of the request

    try:
        # Requires OrbitAdmin: Returns details for a given user registration request
        api_response = api_instance.user_registration_requests_get_registration_request(data_view_name, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRegistrationRequestsApi->user_registration_requests_get_registration_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **token** | **str**| The token of the request | 

### Return type

[**UserRegistrationRequestDetail**](UserRegistrationRequestDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the given user registration request |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView or registration request couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_registration_requests_get_registration_requests**
> PagedResultsUserRegistrationRequestSummary user_registration_requests_get_registration_requests(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns all the current user regisration requests in the system.

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

# Defining host is optional and default to https://example.com/OrbitAPI
configuration.host = "https://example.com/OrbitAPI"
# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.UserRegistrationRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, Firstname, Surname, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, Firstname, Surname, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Requires OrbitAdmin: Returns all the current user regisration requests in the system.
        api_response = api_instance.user_registration_requests_get_registration_requests(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRegistrationRequestsApi->user_registration_requests_get_registration_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, Firstname, Surname, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, Firstname, Surname, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsUserRegistrationRequestSummary**](PagedResultsUserRegistrationRequestSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all user registration requests |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

