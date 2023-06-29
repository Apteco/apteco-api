# CreateShareDetail

The details required to create a new share

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shareable_type** | **str** | The type of the shareable item (collection, audience, etc.) being shared | 
**shareable_id** | **int** | The id of the shareable item being shared | 
**email_addresses_to_add** | **list[str]** | The list of email addresses to share this shareable item with | 
**notify_added_users** | **bool** | Whether to notify the users added in this share that the shareable item has now been shared with them | 
**added_user_notification_message** | **str** | If added users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message. | [optional] 
**notes** | **str** | The notes associated with this share update | [optional] 
**view_shareable_url** | **str** | A URL of a page to view the shareable item.  If specified this will be used in notification  messages to show added or removed users where to view the shareable item    If the URL is specified, it can use {shareableId} and {emailAddress} parameters    http://www.example.com/collections/{shareableId}?email&#x3D;{emailAddress}    If present, these parameters will be replaced with the id of the shareable item and the email address of the user being added/removed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


