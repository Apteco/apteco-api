# ParetoSpecification

The details needed for specifying a pareto dashboard item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_variable_name** | **str** | The name of the variable to calculate the value for the pareto chart | 
**category_variable_name** | **str** | If specified, the name of the categories to show on the pareto chart.  If no categories are specified then records from the resolve table will be grouped together | [optional] 
**number_of_bands** | **int** | If specified, and no category variable is specified, then the number of bands to group the records on the resolve table into. | [optional] 
**resolve_table_name** | **str** | The name of the table to group together | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


