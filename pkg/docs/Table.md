# Table

Details for a table in the FastStats system
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the table | 
**singular_display_name** | **str** | A description to use for this table when refering to a single entity (i.e. \&quot;A Person\&quot;) | 
**plural_display_name** | **str** | A description to use for this table when refering to multiple entities (i.e. \&quot;Many People\&quot;) | 
**is_default_table** | **bool** | Whether this table is the default table in the FastStats system or not - i.e. the table to use when creating a blank query | 
**is_people_table** | **bool** | Whether this table is the one in the FastStats system used to represent natural people | 
**total_records** | **int** | The total number of records in this table | 
**child_relationship_name** | **str** | A descriptive word or phrase to use when relating this table to one of its child tables (i.e. a Households \&quot;is occupied by\&quot; a Customer) | 
**parent_relationship_name** | **str** | A descriptive word or phrase to use when relating this table to one of its parent tables (i.e. a Customer \&quot;lives at\&quot; a Households) | 
**has_child_tables** | **bool** | Whether this table has any child tables | 
**parent_table** | **str** | The name of the parent table for this table.  The Master table is the only table without a parent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


