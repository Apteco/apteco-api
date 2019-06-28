# CreateSessionParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_salt** | **str** | The salt to use when creating a session | 
**salt_password** | **bool** | Whether you have to use the UserSalt to create the password hash when logging in via the SaltedLogin method | 
**user_salt** | **str** | The password salt for the particular user | 
**use_password_hashes** | **bool** | Whether you have to hash the password with the given algorithm before it is combined with the login salt or not | 
**hash_algorithm** | **str** | The hash algorithm to use when generating the password hash | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


