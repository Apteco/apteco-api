# AudienceSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The audience&#39;s id | 
**title** | **str** | The title of the audience | 
**description** | **str** | The description of the audience | 
**creation_date** | **datetime** | The date the audience was created | 
**owner** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**deletion_date** | **datetime** | The date the audience was deleted, or null if it has not been deleted | 
**resolve_table_name** | **str** | The FastStats table that the audience is defined against | 
**resolve_table_nett_count** | **int** | If the audience has been counted, the latest overall count for the resolve table | [optional] 
**number_of_users_shared_with** | **int** | The number of people this audience has been shared with | 
**share_id** | **int** | The id of the share associated with this audience, or null if the  audience has not yet been shared | 
**number_of_hits** | **int** | The number of hits associated with this audience | 
**system_name** | **str** | The FastStats system that this audience has been created against | 
**last_updated_user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**last_updated_date** | **datetime** | The date the audience was last updated | 
**last_update_id** | **int** | The id of the last update for this audience | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


