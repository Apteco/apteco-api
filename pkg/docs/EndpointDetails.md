# EndpointDetails

The details of a particular endpoint in the API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the endpoint | 
**group_name** | **str** | The name of the group this endpoint belongs to | 
**method** | **str** | The HTTP method used for calling this endpoint | 
**url_template** | **str** | The URL template of this endpoint | 
**allows_anonymous_access** | **bool** | Whether this endpoint can be accessed without authentication details | 
**is_experimental** | **bool** | Whether this endpoint has been marked as experimental | 
**is_under_development** | **bool** | Whether this endpoint has been marked as under development | 
**requires_licence_flags** | **list[str]** | The set of licence flags that the user must have in order to be able to call the endpoint | 
**optionally_requires_licence_flags** | **list[str]** | The set of licence flags that the user might need to have in order to be able to call the endpoint, depending on the type of request sent to the endpoint | 
**requires_roles** | **list[str]** | Any roles that the user must have to access this endpoint | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


