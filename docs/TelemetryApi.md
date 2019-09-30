# apteco_api.TelemetryApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**telemetry_create_telemetry_session**](TelemetryApi.md#telemetry_create_telemetry_session) | **POST** /{dataViewName}/Telemetry/States/{stateId}/Sessions/{sessionId} | Creates a new telemetry session from the given details
[**telemetry_create_telemetry_state**](TelemetryApi.md#telemetry_create_telemetry_state) | **POST** /{dataViewName}/Telemetry/States | Creates a new telemetry state from the given details
[**telemetry_get_telemetry_session**](TelemetryApi.md#telemetry_get_telemetry_session) | **GET** /{dataViewName}/Telemetry/States/{stateId}/Sessions/{sessionId} | Returns the details of a particular telemetry session
[**telemetry_get_telemetry_state**](TelemetryApi.md#telemetry_get_telemetry_state) | **GET** /{dataViewName}/Telemetry/States/{stateId} | Returns the details of a particular telemetry state
[**telemetry_get_telemetry_state_for_user**](TelemetryApi.md#telemetry_get_telemetry_state_for_user) | **GET** /{dataViewName}/Telemetry/States/ForUser/{Username} | Returns the details of a given user&#39;s telemetry state
[**telemetry_update_telemetry_session**](TelemetryApi.md#telemetry_update_telemetry_session) | **POST** /{dataViewName}/Telemetry/States/{stateId}/Sessions/{sessionId}/Update | Update a particular telemetry session from the given details
[**telemetry_update_telemetry_state**](TelemetryApi.md#telemetry_update_telemetry_state) | **POST** /{dataViewName}/Telemetry/States/{stateId}/Update | Updates a particular telemetry state from the given details


# **telemetry_create_telemetry_session**
> TelemetrySession telemetry_create_telemetry_session(data_view_name, state_id, session_id, create_telemetry_session_details=create_telemetry_session_details)

Creates a new telemetry session from the given details

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
api_instance = apteco_api.TelemetryApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
state_id = 'state_id_example' # str | The id of the telemetry state the session belongs to
session_id = 'session_id_example' # str | The id of the telemetry session
create_telemetry_session_details = apteco_api.CreateTelemetrySessionDetails() # CreateTelemetrySessionDetails | The details of the telemetry session to create (optional)

try:
    # Creates a new telemetry session from the given details
    api_response = api_instance.telemetry_create_telemetry_session(data_view_name, state_id, session_id, create_telemetry_session_details=create_telemetry_session_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->telemetry_create_telemetry_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **state_id** | **str**| The id of the telemetry state the session belongs to | 
 **session_id** | **str**| The id of the telemetry session | 
 **create_telemetry_session_details** | [**CreateTelemetrySessionDetails**](CreateTelemetrySessionDetails.md)| The details of the telemetry session to create | [optional] 

### Return type

[**TelemetrySession**](TelemetrySession.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The telemetry session was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to create this telemetry session |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telemetry_create_telemetry_state**
> TelemetryState telemetry_create_telemetry_state(data_view_name, create_telemetry_state_details=create_telemetry_state_details)

Creates a new telemetry state from the given details

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
api_instance = apteco_api.TelemetryApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
create_telemetry_state_details = apteco_api.CreateTelemetryStateDetails() # CreateTelemetryStateDetails | The details of the telemetry state to create (optional)

try:
    # Creates a new telemetry state from the given details
    api_response = api_instance.telemetry_create_telemetry_state(data_view_name, create_telemetry_state_details=create_telemetry_state_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->telemetry_create_telemetry_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **create_telemetry_state_details** | [**CreateTelemetryStateDetails**](CreateTelemetryStateDetails.md)| The details of the telemetry state to create | [optional] 

### Return type

[**TelemetryState**](TelemetryState.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The telemetry state was created successfully |  -  |
**400** | A bad request |  -  |
**403** | The session is not allowed to create this telemetry state |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telemetry_get_telemetry_session**
> TelemetrySession telemetry_get_telemetry_session(data_view_name, state_id, session_id)

Returns the details of a particular telemetry session

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
api_instance = apteco_api.TelemetryApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
state_id = 'state_id_example' # str | The id of the telemetry state the session belongs to
session_id = 'session_id_example' # str | The id of the telemetry session

try:
    # Returns the details of a particular telemetry session
    api_response = api_instance.telemetry_get_telemetry_session(data_view_name, state_id, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->telemetry_get_telemetry_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **state_id** | **str**| The id of the telemetry state the session belongs to | 
 **session_id** | **str**| The id of the telemetry session | 

### Return type

[**TelemetrySession**](TelemetrySession.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The telemetry session |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see this telemetry session |  -  |
**404** | The DataView or telemetry session couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telemetry_get_telemetry_state**
> TelemetryState telemetry_get_telemetry_state(data_view_name, state_id)

Returns the details of a particular telemetry state

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
api_instance = apteco_api.TelemetryApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
state_id = 'state_id_example' # str | The id of the telemetry state to return

try:
    # Returns the details of a particular telemetry state
    api_response = api_instance.telemetry_get_telemetry_state(data_view_name, state_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->telemetry_get_telemetry_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **state_id** | **str**| The id of the telemetry state to return | 

### Return type

[**TelemetryState**](TelemetryState.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The telemetry state |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see this telemetry state |  -  |
**404** | The DataView or telemetry state couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telemetry_get_telemetry_state_for_user**
> TelemetryState telemetry_get_telemetry_state_for_user(data_view_name, username)

Returns the details of a given user's telemetry state

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
api_instance = apteco_api.TelemetryApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
username = 'username_example' # str | The username of the telemetry state to return

try:
    # Returns the details of a given user's telemetry state
    api_response = api_instance.telemetry_get_telemetry_state_for_user(data_view_name, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->telemetry_get_telemetry_state_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **username** | **str**| The username of the telemetry state to return | 

### Return type

[**TelemetryState**](TelemetryState.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The telemetry state |  -  |
**400** | A bad request |  -  |
**403** | The given session or user is not allowed to see this telemetry state |  -  |
**404** | The DataView or telemetry state couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telemetry_update_telemetry_session**
> TelemetrySession telemetry_update_telemetry_session(data_view_name, state_id, session_id, update_telemetry_session_details=update_telemetry_session_details)

Update a particular telemetry session from the given details

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
api_instance = apteco_api.TelemetryApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
state_id = 'state_id_example' # str | The id of the telemetry state the session belongs to
session_id = 'session_id_example' # str | The id of the telemetry session
update_telemetry_session_details = apteco_api.UpdateTelemetrySessionDetails() # UpdateTelemetrySessionDetails | The details of the telemetry session to update (optional)

try:
    # Update a particular telemetry session from the given details
    api_response = api_instance.telemetry_update_telemetry_session(data_view_name, state_id, session_id, update_telemetry_session_details=update_telemetry_session_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->telemetry_update_telemetry_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **state_id** | **str**| The id of the telemetry state the session belongs to | 
 **session_id** | **str**| The id of the telemetry session | 
 **update_telemetry_session_details** | [**UpdateTelemetrySessionDetails**](UpdateTelemetrySessionDetails.md)| The details of the telemetry session to update | [optional] 

### Return type

[**TelemetrySession**](TelemetrySession.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The telemetry session was updated successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to update this telemetry session |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telemetry_update_telemetry_state**
> TelemetryState telemetry_update_telemetry_state(data_view_name, state_id, update_telemetry_state_details=update_telemetry_state_details)

Updates a particular telemetry state from the given details

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
api_instance = apteco_api.TelemetryApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
state_id = 'state_id_example' # str | The id of the telemetry state to update
update_telemetry_state_details = apteco_api.UpdateTelemetryStateDetails() # UpdateTelemetryStateDetails | The details of the telemetry state to update (optional)

try:
    # Updates a particular telemetry state from the given details
    api_response = api_instance.telemetry_update_telemetry_state(data_view_name, state_id, update_telemetry_state_details=update_telemetry_state_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->telemetry_update_telemetry_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **state_id** | **str**| The id of the telemetry state to update | 
 **update_telemetry_state_details** | [**UpdateTelemetryStateDetails**](UpdateTelemetryStateDetails.md)| The details of the telemetry state to update | [optional] 

### Return type

[**TelemetryState**](TelemetryState.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The telemetry state was updated successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to update this telemetry state |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

