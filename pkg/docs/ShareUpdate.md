# ShareUpdate

Details for a particular update that happened to a share
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the update | 
**timestamp** | **datetime** | The timestamp of when the update happened | 
**user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**notes** | **str** | The notes associated with this share update | 
**number_of_added_users** | **int** | The number of users that were added to this share as part of this update | 
**first_added_user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**shared_to_all** | **bool** | Whether this share was shared to all as part of this update | 
**number_of_removed_users** | **int** | The number of users that were removed from this share as part of this update | 
**first_removed_user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**number_of_added_groups** | **int** | The number of groups that were added to this share as part of this update | 
**first_added_group** | [**GroupSummary**](GroupSummary.md) |  | 
**number_of_removed_groups** | **int** | The number of groups that were removed from this share as part of this update | 
**first_removed_group** | [**GroupSummary**](GroupSummary.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


