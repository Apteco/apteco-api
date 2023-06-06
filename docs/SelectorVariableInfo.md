# SelectorVariableInfo

Details specific for selector variables in the FastStats system
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector_type** | **str** | The type of selector that this variable is | [optional] 
**sub_type** | **str** | Further type information (such as whether the selector variable is a date or datetime) for this variable | [optional] 
**var_code_order** | **str** | How the categories are ordered within this variable | [optional] 
**number_of_codes** | **int** | The number of different categories (var codes) that this variable has | [optional] 
**code_length** | **int** | The length of the code for each category (in bytes) for this variable | [optional] 
**minimum_var_code_count** | **int** | The minimum count value in the variable&#39;s set of categories (var codes) | [optional] 
**maximum_var_code_count** | **int** | The maximum count value in the variable&#39;s set of categories (var codes) | [optional] 
**minimum_date** | **datetime** | If this variable is a date variable, The earliest date represented by this variable | [optional] 
**maximum_date** | **datetime** | If this variable is a date variable, The latest date represented by this variable | [optional] 
**combined_from_variable_name** | **str** | If this variable is a summary/combined categories variable, then this is the name of the parent variable that this summarises | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


