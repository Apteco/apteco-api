# DataPurchaseJobDetail

Details for a job to purchase data licensing records
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_info** | [**PurchaseInfo**](PurchaseInfo.md) |  | [optional] 
**id** | **int** | The job&#39;s id | 
**is_complete** | **bool** | Whether the job is complete or not | 
**queue_position** | **int** | If present, the position that the job is in the job queue.  Jobs only start being actively processed once they reach the head of the queue | [optional] 
**progress** | **int** | If present, an estimate of how far through its processing this job is | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


