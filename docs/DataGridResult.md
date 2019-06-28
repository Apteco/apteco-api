# DataGridResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the DataGrid | [optional] 
**notes** | **str** | Any notes associated with the DataGrid | [optional] 
**ran_successfully** | **bool** | Whether the DataGrid was returned successfully or not | 
**system_name** | **str** | The name of the FastStats system that this DataGrid has been produced by | [optional] 
**system_load_date** | **datetime** | The date and time that the FastStats system was last built | [optional] 
**user_name** | **str** | The name of the user that requested this DataGrid | [optional] 
**run_date** | **datetime** | The date and time that this DataGrid was run on | [optional] 
**query_description** | **str** | A textual description of the query that was counted | [optional] 
**counts** | [**list[Count]**](Count.md) | A list of counts for each affected table in the FastStats system.  The first count in the list is the main one. | [optional] 
**headers** | [**list[DataGridHeader]**](DataGridHeader.md) | The DataGrid Headers | [optional] 
**rows** | **list[list[str]]** | The data values in the DataGrid formated as a list of lists | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


