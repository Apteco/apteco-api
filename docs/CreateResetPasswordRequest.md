# CreateResetPasswordRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | The email address for the user resetting their password | 
**reset_password_url** | **str** | A URL to send in the notification to the user to allow them to confirm they want to reset their password.    If the URL is specified, it can use the {token}, {emailAddress} and {username} parameters:    http://www.example.com/resetPassword/{token}?email&#x3D;{emailAddress}&amp;amp;username&#x3D;{username}    If present, the {token} parameter will be replaced with the token of the password reset request, which  will be needed when performing the reset.  The {emailAddress} parameter will be replaced with the email address  of the user resetting their password.  The {username} parameter will be replaced with the username of the  user resetting their password. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


