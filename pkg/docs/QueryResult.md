# QueryResult

Details for a count of a particular query
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the query that has been counted | [optional] 
**notes** | **str** | Any notes associated with the query that has been counted | [optional] 
**ran_successfully** | **bool** | Whether the query was counted successfully or not | 
**system_name** | **str** | The name of the FastStats system that this count has been produced by | [optional] 
**system_load_date** | **datetime** | The date and time that the FastStats system from which this count has come was last built | [optional] 
**user_name** | **str** | The name of the user that requested this count | [optional] 
**run_date** | **datetime** | The date and time that this count was run on | [optional] 
**query_description** | **str** | A textual description of the query that was counted | [optional] 
**counts** | [**list[Count]**](Count.md) | A list of counts for each affected table in the FastStats system.  The first count in the list is the main one. | [optional] 
**messages** | [**list[ServerMessage]**](ServerMessage.md) | A list of messages associated with this result | [optional] 
**query** | [**Query**](Query.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


