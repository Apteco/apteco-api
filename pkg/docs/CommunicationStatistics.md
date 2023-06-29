# CommunicationStatistics

Communication statistics for a given set of days

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **list[str]** | The set of days where communication information is available | 
**communications_counts** | **list[int]** | The set of counts representing the number of communications on the corresponding day.  The first figure is data for the first day in the Days list, and so on. | 
**total_communications_count** | **int** | The total number of communications across all days | 
**deliveries_counts** | **list[int]** | The set of counts representing the number of deliveries that have run on the corresponding day.  The first figure is data for the first day in the Days list, and so on. | 
**total_deliveries_count** | **int** | The total number of deliveries that have run across all days | 
**messages_counts** | **list[int]** | The set of counts representing the number of messages that have had at least one delivery run on the corresponding day.  The first figure is data for the first day in the Days list, and so on. | 
**total_messages_count** | **int** | The total number of messages that have had at least one delivery run across all days | 
**campaigns_counts** | **list[int]** | The set of counts representing the number of campaigns that have had at least one delivery run on the corresponding day.  The first figure is data for the first day in the Days list, and so on. | 
**total_campaigns_count** | **int** | The total number of campaigns that have had at least one delivery run across all days | 
**people_counts** | **list[int]** | The set of counts representing the number of unique people processed on the corresponding day.  The first figure is data for the first day in the Days list, and so on. | 
**communication_statistics_timestamp** | **datetime** | The date and time that the communication statistics were calculated | [optional] 
**campaign_statistics_timestamp** | **datetime** | The date and time that the delivery, message and campaign statistics were calculated | [optional] 
**people_statistics_timestamp** | **datetime** | The date and time that the people statistics were calculated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


