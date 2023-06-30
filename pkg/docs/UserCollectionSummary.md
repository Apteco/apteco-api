# UserCollectionSummary

Summary details for a collection viewable by a given user
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewing_username** | **str** | The username of the user that has access to this collection | 
**status** | **str** | The status of the collection | 
**shared_to_me** | **bool** | Whether this collection has been shared to the given user by someone else | 
**shared_by_me** | **bool** | Whether this collection has been shared to others by the given user | 
**id** | **int** | The collection&#39;s id | 
**title** | **str** | The title of the collection | 
**description** | **str** | The description of the collection | 
**creation_date** | **datetime** | The date the collection was created | 
**owner** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**deletion_date** | **datetime** | The date the collection was deleted, or null if it has not been deleted | 
**number_of_parts** | **int** | The number of parts within this collection | [optional] 
**number_of_users_shared_with** | **int** | The number of people this collection has been shared with | 
**share_id** | **int** | The id of the share associated with this collection, or null if the  collection has not yet been shared | 
**number_of_hits** | **int** | The number of hits associated with this collection | 
**system_name** | **str** | The FastStats system that this collection has been created against | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


