# apteco_api.ExternalLoginApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_login_assertion_consumer_service**](ExternalLoginApi.md#external_login_assertion_consumer_service) | **POST** /ExternalLogin/AssertionConsumerService | Initiate the next phase of the login process that establishes a session.
[**external_login_login**](ExternalLoginApi.md#external_login_login) | **GET** /ExternalLogin/Login | Initiate the external login process
[**external_login_single_logout_service**](ExternalLoginApi.md#external_login_single_logout_service) | **GET** /ExternalLogin/SingleLogoutService | Initiate a logout from the application.


# **external_login_assertion_consumer_service**
> external_login_assertion_consumer_service()

Initiate the next phase of the login process that establishes a session.

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
    api_instance = apteco_api.ExternalLoginApi(api_client)
    
    try:
        # Initiate the next phase of the login process that establishes a session.
        api_instance.external_login_assertion_consumer_service()
    except ApiException as e:
        print("Exception when calling ExternalLoginApi->external_login_assertion_consumer_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**302** | A redirect to the application to process the created login token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_login_login**
> external_login_login(return_url=return_url)

Initiate the external login process

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
    api_instance = apteco_api.ExternalLoginApi(api_client)
    return_url = 'return_url_example' # str | The URL to redirect to after the login process has been successful (optional)

    try:
        # Initiate the external login process
        api_instance.external_login_login(return_url=return_url)
    except ApiException as e:
        print("Exception when calling ExternalLoginApi->external_login_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_url** | **str**| The URL to redirect to after the login process has been successful | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**302** | A redirect to the next phase of the login process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_login_single_logout_service**
> external_login_single_logout_service(saml_request=saml_request)

Initiate a logout from the application.

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
    api_instance = apteco_api.ExternalLoginApi(api_client)
    saml_request = 'saml_request_example' # str | The SAML details (optional)

    try:
        # Initiate a logout from the application.
        api_instance.external_login_single_logout_service(saml_request=saml_request)
    except ApiException as e:
        print("Exception when calling ExternalLoginApi->external_login_single_logout_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_request** | **str**| The SAML details | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**302** | A redirect to the application to perform the logout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

