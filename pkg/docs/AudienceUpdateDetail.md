# AudienceUpdateDetail

Details for an audience update
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brief_text** | **str** | Notes associated with the audience at the time of this update | [optional] 
**exclude_query** | [**Query**](Query.md) |  | [optional] 
**include_query** | [**Query**](Query.md) |  | [optional] 
**body_query** | [**Query**](Query.md) |  | [optional] 
**selection_modifiers** | [**SelectionModifiers**](SelectionModifiers.md) |  | [optional] 
**id** | **int** | The audience update&#39;s id | 
**timestamp** | **datetime** | The timestamp of when the update happened | 
**user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**title** | **str** | The title of the audience at the time of this update | 
**description** | **str** | The description of the audience at the time of this update | 
**owner** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**is_deleted** | **bool** | Whether this update set the audience to be deleted or not | 
**resolve_table_name** | **str** | The FastStats table that the audience is defined against at the time of this update | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


