# CreateUserRegistrationRequest

The parameters needed to create a new user registration request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username for the new user to be created with | 
**firstname** | **str** | The first name for the new user | [optional] 
**surname** | **str** | The surname for the new user | [optional] 
**email_address** | **str** | The email address for the new user | 
**password** | **str** | The password for the new user | 
**confirm_registration_url** | **str** | A URL to send in the notification to the user to allow them to confirm their registration.    If the URL is specified, it can use the {token} parameter:    http://www.example.com/register/{token}    If present, this parameter will be replaced with the token of the registration request, which will be needed when confirming the registration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


