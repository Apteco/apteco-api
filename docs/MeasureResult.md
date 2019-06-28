# MeasureResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the measure | 
**rows** | **list[str]** | If the cube is a full cube then a set of rows containing a tab delimeted set of values.  The number of values in each row will be one per category in the first dimension.  If there is a second dimension then there will be one row for each category in the second dimension.  If there are three dimensions then there will be a set of rows (holding the data for all the cells in dimensions 1 and 2) for each category in dimension 3. | 
**cells** | **list[str]** | If he cube is a sparse cube then there will be a set of cells, each containing a way of indexing the cell in the cube and then the value of that cell. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


