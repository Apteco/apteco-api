# JobSummary

Summary information for a job in FastStats
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the job | 
**priority** | **int** | The priority of the job.  The lower the number the more important the job | 
**state** | **str** | The state of the job.  Valid values can include &#39;cancel&#39;, &#39;done&#39;, &#39;incomplete&#39;, &#39;inserting&#39; and &#39;unassigned&#39; | 
**cancel_requested** | **bool** | Whether this job has been asked to cancel.  If it has then acted on this request and been cancelled then the state will be set to &#39;cancel&#39; | 
**time_added** | **datetime** | The date and time that the job was added to the job queue | [optional] 
**time_sent** | **datetime** | The date and time that the job was sent from the queue to be processed | [optional] 
**time_finished** | **datetime** | The date and time that the job finished processing | [optional] 
**server** | **str** | The hostname of the server that is processing/processed this job | 
**system_name** | **str** | The name of the FastStats system that this job is running against | 
**thread_number** | **int** | The number of the thread within the FastStats Service that is running this job | 
**username** | **str** | The name of the user that submitted this job | 
**job_type** | **str** | The type of the job | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


