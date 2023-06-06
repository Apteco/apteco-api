# AudienceCheckDetail

Detail information for an audience check
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_update_id** | **int** | The id of the update (audience version) that the export was created from | 
**timestamp** | **datetime** | The date and time that the export was produced | 
**fast_stats_build_date** | **datetime** | The date and time that the FastStats system used to create this export was built | 
**user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**nett_counts** | [**list[Count]**](Count.md) | The set of overall counts for the audience behind this export | 
**dimension_results** | [**list[CheckDimensionResult]**](CheckDimensionResult.md) | The list of dimension results containing audience and base counts | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


