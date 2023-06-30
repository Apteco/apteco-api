# UserAudienceCompositionDetail

Details for an audience viewable by a given user
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewing_username** | **str** | The username of the user that has access to this composition | 
**shared_to_me** | **bool** | Whether this composition has been shared to the given user by someone else | 
**shared_by_me** | **bool** | Whether this composition has been shared to others by the given user | 
**check_composition_definition** | [**CheckCompositionDefinition**](CheckCompositionDefinition.md) |  | [optional] 
**export_composition_definition** | [**ExportCompositionDefinition**](ExportCompositionDefinition.md) |  | [optional] 
**compositions_lookup** | [**SystemLookup**](SystemLookup.md) |  | [optional] 
**id** | **int** | The id of this composition | 
**description** | **str** | The description of this composition | 
**type** | **str** | The type of this composition | 
**system_name** | **str** | The name of the FastStats system that this composition is for | 
**owner** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**number_of_users_shared_with** | **int** | The number of people this composition has been shared with | 
**shared_to_all** | **bool** | Whether this composition has been shared to all users | 
**share_id** | **int** | The id of the share associated with this composition, or null if the  composition has not yet been shared | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


