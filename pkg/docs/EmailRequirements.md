# EmailRequirements

The details of the email requirements within the user configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_unrestricted_email_domains** | **bool** | Whether the domains of email addresses used to create users or share to users will  be checked against the list of RestrictedEmailDomains | 
**restricted_email_domains** | **list[str]** | The list of valid email domains available for creating user or sharing with users  If AllowUnrestrictedEmailDomains is false and an attempt is made to create a user  or share to a user with an email address that has a domain not in the list then an  error will be returned. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


