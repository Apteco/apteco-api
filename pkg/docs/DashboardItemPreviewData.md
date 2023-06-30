# DashboardItemPreviewData

Information to request the calculating the preview of a dashboard item (cube) from FastStats based upon a query
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_item_id** | **str** | The id for this dashboard item | 
**drill_down_level** | **int** | The drill down level for this dashboard item | 
**sort_order** | **str** | Whether the chart for the given drill down level should be sorted in it&#39;s natural order, by ascending or descending values | 
**base_query** | [**Query**](Query.md) |  | 
**data_specification** | [**DashboardItemDataSpecification**](DashboardItemDataSpecification.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


