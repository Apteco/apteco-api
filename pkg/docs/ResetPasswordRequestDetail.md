# ResetPasswordRequestDetail

Details of a reset password request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reset_password_url** | **str** | The URL sent in the notification to the user to allow them to confirm they want to reset their password. | [optional] 
**has_notification_been_sent** | **bool** | Whether the notification has been sent to the user or not. | 
**token** | **str** | The token for this reset password request | 
**username** | **str** | The username of the user requesting the reset password | 
**email_address** | **str** | The email address of the user requesting the reset password | 
**creation_date** | **datetime** | The date and time this request was created | 
**confirmed_date** | **datetime** | The date and time this request was confirmed | [optional] 
**expired_date** | **datetime** | The date and time this request expired | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


