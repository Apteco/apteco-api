# ModifyUserDashboardDetail

Details used to modify an existing dashboard for a given user
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the dashboard | [optional] 
**id** | **int** | The dashboard&#39;s id | 
**title** | **str** | The title of the dashboard | 
**description** | **str** | The description of the dashboard | [optional] 
**theme_id** | **int** | The dashboard theme id | [optional] 
**logo_id** | **int** | The dashboard logo id | [optional] 
**base_query** | [**Query**](Query.md) |  | [optional] 
**dashboard_items** | [**list[DashboardContentItem]**](DashboardContentItem.md) | The items that are contained within the dashboard | [optional] 
**system_name** | **str** | The connected system of the dashboard | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


