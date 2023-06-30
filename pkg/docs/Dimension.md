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
**minimum_category_count** | **int** | If defined, a minimum threshold for all categories in this dimension before they are included in the results for the cube.  The  value for the threshold is the category&#39;s instant count.  If this property is specified then the TopNCategoryCount and PercentageOfMaximumCategoryThreshold properties must be left undefined. | [optional] 
**top_n_category_count** | **int** | If defined, specifies how many categories to return for this dimension (sorted descending by their instant count).   If this property is specified then the MinimumCategoryCount and PercentageOfMaximumCategoryThreshold properties must be left undefined. | [optional] 
**percentage_of_maximum_category_threshold** | **int** | If defined, a threshold for all categories in this dimension before they are included in the results for the cube.  The  threshold is specified as a percentage of the biggest instant count for any category in this dimension.  If this property is specified then the MinimumCategoryCount and TopNCategoryCount properties must be left undefined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


