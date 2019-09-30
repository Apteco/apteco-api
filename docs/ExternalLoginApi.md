# apteco_api.ExternalLoginApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_login_assertion_consumer_service**](ExternalLoginApi.md#external_login_assertion_consumer_service) | **POST** /ExternalLogin/AssertionConsumerService | UNDER DEVELOPMENT: Initiate the next phase of the login process that establishes a session.
[**external_login_login**](ExternalLoginApi.md#external_login_login) | **GET** /ExternalLogin/Login | UNDER DEVELOPMENT: Initiate the external login process


# **external_login_assertion_consumer_service**
> external_login_assertion_consumer_service()

UNDER DEVELOPMENT: Initiate the next phase of the login process that establishes a session.

UNDER DEVELOPMENT

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.ExternalLoginApi()

try:
    # UNDER DEVELOPMENT: Initiate the next phase of the login process that establishes a session.
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

UNDER DEVELOPMENT: Initiate the external login process

UNDER DEVELOPMENT

### Example

```python
from __future__ import print_function
import time
import apteco_api
from apteco_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apteco_api.ExternalLoginApi()
return_url = 'return_url_example' # str | The URL to redirect to after the login process has been successful (optional)

try:
    # UNDER DEVELOPMENT: Initiate the external login process
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

