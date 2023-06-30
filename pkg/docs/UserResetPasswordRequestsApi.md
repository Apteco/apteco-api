# apteco_api.UserResetPasswordRequestsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_reset_password_requests_confirm_reset_password_request**](UserResetPasswordRequestsApi.md#user_reset_password_requests_confirm_reset_password_request) | **POST** /{dataViewName}/UserResetPasswordRequests/{token} | Confirms a given reset password request and changes the password
[**user_reset_password_requests_create_reset_password_request**](UserResetPasswordRequestsApi.md#user_reset_password_requests_create_reset_password_request) | **POST** /{dataViewName}/UserResetPasswordRequests | Creates a new reset password requests, which will check that the provided email address exists and then issue a confirmation notification
[**user_reset_password_requests_get_reset_password_request**](UserResetPasswordRequestsApi.md#user_reset_password_requests_get_reset_password_request) | **GET** /{dataViewName}/UserResetPasswordRequests/{token} | Requires OrbitAdmin: Returns details for a given reset password request
[**user_reset_password_requests_get_reset_password_requests**](UserResetPasswordRequestsApi.md#user_reset_password_requests_get_reset_password_requests) | **GET** /{dataViewName}/UserResetPasswordRequests | Requires OrbitAdmin: Returns all the current reset password requests in the system.


# **user_reset_password_requests_confirm_reset_password_request**
> user_reset_password_requests_confirm_reset_password_request(data_view_name, token, confirm_reset_password_request=confirm_reset_password_request)

Confirms a given reset password request and changes the password

### Example

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


# Enter a context with an instance of the API client
with apteco_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.UserResetPasswordRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
token = 'token_example' # str | The token of the request
confirm_reset_password_request = apteco_api.ConfirmResetPasswordRequest() # ConfirmResetPasswordRequest | The details needed to confirm the reset password request (optional)

    try:
        # Confirms a given reset password request and changes the password
        api_instance.user_reset_password_requests_confirm_reset_password_request(data_view_name, token, confirm_reset_password_request=confirm_reset_password_request)
    except ApiException as e:
        print("Exception when calling UserResetPasswordRequestsApi->user_reset_password_requests_confirm_reset_password_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **token** | **str**| The token of the request | 
 **confirm_reset_password_request** | [**ConfirmResetPasswordRequest**](ConfirmResetPasswordRequest.md)| The details needed to confirm the reset password request | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The user&#39;s password has been successfully reset |  -  |
**400** | Bad request, or the email address provided doesn&#39;t match the one used to create the token |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_reset_password_requests_create_reset_password_request**
> ResetPasswordRequestDetail user_reset_password_requests_create_reset_password_request(data_view_name, create_reset_password_request=create_reset_password_request)

Creates a new reset password requests, which will check that the provided email address exists and then issue a confirmation notification

### Example

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


# Enter a context with an instance of the API client
with apteco_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.UserResetPasswordRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
create_reset_password_request = apteco_api.CreateResetPasswordRequest() # CreateResetPasswordRequest | The details needed to create the reset password request (optional)

    try:
        # Creates a new reset password requests, which will check that the provided email address exists and then issue a confirmation notification
        api_response = api_instance.user_reset_password_requests_create_reset_password_request(data_view_name, create_reset_password_request=create_reset_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserResetPasswordRequestsApi->user_reset_password_requests_create_reset_password_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **create_reset_password_request** | [**CreateResetPasswordRequest**](CreateResetPasswordRequest.md)| The details needed to create the reset password request | [optional] 

### Return type

[**ResetPasswordRequestDetail**](ResetPasswordRequestDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created request details |  -  |
**400** | Bad request or resetting passwords is not allowed in this system |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_reset_password_requests_get_reset_password_request**
> ResetPasswordRequestDetail user_reset_password_requests_get_reset_password_request(data_view_name, token)

Requires OrbitAdmin: Returns details for a given reset password request

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
    api_instance = apteco_api.UserResetPasswordRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
token = 'token_example' # str | The token of the request

    try:
        # Requires OrbitAdmin: Returns details for a given reset password request
        api_response = api_instance.user_reset_password_requests_get_reset_password_request(data_view_name, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserResetPasswordRequestsApi->user_reset_password_requests_get_reset_password_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **token** | **str**| The token of the request | 

### Return type

[**ResetPasswordRequestDetail**](ResetPasswordRequestDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the given reset password request |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView or reset password request couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_reset_password_requests_get_reset_password_requests**
> PagedResultsUserRegistrationRequestSummary user_reset_password_requests_get_reset_password_requests(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Returns all the current reset password requests in the system.

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
    api_instance = apteco_api.UserResetPasswordRequestsApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate. (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate. (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Requires OrbitAdmin: Returns all the current reset password requests in the system.
        api_response = api_instance.user_reset_password_requests_get_reset_password_requests(data_view_name, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserResetPasswordRequestsApi->user_reset_password_requests_get_reset_password_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate. | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate. | [optional] 
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
**200** | The list of allreset password requests |  -  |
**400** | Bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

