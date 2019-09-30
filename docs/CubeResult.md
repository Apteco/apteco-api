# CubeResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the cube that has been calculated | [optional] 
**notes** | **str** | Any notes associated with the query that has been counted | [optional] 
**ran_successfully** | **bool** | Whether the query was counted successfully or not | [optional] 
**system_name** | **str** | The name of the FastStats system that this count has been produced by | [optional] 
**system_load_date** | **datetime** | The date and time that the FastStats system from which this count has come was last built | [optional] 
**user_name** | **str** | The name of the user that requested this count | [optional] 
**run_date** | **datetime** | The date and time that this count was run on | [optional] 
**query_description** | **str** | A textual description of the query that was counted | [optional] 
**dimension_results** | [**list[DimensionResult]**](DimensionResult.md) | The set of dimension results for this cube, containing the category codes and descriptions for each dimension in the cube | [optional] 
**measure_results** | [**list[MeasureResult]**](MeasureResult.md) | The set of measure results for this cube, containing the values for each measure in the cube | [optional] 
**cube** | [**Cube**](Cube.md) |  | [optional] 
**counts** | [**list[Count]**](Count.md) | A list of counts for each affected table in the FastStats system.  The first count in the list is the main one. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


