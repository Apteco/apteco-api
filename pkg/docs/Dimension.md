# Dimension

A dimension to define the categories to break the data in the cube down by

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the dimension | 
**type** | **str** | The type of the dimension | 
**query** | [**Query**](Query.md) |  | [optional] 
**variable_name** | **str** | If the dimension is a selector, numeric, date or text dimension then the name of the variable to use | [optional] 
**banding** | [**DimensionBanding**](DimensionBanding.md) |  | [optional] 
**function** | **str** | Details of the function to use for this dimension | [optional] 
**none_cell** | **bool** | If this dimension represents something for a table lower down the hierarchy to the cube&#39;s resolve table,  whether to include a cell for where there a no records on the lower table.  I.e. for where a person has no orders | [optional] 
**omit_unclassified** | **bool** | If this dimension represents a selector with an unclassified code, whether to omit this from the cube | [optional] 
**filter_query** | [**Query**](Query.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


