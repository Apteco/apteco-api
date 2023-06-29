# ExportAudienceDetails

The details required to generate a data export for an audience

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_number_of_rows_to_browse** | **int** | The maximum number of rows to return when browsing the data | 
**return_browse_rows** | **bool** | Whether to return data rows in the response or just export data to a file | 
**filename** | **str** | If specified, the filename of a file to create, containing the full export data.  The file will be created in the directory for the associated audience, as configured in the API | [optional] 
**output** | [**Output**](Output.md) |  | [optional] 
**columns** | [**list[Column]**](Column.md) | The list of columns to include in this export | 
**generate_urn_file** | **bool** | Whether to generate a URN file with this export or not | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


