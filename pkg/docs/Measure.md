# Measure

A measure to define the figures shown for each cell created by the dimensions of the cube

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the measure | 
**resolve_table_name** | **str** | The name of the table to resolve this measure to.  I.e. all the counts in this measure will be counts of entities from this table | 
**function** | **str** | The function to use to aggregate up the data per cell within this measure | 
**variable_name** | **str** | If the measure is based on a variable then the name of the variable to use | [optional] 
**query** | [**Query**](Query.md) |  | [optional] 
**filter_query** | [**Query**](Query.md) |  | [optional] 
**expression** | [**Expression**](Expression.md) |  | [optional] 
**sort** | **str** | How the cells are sorted in this measure | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


