# Cube

Information to request the calculating of a cube from FastStats based upon a query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_query** | [**Query**](Query.md) |  | 
**resolve_table_name** | **str** | The name of the table to resolve this cube to.  I.e. all the counts in the cube will be counts of entities from this table | 
**storage** | **str** | How the results of the cube will be returned | 
**dimensions** | [**list[Dimension]**](Dimension.md) | The dimensions to build the cube with.  This can be one or more variables, queries, etc. | 
**measures** | [**list[Measure]**](Measure.md) | The measures to build the cube with.  This can be one or more aggregations to calculate for the specified dimensions such as counts, sums, means, etc. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


