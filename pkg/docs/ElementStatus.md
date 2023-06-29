# ElementStatus

Status information for a PeopleStage element

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The element&#39;s id | 
**description** | **str** | The element&#39;s description | 
**type** | **str** | The element&#39;s type | 
**successful_campaigns_count** | **int** | The number of campaigns that currently have a success status within this element | [optional] 
**errored_campaigns_count** | **int** | The number of campaigns that currently have an errored status within this element | [optional] 
**inactive_campaigns_count** | **int** | The number of campaigns that currently have an inactive status within this element | [optional] 
**needs_approval_campaigns_count** | **int** | The number of campaigns that currently have a message that needs approval within this element | [optional] 
**channel_types** | **list[str]** | The different types of channel that have been used by deliveries within this element | [optional] 
**first_ran** | **datetime** | The first time that any deliveries ran within this element | [optional] 
**last_ran** | **datetime** | The last time that any deliveries ran within this element | [optional] 
**statistics_timestamp** | **datetime** | The date and time that the statistics were calculated | [optional] 
**path** | [**list[ElementKey]**](ElementKey.md) | The element&#39;s path | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


