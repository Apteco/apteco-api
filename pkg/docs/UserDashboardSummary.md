# UserDashboardSummary

Summary details for a dashboard viewable by a given user
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewing_username** | **str** | The username of the user that has access to this dashboard | 
**status** | **str** | The status of the dashboard | 
**shared_to_me** | **bool** | Whether this dashboard has been shared to the given user by someone else | 
**shared_by_me** | **bool** | Whether this dashboard has been shared to others by the given user | 
**id** | **int** | The dashboard&#39;s id | 
**title** | **str** | The title of the dashboard | 
**description** | **str** | The description of the dashboard | [optional] 
**system_name** | **str** | The FastStats system that this dashboard has been created against | 
**created_on** | **datetime** | The date the dashboard was created | [optional] 
**owner** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**last_updated_on** | **datetime** | The date the dashboard was last updated | [optional] 
**last_updated_by** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | [optional] 
**last_update_id** | **int** | The id of the last update for this dashboard | 
**number_of_users_shared_with** | **int** | The number of people this dashboard has been shared with | 
**shared_to_all** | **bool** | Whether this dashboard has been shared to all users | 
**share_id** | **int** | The id of the share associated with this dashboard, or null if the  dashboard has not yet been shared | [optional] 
**deleted_on** | **datetime** | The date the dashboard was deleted, or null if it has not been deleted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


