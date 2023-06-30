# UserAudienceCompositionSummary

Summary details for an audience composition viewable by a given user
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewing_username** | **str** | The username of the user that has access to this audience composition | 
**shared_to_me** | **bool** | Whether this audience composition has been shared to the given user by someone else | 
**shared_by_me** | **bool** | Whether this audience composition has been shared to others by the given user | 
**id** | **int** | The id of this composition | 
**description** | **str** | The description of this composition | 
**type** | **str** | The type of this composition | 
**system_name** | **str** | The name of the FastStats system that this composition is for | 
**owner** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**number_of_users_shared_with** | **int** | The number of people this composition has been shared with | 
**shared_to_all** | **bool** | Whether this composition has been shared to all users | 
**share_id** | **int** | The id of the share associated with this composition, or null if the  composition has not yet been shared | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


