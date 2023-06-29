# AudienceExportDetail

Detail information for an audience export

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_update_id** | **int** | The id of the update (audience version) that the export was created from | 
**timestamp** | **datetime** | The date and time that the export was produced | 
**fast_stats_build_date** | **datetime** | The date and time that the FastStats system used to create this export was built | 
**user** | [**UserDisplayDetails**](UserDisplayDetails.md) |  | 
**nett_counts** | [**list[Count]**](Count.md) | The set of overall counts for the audience behind this export | 
**urn_file_path** | **str** | If a URN file was generated as part of this export then this will be its path within the FastStats system | 
**maximum_number_of_rows_to_browse** | **int** | The requested maximum number of rows to return when browsing the data | 
**return_browse_rows** | **bool** | Whether data rows were requested to be returned or whether the data was exported directly to the specified file | 
**file_path** | **str** | If specified, the path of a file that the data was exported to | [optional] 
**output** | [**Output**](Output.md) |  | [optional] 
**columns** | [**list[Column]**](Column.md) | The list of columns that have been included in this export | 
**rows** | [**list[Row]**](Row.md) | If data rows were requested to be returned then the set of rows containing data for the given columns selected by the audience queries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


