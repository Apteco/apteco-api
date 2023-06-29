# UserRegistrationRequestDetail

Details of a user registration request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm_registration_url** | **str** | The URL sent in the notification to the user to allow them to confirm their registration | [optional] 
**has_notification_been_sent** | **bool** | Whether the notification has been sent to the user or not. | 
**token** | **str** | The token for this registration request | 
**username** | **str** | The requested username | 
**firstname** | **str** | The requested first name | [optional] 
**surname** | **str** | The requested surname | [optional] 
**email_address** | **str** | The requested email address | 
**creation_date** | **datetime** | The date and time this request was created | 
**confirmed_date** | **datetime** | The date and time this request was confirmed | [optional] 
**expired_date** | **datetime** | The date and time this request expired | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


