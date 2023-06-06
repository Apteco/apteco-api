# apteco_api.AudiencesApi

All URIs are relative to *https://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audiences_calculate_audience_data_licensing_sync**](AudiencesApi.md#audiences_calculate_audience_data_licensing_sync) | **POST** /{dataViewName}/Audiences/{audienceId}/DataLicensingSync | Get data licensing information for the latest version of this audience
[**audiences_calculate_audience_latest_update_sync**](AudiencesApi.md#audiences_calculate_audience_latest_update_sync) | **POST** /{dataViewName}/Audiences/{audienceId}/CalculateSync | Calculate counts against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to produce the end result
[**audiences_cancel_calculate_audience_data_licensing_job**](AudiencesApi.md#audiences_cancel_calculate_audience_data_licensing_job) | **DELETE** /{dataViewName}/Audiences/{audienceId}/DataLicensingJobs/{jobId} | Cancel a running data licensing job
[**audiences_cancel_calculate_audience_job**](AudiencesApi.md#audiences_cancel_calculate_audience_job) | **DELETE** /{dataViewName}/Audiences/{audienceId}/CalculateJobs/{jobId} | Cancel a running calculate job
[**audiences_cancel_check_audience_job**](AudiencesApi.md#audiences_cancel_check_audience_job) | **DELETE** /{dataViewName}/Audiences/{audienceId}/CheckJobs/{jobId} | Cancel a running check job
[**audiences_cancel_export_audience_job**](AudiencesApi.md#audiences_cancel_export_audience_job) | **DELETE** /{dataViewName}/Audiences/{audienceId}/ExportJobs/{jobId} | Cancel a running export job
[**audiences_check_audience_latest_update_sync**](AudiencesApi.md#audiences_check_audience_latest_update_sync) | **POST** /{dataViewName}/Audiences/{audienceId}/CheckSync | Calculate check statistics against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to analyse and the specified dimensions will be used to perform the analysis.
[**audiences_create_audience**](AudiencesApi.md#audiences_create_audience) | **POST** /{dataViewName}/Audiences | Creates a new audience from the given details for the logged in user.
[**audiences_create_audience_hit_for_audience**](AudiencesApi.md#audiences_create_audience_hit_for_audience) | **POST** /{dataViewName}/Audiences/{audienceId}/Hits | Register a hit (view) for the given audience
[**audiences_create_audience_update**](AudiencesApi.md#audiences_create_audience_update) | **POST** /{dataViewName}/Audiences/{audienceId}/Updates | Updates the details of a particular audience.  If you don&#39;t have an id for the  audience then POST to the /Audiences URL to create a new audience.
[**audiences_create_calculate_audience_data_licensing_job**](AudiencesApi.md#audiences_create_calculate_audience_data_licensing_job) | **POST** /{dataViewName}/Audiences/{audienceId}/DataLicensingJobs | Create a new job to get data licensing information for the latest version of this audience
[**audiences_create_calculate_audience_job_for_latest_update**](AudiencesApi.md#audiences_create_calculate_audience_job_for_latest_update) | **POST** /{dataViewName}/Audiences/{audienceId}/CalculateJobs | Create a new job to calculate counts against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to produce the end result
[**audiences_create_check_audience_job_for_latest_update**](AudiencesApi.md#audiences_create_check_audience_job_for_latest_update) | **POST** /{dataViewName}/Audiences/{audienceId}/CheckJobs | Create a new job to calculate check statistics against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to analyse and the specified dimensions will be used to perform the analysis.
[**audiences_create_export_audience_job_for_latest_update**](AudiencesApi.md#audiences_create_export_audience_job_for_latest_update) | **POST** /{dataViewName}/Audiences/{audienceId}/ExportJobs | Create a new job to export data from the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to export and the specified columns will be used to export the data, to a file  and/or as a sample within the body of the result
[**audiences_delete_audience**](AudiencesApi.md#audiences_delete_audience) | **DELETE** /{dataViewName}/Audiences/{audienceId} | Deletes the specified audience
[**audiences_export_audience_latest_update_sync**](AudiencesApi.md#audiences_export_audience_latest_update_sync) | **POST** /{dataViewName}/Audiences/{audienceId}/ExportSync | Create a new job to export data from the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to export and the specified columns will be used to export the data, to a file  and/or as a sample within the body of the result
[**audiences_get_audience**](AudiencesApi.md#audiences_get_audience) | **GET** /{dataViewName}/Audiences/{audienceId} | Returns the details of a particular audience
[**audiences_get_audience_hit_for_audience**](AudiencesApi.md#audiences_get_audience_hit_for_audience) | **GET** /{dataViewName}/Audiences/{audienceId}/Hits/{audienceHitId} | Returns details for a given audience hit for this audience
[**audiences_get_audience_hits_for_audience**](AudiencesApi.md#audiences_get_audience_hits_for_audience) | **GET** /{dataViewName}/Audiences/{audienceId}/Hits | Returns a summary of the hits for this audience - i.e. information about when users have viewed the audience.
[**audiences_get_audience_latest_native_for_nett_query**](AudiencesApi.md#audiences_get_audience_latest_native_for_nett_query) | **GET** /{dataViewName}/Audiences/{audienceId}/Native/Nett | Returns native XML (i.e. for use with other FastStats applications) for the Nett query of the latest update for a particular audience
[**audiences_get_audience_result**](AudiencesApi.md#audiences_get_audience_result) | **GET** /{dataViewName}/Audiences/{audienceId}/Results/{audienceResultId} | Returns details of a particular result for a particular audience
[**audiences_get_audience_results**](AudiencesApi.md#audiences_get_audience_results) | **GET** /{dataViewName}/Audiences/{audienceId}/Results | Returns a summary of the results for a particular audience
[**audiences_get_audience_update**](AudiencesApi.md#audiences_get_audience_update) | **GET** /{dataViewName}/Audiences/{audienceId}/Updates/{audienceUpdateId} | Returns details of an update for a particular audience
[**audiences_get_audience_updates**](AudiencesApi.md#audiences_get_audience_updates) | **GET** /{dataViewName}/Audiences/{audienceId}/Updates | Returns a summary of the updates to a particular audience
[**audiences_get_audiences**](AudiencesApi.md#audiences_get_audiences) | **GET** /{dataViewName}/Audiences | Requires OrbitAdmin: Gets summary information about each audience in the DataView.
[**audiences_get_calculate_audience_data_licensing_job**](AudiencesApi.md#audiences_get_calculate_audience_data_licensing_job) | **POST** /{dataViewName}/Audiences/{audienceId}/DataLicensingJobs/{jobId} | Get the status of a running calculate job
[**audiences_get_calculate_audience_job**](AudiencesApi.md#audiences_get_calculate_audience_job) | **GET** /{dataViewName}/Audiences/{audienceId}/CalculateJobs/{jobId} | Get the status of a running calculate job
[**audiences_get_check_audience_job**](AudiencesApi.md#audiences_get_check_audience_job) | **GET** /{dataViewName}/Audiences/{audienceId}/CheckJobs/{jobId} | Get the status of a running check job
[**audiences_get_export_audience_job**](AudiencesApi.md#audiences_get_export_audience_job) | **GET** /{dataViewName}/Audiences/{audienceId}/ExportJobs/{jobId} | Get the status of a running export job
[**audiences_transfer_audience_ownership**](AudiencesApi.md#audiences_transfer_audience_ownership) | **POST** /{dataViewName}/Audiences/{audienceId}/TransferOwnership | Transfer ownership of an audience from the current user to a new owner


# **audiences_calculate_audience_data_licensing_sync**
> LicensingInfo audiences_calculate_audience_data_licensing_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, data_licensing_detail=data_licensing_detail)

Get data licensing information for the latest version of this audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to calculate the result for
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
data_licensing_detail = apteco_api.DataLicensingDetail() # DataLicensingDetail | The details required to get data licensing information for an audience (optional)

    try:
        # Get data licensing information for the latest version of this audience
        api_response = api_instance.audiences_calculate_audience_data_licensing_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, data_licensing_detail=data_licensing_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_calculate_audience_data_licensing_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to calculate the result for | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service&#39;s configuration | [optional] 
 **data_licensing_detail** | [**DataLicensingDetail**](DataLicensingDetail.md)| The details required to get data licensing information for an audience | [optional] 

### Return type

[**LicensingInfo**](LicensingInfo.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculation completed successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get data licensing information. |  -  |
**404** | The audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_calculate_audience_latest_update_sync**
> AudienceResultDetail audiences_calculate_audience_latest_update_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, calculate_audience_details=calculate_audience_details)

Calculate counts against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to produce the end result

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to calculate the result for.
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
calculate_audience_details = apteco_api.CalculateAudienceDetails() # CalculateAudienceDetails | The details for calculating this audience. (optional)

    try:
        # Calculate counts against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to produce the end result
        api_response = api_instance.audiences_calculate_audience_latest_update_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, calculate_audience_details=calculate_audience_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_calculate_audience_latest_update_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to calculate the result for. | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service&#39;s configuration | [optional] 
 **calculate_audience_details** | [**CalculateAudienceDetails**](CalculateAudienceDetails.md)| The details for calculating this audience. | [optional] 

### Return type

[**AudienceResultDetail**](AudienceResultDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The calculation completed successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to count this audience. |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_cancel_calculate_audience_data_licensing_job**
> audiences_cancel_calculate_audience_data_licensing_job(data_view_name, audience_id, job_id)

Cancel a running data licensing job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the data licensing job is running for.
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running data licensing job
        api_instance.audiences_cancel_calculate_audience_data_licensing_job(data_view_name, audience_id, job_id)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_cancel_calculate_audience_data_licensing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the data licensing job is running for. | 
 **job_id** | **int**| The id of the job to cancel | 

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
**204** | The job was cancelled successful |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to cancel the data licensing job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_cancel_calculate_audience_job**
> audiences_cancel_calculate_audience_job(data_view_name, audience_id, job_id)

Cancel a running calculate job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the calculate job is running for.
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running calculate job
        api_instance.audiences_cancel_calculate_audience_job(data_view_name, audience_id, job_id)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_cancel_calculate_audience_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the calculate job is running for. | 
 **job_id** | **int**| The id of the job to cancel | 

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
**204** | The job was cancelled successful |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to cancel the calculate job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_cancel_check_audience_job**
> audiences_cancel_check_audience_job(data_view_name, audience_id, job_id)

Cancel a running check job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the check job is running for.
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running check job
        api_instance.audiences_cancel_check_audience_job(data_view_name, audience_id, job_id)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_cancel_check_audience_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the check job is running for. | 
 **job_id** | **int**| The id of the job to cancel | 

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
**204** | The job was cancelled successful |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to cancel the check job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_cancel_export_audience_job**
> audiences_cancel_export_audience_job(data_view_name, audience_id, job_id)

Cancel a running export job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the export job is running for.
job_id = 56 # int | The id of the job to cancel

    try:
        # Cancel a running export job
        api_instance.audiences_cancel_export_audience_job(data_view_name, audience_id, job_id)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_cancel_export_audience_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the export job is running for. | 
 **job_id** | **int**| The id of the job to cancel | 

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
**204** | The job was cancelled successful |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to cancel the export job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_check_audience_latest_update_sync**
> AudienceCheckDetail audiences_check_audience_latest_update_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, check_audience_details=check_audience_details)

Calculate check statistics against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to analyse and the specified dimensions will be used to perform the analysis.

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to calculate the result for.
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
check_audience_details = apteco_api.CheckAudienceDetails() # CheckAudienceDetails | The details for checking this audience. (optional)

    try:
        # Calculate check statistics against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to analyse and the specified dimensions will be used to perform the analysis.
        api_response = api_instance.audiences_check_audience_latest_update_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, check_audience_details=check_audience_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_check_audience_latest_update_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to calculate the result for. | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service&#39;s configuration | [optional] 
 **check_audience_details** | [**CheckAudienceDetails**](CheckAudienceDetails.md)| The details for checking this audience. | [optional] 

### Return type

[**AudienceCheckDetail**](AudienceCheckDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculation completed successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to check this audience. |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_create_audience**
> AudienceDetail audiences_create_audience(data_view_name, audience_detail=audience_detail)

Creates a new audience from the given details for the logged in user.

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

# Defining host is optional and default to https://example.com/OrbitAPI
configuration.host = "https://example.com/OrbitAPI"
# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_detail = apteco_api.CreateAudienceDetail() # CreateAudienceDetail | The details for the audience to create.  If you want              to update a specific audience then PUT to the /Audiences/{audienceId} URL (optional)

    try:
        # Creates a new audience from the given details for the logged in user.
        api_response = api_instance.audiences_create_audience(data_view_name, audience_detail=audience_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_detail** | [**CreateAudienceDetail**](CreateAudienceDetail.md)| The details for the audience to create.  If you want              to update a specific audience then PUT to the /Audiences/{audienceId} URL | [optional] 

### Return type

[**AudienceDetail**](AudienceDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The audience was created successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_create_audience_hit_for_audience**
> AudienceHitDetail audiences_create_audience_hit_for_audience(data_view_name, audience_id, create_audience_hit_details=create_audience_hit_details)

Register a hit (view) for the given audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to register the hit for
create_audience_hit_details = apteco_api.CreateAudienceHitDetails() # CreateAudienceHitDetails | Details to register the hit with (optional)

    try:
        # Register a hit (view) for the given audience
        api_response = api_instance.audiences_create_audience_hit_for_audience(data_view_name, audience_id, create_audience_hit_details=create_audience_hit_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create_audience_hit_for_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to register the hit for | 
 **create_audience_hit_details** | [**CreateAudienceHitDetails**](CreateAudienceHitDetails.md)| Details to register the hit with | [optional] 

### Return type

[**AudienceHitDetail**](AudienceHitDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the created audience hit |  -  |
**400** | Bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_create_audience_update**
> AudienceUpdateDetail audiences_create_audience_update(data_view_name, audience_id, create_audience_update=create_audience_update)

Updates the details of a particular audience.  If you don't have an id for the  audience then POST to the /Audiences URL to create a new audience.

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

# Defining host is optional and default to https://example.com/OrbitAPI
configuration.host = "https://example.com/OrbitAPI"
# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to add/update
create_audience_update = apteco_api.CreateAudienceUpdate() # CreateAudienceUpdate | The details for the audience to add/update (optional)

    try:
        # Updates the details of a particular audience.  If you don't have an id for the  audience then POST to the /Audiences URL to create a new audience.
        api_response = api_instance.audiences_create_audience_update(data_view_name, audience_id, create_audience_update=create_audience_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create_audience_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to add/update | 
 **create_audience_update** | [**CreateAudienceUpdate**](CreateAudienceUpdate.md)| The details for the audience to add/update | [optional] 

### Return type

[**AudienceUpdateDetail**](AudienceUpdateDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The audience details were added/updated successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to update the details for this audience.  Only audience owners or admins can modify their audience |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_create_calculate_audience_data_licensing_job**
> AudienceDataLicensingInfoJobDetail audiences_create_calculate_audience_data_licensing_job(data_view_name, audience_id, data_licensing_detail=data_licensing_detail)

Create a new job to get data licensing information for the latest version of this audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to calculate the result for
data_licensing_detail = apteco_api.DataLicensingDetail() # DataLicensingDetail | The details required to get data licensing information for an audience (optional)

    try:
        # Create a new job to get data licensing information for the latest version of this audience
        api_response = api_instance.audiences_create_calculate_audience_data_licensing_job(data_view_name, audience_id, data_licensing_detail=data_licensing_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create_calculate_audience_data_licensing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to calculate the result for | 
 **data_licensing_detail** | [**DataLicensingDetail**](DataLicensingDetail.md)| The details required to get data licensing information for an audience | [optional] 

### Return type

[**AudienceDataLicensingInfoJobDetail**](AudienceDataLicensingInfoJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The calculate data licensing info job was successfully created |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the status of this data licensing job. |  -  |
**404** | The audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_create_calculate_audience_job_for_latest_update**
> AudienceCalculateJobDetail audiences_create_calculate_audience_job_for_latest_update(data_view_name, audience_id, calculate_audience_details=calculate_audience_details)

Create a new job to calculate counts against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to produce the end result

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to calculate the result for.
calculate_audience_details = apteco_api.CalculateAudienceDetails() # CalculateAudienceDetails | The details for calculating this audience. (optional)

    try:
        # Create a new job to calculate counts against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to produce the end result
        api_response = api_instance.audiences_create_calculate_audience_job_for_latest_update(data_view_name, audience_id, calculate_audience_details=calculate_audience_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create_calculate_audience_job_for_latest_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to calculate the result for. | 
 **calculate_audience_details** | [**CalculateAudienceDetails**](CalculateAudienceDetails.md)| The details for calculating this audience. | [optional] 

### Return type

[**AudienceCalculateJobDetail**](AudienceCalculateJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The calculate job was successfully created |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to calculate this audience. |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_create_check_audience_job_for_latest_update**
> AudienceCheckJobDetail audiences_create_check_audience_job_for_latest_update(data_view_name, audience_id, check_audience_details=check_audience_details)

Create a new job to calculate check statistics against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to analyse and the specified dimensions will be used to perform the analysis.

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to calculate the result for.
check_audience_details = apteco_api.CheckAudienceDetails() # CheckAudienceDetails | The details for checking this audience. (optional)

    try:
        # Create a new job to calculate check statistics against the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to analyse and the specified dimensions will be used to perform the analysis.
        api_response = api_instance.audiences_create_check_audience_job_for_latest_update(data_view_name, audience_id, check_audience_details=check_audience_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create_check_audience_job_for_latest_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to calculate the result for. | 
 **check_audience_details** | [**CheckAudienceDetails**](CheckAudienceDetails.md)| The details for checking this audience. | [optional] 

### Return type

[**AudienceCheckJobDetail**](AudienceCheckJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The check job was successfully created |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to check this audience. |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_create_export_audience_job_for_latest_update**
> AudienceExportJobDetail audiences_create_export_audience_job_for_latest_update(data_view_name, audience_id, export_audience_details=export_audience_details)

Create a new job to export data from the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to export and the specified columns will be used to export the data, to a file  and/or as a sample within the body of the result

Might require licence flags [Export]

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to export data for.
export_audience_details = apteco_api.ExportAudienceDetails() # ExportAudienceDetails | The details for exporting this audience. (optional)

    try:
        # Create a new job to export data from the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to export and the specified columns will be used to export the data, to a file  and/or as a sample within the body of the result
        api_response = api_instance.audiences_create_export_audience_job_for_latest_update(data_view_name, audience_id, export_audience_details=export_audience_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create_export_audience_job_for_latest_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to export data for. | 
 **export_audience_details** | [**ExportAudienceDetails**](ExportAudienceDetails.md)| The details for exporting this audience. | [optional] 

### Return type

[**AudienceExportJobDetail**](AudienceExportJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The export job was successfully created |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to export this audience. |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_delete_audience**
> audiences_delete_audience(data_view_name, audience_id)

Deletes the specified audience

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

# Defining host is optional and default to https://example.com/OrbitAPI
configuration.host = "https://example.com/OrbitAPI"
# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to delete

    try:
        # Deletes the specified audience
        api_instance.audiences_delete_audience(data_view_name, audience_id)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_delete_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to delete | 

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
**204** | The audience was deleted successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete this audience.  Only audience owners or admins can delete their audiences |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_export_audience_latest_update_sync**
> AudienceExportDetail audiences_export_audience_latest_update_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, export_audience_details=export_audience_details)

Create a new job to export data from the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to export and the specified columns will be used to export the data, to a file  and/or as a sample within the body of the result

Might require licence flags [Export]

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to export data for.
timeout_in_seconds = 56 # int | The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service's configuration (optional)
export_audience_details = apteco_api.ExportAudienceDetails() # ExportAudienceDetails | The details for calculating this audience. (optional)

    try:
        # Create a new job to export data from the FastStats system for the latest version of this audience.  The different queries associated with the latest  version of this audience will be combined to identify the data to export and the specified columns will be used to export the data, to a file  and/or as a sample within the body of the result
        api_response = api_instance.audiences_export_audience_latest_update_sync(data_view_name, audience_id, timeout_in_seconds=timeout_in_seconds, export_audience_details=export_audience_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_export_audience_latest_update_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to export data for. | 
 **timeout_in_seconds** | **int**| The number of seconds before the request will time out.  Leave unspecified to use the default value given in the audience service&#39;s configuration | [optional] 
 **export_audience_details** | [**ExportAudienceDetails**](ExportAudienceDetails.md)| The details for calculating this audience. | [optional] 

### Return type

[**AudienceExportDetail**](AudienceExportDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The export completed successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to export this audience. |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience**
> AudienceDetail audiences_get_audience(data_view_name, audience_id, include_queries=include_queries, include_brief=include_brief)

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

# Defining host is optional and default to https://example.com/OrbitAPI
configuration.host = "https://example.com/OrbitAPI"
# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to view
include_queries = True # bool | If specified, whether to include the query definitions for this audience or not.  Defaults to true - to return query definitions (optional)
include_brief = True # bool | If specified, whether to include the brief for this audience or not.  Defaults to true - to return the brief (optional)

    try:
        # Returns the details of a particular audience
        api_response = api_instance.audiences_get_audience(data_view_name, audience_id, include_queries=include_queries, include_brief=include_brief)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to view | 
 **include_queries** | **bool**| If specified, whether to include the query definitions for this audience or not.  Defaults to true - to return query definitions | [optional] 
 **include_brief** | **bool**| If specified, whether to include the brief for this audience or not.  Defaults to true - to return the brief | [optional] 

### Return type

[**AudienceDetail**](AudienceDetail.md)

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
**404** | The audience or DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience_hit_for_audience**
> AudienceHitDetail audiences_get_audience_hit_for_audience(data_view_name, audience_id, audience_hit_id)

Returns details for a given audience hit for this audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to get the hit information for
audience_hit_id = 56 # int | The id of the hit

    try:
        # Returns details for a given audience hit for this audience
        api_response = api_instance.audiences_get_audience_hit_for_audience(data_view_name, audience_id, audience_hit_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience_hit_for_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to get the hit information for | 
 **audience_hit_id** | **int**| The id of the hit | 

### Return type

[**AudienceHitDetail**](AudienceHitDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the given audience hit |  -  |
**400** | Bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView, audience or audience hit couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience_hits_for_audience**
> PagedResultsAudienceHitSummary audiences_get_audience_hits_for_audience(data_view_name, audience_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns a summary of the hits for this audience - i.e. information about when users have viewed the audience.

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to get the hit information for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, Timestamp, UserAgentDetails (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns a summary of the hits for this audience - i.e. information about when users have viewed the audience.
        api_response = api_instance.audiences_get_audience_hits_for_audience(data_view_name, audience_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience_hits_for_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to get the hit information for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, Timestamp, UserAgentDetails | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAudienceHitSummary**](PagedResultsAudienceHitSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries of the hits of this audience |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience_latest_native_for_nett_query**
> str audiences_get_audience_latest_native_for_nett_query(data_view_name, audience_id)

Returns native XML (i.e. for use with other FastStats applications) for the Nett query of the latest update for a particular audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience

    try:
        # Returns native XML (i.e. for use with other FastStats applications) for the Nett query of the latest update for a particular audience
        api_response = api_instance.audiences_get_audience_latest_native_for_nett_query(data_view_name, audience_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience_latest_native_for_nett_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience | 

### Return type

**str**

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The query XML |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience_result**
> AudienceResultDetail audiences_get_audience_result(data_view_name, audience_id, audience_result_id)

Returns details of a particular result for a particular audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to get the results for
audience_result_id = 56 # int | The id of the result for the audience

    try:
        # Returns details of a particular result for a particular audience
        api_response = api_instance.audiences_get_audience_result(data_view_name, audience_id, audience_result_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to get the results for | 
 **audience_result_id** | **int**| The id of the result for the audience | 

### Return type

[**AudienceResultDetail**](AudienceResultDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience result |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView, audience or result couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience_results**
> PagedResultsAudienceResultSummary audiences_get_audience_results(data_view_name, audience_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns a summary of the results for a particular audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to get the audience of results for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Timestamp, Username, AudienceUpdateId, Description, OwnerUsername, IsDeleted, ResolveTableName, BriefText (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Timestamp, Username, AudienceUpdateId, Description, OwnerUsername, IsDeleted, ResolveTableName, BriefText (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns a summary of the results for a particular audience
        api_response = api_instance.audiences_get_audience_results(data_view_name, audience_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to get the audience of results for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Timestamp, Username, AudienceUpdateId, Description, OwnerUsername, IsDeleted, ResolveTableName, BriefText | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Timestamp, Username, AudienceUpdateId, Description, OwnerUsername, IsDeleted, ResolveTableName, BriefText | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAudienceResultSummary**](PagedResultsAudienceResultSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries of the audience results |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience_update**
> AudienceUpdateDetail audiences_get_audience_update(data_view_name, audience_id, audience_update_id, include_queries=include_queries, include_brief=include_brief)

Returns details of an update for a particular audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that contains the update
audience_update_id = 56 # int | The id of the update for the audience
include_queries = True # bool | If specified, whether to include the query definitions for this update or not.  Defaults to true - to return query definitions (optional)
include_brief = True # bool | If specified, whether to include the brief for this update or not.  Defaults to true - to return the brief (optional)

    try:
        # Returns details of an update for a particular audience
        api_response = api_instance.audiences_get_audience_update(data_view_name, audience_id, audience_update_id, include_queries=include_queries, include_brief=include_brief)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that contains the update | 
 **audience_update_id** | **int**| The id of the update for the audience | 
 **include_queries** | **bool**| If specified, whether to include the query definitions for this update or not.  Defaults to true - to return query definitions | [optional] 
 **include_brief** | **bool**| If specified, whether to include the brief for this update or not.  Defaults to true - to return the brief | [optional] 

### Return type

[**AudienceUpdateDetail**](AudienceUpdateDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience update |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView, audience or update couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audience_updates**
> PagedResultsAudienceUpdateSummary audiences_get_audience_updates(data_view_name, audience_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns a summary of the updates to a particular audience

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to get the updates for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Timestamp, Username, Title, Description, OwnerUsername, IsDeleted, ResolveTableName (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Timestamp, Username, Title, Description, OwnerUsername, IsDeleted, ResolveTableName (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Returns a summary of the updates to a particular audience
        api_response = api_instance.audiences_get_audience_updates(data_view_name, audience_id, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audience_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to get the updates for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Timestamp, Username, Title, Description, OwnerUsername, IsDeleted, ResolveTableName | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Timestamp, Username, Title, Description, OwnerUsername, IsDeleted, ResolveTableName | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAudienceUpdateSummary**](PagedResultsAudienceUpdateSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries of the audience updates |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this audience |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_audiences**
> PagedResultsAudienceSummary audiences_get_audiences(data_view_name, include_deleted=include_deleted, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Gets summary information about each audience in the DataView.

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
include_deleted = 'include_deleted_example' # str | If specified, whether to include deleted audience, not deleted audience or both.  Defaults to not deleted only (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, LastUpdatedUsername, LastUpdatedOn (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, LastUpdatedUsername, LastUpdatedOn (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

    try:
        # Requires OrbitAdmin: Gets summary information about each audience in the DataView.
        api_response = api_instance.audiences_get_audiences(data_view_name, include_deleted=include_deleted, filter=filter, order_by=order_by, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_audiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **include_deleted** | **str**| If specified, whether to include deleted audience, not deleted audience or both.  Defaults to not deleted only | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, LastUpdatedUsername, LastUpdatedOn | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, SystemName, Title, Description, OwnerUsername, CreatedOn, DeletedOn, ResolveTableName, LastUpdatedUsername, LastUpdatedOn | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsAudienceSummary**](PagedResultsAudienceSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all audiences |  -  |
**400** | A bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_calculate_audience_data_licensing_job**
> AudienceDataLicensingInfoJobDetail audiences_get_calculate_audience_data_licensing_job(data_view_name, audience_id, job_id, data_licensing_detail=data_licensing_detail)

Get the status of a running calculate job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the calculate job is running for.
job_id = 56 # int | The id of the job to get the status for.
data_licensing_detail = apteco_api.DataLicensingDetail() # DataLicensingDetail | The details required to get data licensing information for an audience (optional)

    try:
        # Get the status of a running calculate job
        api_response = api_instance.audiences_get_calculate_audience_data_licensing_job(data_view_name, audience_id, job_id, data_licensing_detail=data_licensing_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_calculate_audience_data_licensing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the calculate job is running for. | 
 **job_id** | **int**| The id of the job to get the status for. | 
 **data_licensing_detail** | [**DataLicensingDetail**](DataLicensingDetail.md)| The details required to get data licensing information for an audience | [optional] 

### Return type

[**AudienceDataLicensingInfoJobDetail**](AudienceDataLicensingInfoJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job status details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the status of this calculate job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_calculate_audience_job**
> AudienceCalculateJobDetail audiences_get_calculate_audience_job(data_view_name, audience_id, job_id)

Get the status of a running calculate job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the calculate job is running for.
job_id = 56 # int | The id of the job to get the status for.

    try:
        # Get the status of a running calculate job
        api_response = api_instance.audiences_get_calculate_audience_job(data_view_name, audience_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_calculate_audience_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the calculate job is running for. | 
 **job_id** | **int**| The id of the job to get the status for. | 

### Return type

[**AudienceCalculateJobDetail**](AudienceCalculateJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job status details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the status of this calculate job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_check_audience_job**
> AudienceCheckJobDetail audiences_get_check_audience_job(data_view_name, audience_id, job_id)

Get the status of a running check job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the check job is running for.
job_id = 56 # int | The id of the job to get the status for.

    try:
        # Get the status of a running check job
        api_response = api_instance.audiences_get_check_audience_job(data_view_name, audience_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_check_audience_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the check job is running for. | 
 **job_id** | **int**| The id of the job to get the status for. | 

### Return type

[**AudienceCheckJobDetail**](AudienceCheckJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job status details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the status of this check job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get_export_audience_job**
> AudienceExportJobDetail audiences_get_export_audience_job(data_view_name, audience_id, job_id)

Get the status of a running export job

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
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience that the export job is running for.
job_id = 56 # int | The id of the job to get the status for.

    try:
        # Get the status of a running export job
        api_response = api_instance.audiences_get_export_audience_job(data_view_name, audience_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get_export_audience_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience that the export job is running for. | 
 **job_id** | **int**| The id of the job to get the status for. | 

### Return type

[**AudienceExportJobDetail**](AudienceExportJobDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job status details |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to get the status of this export job. |  -  |
**404** | The DataView, audience or job couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_transfer_audience_ownership**
> AudienceDetail audiences_transfer_audience_ownership(data_view_name, audience_id, include_queries=include_queries, include_brief=include_brief, transfer_ownership_details=transfer_ownership_details)

Transfer ownership of an audience from the current user to a new owner

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

# Defining host is optional and default to https://example.com/OrbitAPI
configuration.host = "https://example.com/OrbitAPI"
# Enter a context with an instance of the API client
with apteco_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apteco_api.AudiencesApi(api_client)
    data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
audience_id = 56 # int | The id of the audience to transfer.
include_queries = True # bool | If specified, whether to include the query definitions for the returned audience or not.  Defaults to true - to return query definitions (optional)
include_brief = True # bool | If specified, whether to include the brief for this audience or not.  Defaults to true - to return the brief (optional)
transfer_ownership_details = apteco_api.TransferAudienceOwnershipDetails() # TransferAudienceOwnershipDetails | The details for transferring ownership of the audience. (optional)

    try:
        # Transfer ownership of an audience from the current user to a new owner
        api_response = api_instance.audiences_transfer_audience_ownership(data_view_name, audience_id, include_queries=include_queries, include_brief=include_brief, transfer_ownership_details=transfer_ownership_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudiencesApi->audiences_transfer_audience_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **audience_id** | **int**| The id of the audience to transfer. | 
 **include_queries** | **bool**| If specified, whether to include the query definitions for the returned audience or not.  Defaults to true - to return query definitions | [optional] 
 **include_brief** | **bool**| If specified, whether to include the brief for this audience or not.  Defaults to true - to return the brief | [optional] 
 **transfer_ownership_details** | [**TransferAudienceOwnershipDetails**](TransferAudienceOwnershipDetails.md)| The details for transferring ownership of the audience. | [optional] 

### Return type

[**AudienceDetail**](AudienceDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ownership of the audience was successfully transferred |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to transfer this audience.  Only audience owners can transfer their audiences |  -  |
**404** | The DataView or audience couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

