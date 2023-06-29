# AudienceResultSummary

Summary information for an audience result

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id for this audience result | 
**audience_update_id** | **int** | The id of the update (audience version) that this audience result was calculated with | 
**timestamp** | **datetime** | The date and time that this audience result was calculated | 
**fast_stats_build_date** | **datetime** | The date and time that the FastStats system used to calculate this audience result was built | 
**user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**nett_results** | [**AudienceQueryResult**](AudienceQueryResult.md) |  | 
**urn_file_path** | **str** | If a URN file was generated as part of this audience result then this will be its path within the FastStats system | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


