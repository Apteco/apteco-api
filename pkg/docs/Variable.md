# Variable

Details for a variable in the FastStats system
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the variable | 
**description** | **str** | The description of the variable | 
**type** | **str** | The type of the variable | 
**folder_name** | **str** | The name of the folder that this variable belongs to within the FastStats system | [optional] 
**table_name** | **str** | The name of the table that this variable is from | 
**is_selectable** | **bool** | Whether the variable is allowed to used in selections | 
**is_browsable** | **bool** | Whether the variable is allowed to viewed with a client application (but not exported) | 
**is_exportable** | **bool** | Whether the variable is allowed to exported by a client application | 
**is_virtual** | **bool** | Whether the variable is a virtual variable (i.e. created after the system has been built) or not | 
**selector_info** | [**SelectorVariableInfo**](SelectorVariableInfo.md) |  | [optional] 
**numeric_info** | [**NumericVariableInfo**](NumericVariableInfo.md) |  | [optional] 
**text_info** | [**TextVariableInfo**](TextVariableInfo.md) |  | [optional] 
**reference_info** | [**object**](.md) | Details specific for reference (URN) variables in the FastStats system | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


