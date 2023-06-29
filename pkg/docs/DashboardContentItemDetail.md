# DashboardContentItemDetail

The details of a dashboard item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drilldown_level** | **int** | The drill down level of the dashboard item | 
**description** | **str** | The description of the dashboard item | [optional] 
**chart_type** | **str** | The chart type that will be shown in the dashboard item | 
**resolve_table_name** | **str** | The table name that the data will resolve to | 
**dimensions** | [**list[Dimension]**](Dimension.md) | The dimensions of the dashboard item chart | [optional] 
**measures** | [**list[Measure]**](Measure.md) | The measures of the dashboard item chart | [optional] 
**omit_zeros** | **bool** | Whether to omit zeroes in the data of the dashboard item | [optional] 
**omit_unclassified** | **bool** | Whether to omit unclassifieds in the data of the dashboard item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


