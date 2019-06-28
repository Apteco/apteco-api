# apteco_api.CollectionsApi

All URIs are relative to *http://example.com/OrbitAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_create_collection**](CollectionsApi.md#collections_create_collection) | **POST** /{dataViewName}/Collections | Creates a new collection from the given details for the logged in user.
[**collections_create_collection_hit_for_collection**](CollectionsApi.md#collections_create_collection_hit_for_collection) | **POST** /{dataViewName}/Collections/{collectionId}/Hits | Register a hit (view) for the given collection
[**collections_delete_collection**](CollectionsApi.md#collections_delete_collection) | **DELETE** /{dataViewName}/Collections/{collectionId} | Deletes the specified collection
[**collections_get_collection**](CollectionsApi.md#collections_get_collection) | **GET** /{dataViewName}/Collections/{collectionId} | Returns the details of a particular collection
[**collections_get_collection_hit_for_collection**](CollectionsApi.md#collections_get_collection_hit_for_collection) | **GET** /{dataViewName}/Collections/{collectionId}/Hits/{collectionHitId} | Returns details for a given collection hit for this collection
[**collections_get_collection_hits_for_collection**](CollectionsApi.md#collections_get_collection_hits_for_collection) | **GET** /{dataViewName}/Collections/{collectionId}/Hits | Returns a summary of the hits for this collection - i.e. information about when users have viewed the collection.
[**collections_get_collection_part**](CollectionsApi.md#collections_get_collection_part) | **GET** /{dataViewName}/Collections/{collectionId}/Parts/{partIndex} | Returns details of a part contained within a particular collection
[**collections_get_collection_parts**](CollectionsApi.md#collections_get_collection_parts) | **GET** /{dataViewName}/Collections/{collectionId}/Parts | Returns a summary of the parts contained within a particular collection
[**collections_get_collections**](CollectionsApi.md#collections_get_collections) | **GET** /{dataViewName}/Collections | Requires OrbitAdmin: Gets summary information about each collection in the DataView.
[**collections_transfer_collection_ownership**](CollectionsApi.md#collections_transfer_collection_ownership) | **POST** /{dataViewName}/Collections/{collectionId}/TransferOwnership | Transfer ownership of a collection from the current user to a new owner
[**collections_upsert_collection**](CollectionsApi.md#collections_upsert_collection) | **PUT** /{dataViewName}/Collections/{collectionId} | Updates the details of a particular collection.  If you don&#39;t have an id for the  collection then POST to the /Collections URL to create a new collection.


# **collections_create_collection**
> UpsertCollectionDetail collections_create_collection(data_view_name, collection_detail=collection_detail)

Creates a new collection from the given details for the logged in user.

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_detail = apteco_api.UpsertCollectionDetail() # UpsertCollectionDetail | The details for the collection to create.  If you want              to update a specific collection then PUT to the /Collections/{collectionId} URL (optional)

try:
    # Creates a new collection from the given details for the logged in user.
    api_response = api_instance.collections_create_collection(data_view_name, collection_detail=collection_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_detail** | [**UpsertCollectionDetail**](UpsertCollectionDetail.md)| The details for the collection to create.  If you want              to update a specific collection then PUT to the /Collections/{collectionId} URL | [optional] 

### Return type

[**UpsertCollectionDetail**](UpsertCollectionDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The collection was created successfully |  -  |
**400** | A bad request |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_create_collection_hit_for_collection**
> CollectionHitDetail collections_create_collection_hit_for_collection(data_view_name, collection_id, create_collection_hit_details=create_collection_hit_details)

Register a hit (view) for the given collection

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to register the hit for
create_collection_hit_details = apteco_api.CreateCollectionHitDetails() # CreateCollectionHitDetails | Details to register the hit with (optional)

try:
    # Register a hit (view) for the given collection
    api_response = api_instance.collections_create_collection_hit_for_collection(data_view_name, collection_id, create_collection_hit_details=create_collection_hit_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_create_collection_hit_for_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to register the hit for | 
 **create_collection_hit_details** | [**CreateCollectionHitDetails**](CreateCollectionHitDetails.md)| Details to register the hit with | [optional] 

### Return type

[**CollectionHitDetail**](CollectionHitDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the created collection hit |  -  |
**400** | Bad request |  -  |
**403** | The given session is not allowed to see the details for this collection |  -  |
**404** | The DataView or collection couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_delete_collection**
> collections_delete_collection(data_view_name, collection_id)

Deletes the specified collection

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to delete

try:
    # Deletes the specified collection
    api_instance.collections_delete_collection(data_view_name, collection_id)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to delete | 

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
**204** | The collection was deleted successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to delete this collection.  Only collection owners or admins can delete their collections |  -  |
**404** | The DataView or collection couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get_collection**
> CollectionDetail collections_get_collection(data_view_name, collection_id)

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to view

try:
    # Returns the details of a particular collection
    api_response = api_instance.collections_get_collection(data_view_name, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to view | 

### Return type

[**CollectionDetail**](CollectionDetail.md)

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
**404** | The collection or DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get_collection_hit_for_collection**
> CollectionHitDetail collections_get_collection_hit_for_collection(data_view_name, collection_id, collection_hit_id)

Returns details for a given collection hit for this collection

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to get the hit information for
collection_hit_id = 56 # int | The id of the hit

try:
    # Returns details for a given collection hit for this collection
    api_response = api_instance.collections_get_collection_hit_for_collection(data_view_name, collection_id, collection_hit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_get_collection_hit_for_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to get the hit information for | 
 **collection_hit_id** | **int**| The id of the hit | 

### Return type

[**CollectionHitDetail**](CollectionHitDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the given collection hit |  -  |
**400** | Bad request |  -  |
**403** | The given session is not allowed to see the details for this collection |  -  |
**404** | The DataView, collection or collection hit couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get_collection_hits_for_collection**
> PagedResultsCollectionHitSummary collections_get_collection_hits_for_collection(data_view_name, collection_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns a summary of the hits for this collection - i.e. information about when users have viewed the collection.

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to get the hit information for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, Timestamp, UserAgentDetails (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns a summary of the hits for this collection - i.e. information about when users have viewed the collection.
    api_response = api_instance.collections_get_collection_hits_for_collection(data_view_name, collection_id, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_get_collection_hits_for_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to get the hit information for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Username, Timestamp, UserAgentDetails | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsCollectionHitSummary**](PagedResultsCollectionHitSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries of the hits of this collection |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this collection |  -  |
**404** | The DataView or collection couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get_collection_part**
> CollectionPartDetail collections_get_collection_part(data_view_name, collection_id, part_index)

Returns details of a part contained within a particular collection

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection that contains the part
part_index = 56 # int | The index of the part within the collection

try:
    # Returns details of a part contained within a particular collection
    api_response = api_instance.collections_get_collection_part(data_view_name, collection_id, part_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_get_collection_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection that contains the part | 
 **part_index** | **int**| The index of the part within the collection | 

### Return type

[**CollectionPartDetail**](CollectionPartDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The collection part |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this collection |  -  |
**404** | The DataView, collection or part within the collection couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get_collection_parts**
> PagedResultsCollectionPartSummary collections_get_collection_parts(data_view_name, collection_id, filter=filter, order_by=order_by, offset=offset, count=count)

Returns a summary of the parts contained within a particular collection

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to get the parts for
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Title, VisualisationType (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Title, VisualisationType (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Returns a summary of the parts contained within a particular collection
    api_response = api_instance.collections_get_collection_parts(data_view_name, collection_id, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_get_collection_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to get the parts for | 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Title, VisualisationType | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Title, VisualisationType | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsCollectionPartSummary**](PagedResultsCollectionPartSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries of the collection parts |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to see the details for this collection |  -  |
**404** | The DataView or collection couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get_collections**
> PagedResultsCollectionSummary collections_get_collections(data_view_name, include_deleted=include_deleted, filter=filter, order_by=order_by, offset=offset, count=count)

Requires OrbitAdmin: Gets summary information about each collection in the DataView.

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
include_deleted = 'include_deleted_example' # str | If specified, whether to include deleted collections, not deleted collections or both.  Defaults to not deleted only (optional)
filter = 'filter_example' # str | Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate (optional)
order_by = 'order_by_example' # str | Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate (optional)
offset = 56 # int | The number of items to skip in the (potentially filtered) result set before returning subsequent items. (optional)
count = 56 # int | The maximum number of items to show from the (potentially filtered) result set. (optional)

try:
    # Requires OrbitAdmin: Gets summary information about each collection in the DataView.
    api_response = api_instance.collections_get_collections(data_view_name, include_deleted=include_deleted, filter=filter, order_by=order_by, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_get_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **include_deleted** | **str**| If specified, whether to include deleted collections, not deleted collections or both.  Defaults to not deleted only | [optional] 
 **filter** | **str**| Filter the list of items using a simple expression language.  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate | [optional] 
 **order_by** | **str**| Order the items by a given field (in ascending order unless the field is preceeded by a \&quot;-\&quot; character).  The available list of fields are Id, Title, Description, CreationDate, OwnerUsername, DeletionDate | [optional] 
 **offset** | **int**| The number of items to skip in the (potentially filtered) result set before returning subsequent items. | [optional] 
 **count** | **int**| The maximum number of items to show from the (potentially filtered) result set. | [optional] 

### Return type

[**PagedResultsCollectionSummary**](PagedResultsCollectionSummary.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all collection |  -  |
**400** | A bad request |  -  |
**403** | The user isn&#39;t an admin user |  -  |
**404** | The DataView couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_transfer_collection_ownership**
> CollectionDetail collections_transfer_collection_ownership(data_view_name, collection_id, transfer_ownership_details=transfer_ownership_details)

Transfer ownership of a collection from the current user to a new owner

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to transfer.
transfer_ownership_details = apteco_api.TransferCollectionOwnershipDetails() # TransferCollectionOwnershipDetails | The details for transferring ownership of the collection. (optional)

try:
    # Transfer ownership of a collection from the current user to a new owner
    api_response = api_instance.collections_transfer_collection_ownership(data_view_name, collection_id, transfer_ownership_details=transfer_ownership_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_transfer_collection_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to transfer. | 
 **transfer_ownership_details** | [**TransferCollectionOwnershipDetails**](TransferCollectionOwnershipDetails.md)| The details for transferring ownership of the collection. | [optional] 

### Return type

[**CollectionDetail**](CollectionDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ownership of the collection was successfully transferred |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to transfer this collection.  Only collection owners can transfer their collections |  -  |
**404** | The DataView or collection couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_upsert_collection**
> CollectionDetail collections_upsert_collection(data_view_name, collection_id, collection_detail=collection_detail)

Updates the details of a particular collection.  If you don't have an id for the  collection then POST to the /Collections URL to create a new collection.

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
api_instance = apteco_api.CollectionsApi(apteco_api.ApiClient(configuration))
data_view_name = 'data_view_name_example' # str | The name of the DataView to act on
collection_id = 56 # int | The id of the collection to add/update
collection_detail = apteco_api.UpsertCollectionDetail() # UpsertCollectionDetail | The details for the collection to add/update (optional)

try:
    # Updates the details of a particular collection.  If you don't have an id for the  collection then POST to the /Collections URL to create a new collection.
    api_response = api_instance.collections_upsert_collection(data_view_name, collection_id, collection_detail=collection_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_upsert_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_name** | **str**| The name of the DataView to act on | 
 **collection_id** | **int**| The id of the collection to add/update | 
 **collection_detail** | [**UpsertCollectionDetail**](UpsertCollectionDetail.md)| The details for the collection to add/update | [optional] 

### Return type

[**CollectionDetail**](CollectionDetail.md)

### Authorization

[faststats_auth](../README.md#faststats_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The collection details were added/updated successfully |  -  |
**400** | A bad request |  -  |
**403** | The given session is not allowed to update the details for this collection.  Only collection owners or admins can modify their collections |  -  |
**404** | The DataView or collection couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

