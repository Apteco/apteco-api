# CreateShareUpdate

The details required to create a new share update

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** | The notes associated with this share update | [optional] 
**email_addresses_to_add** | **list[str]** | Email addresses of new users to share this shareable item with | [optional] 
**notify_added_users** | **bool** | Whether to notify new users that the shareable item has now been shared with them | 
**added_user_notification_message** | **str** | If added users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message. | [optional] 
**email_addresses_to_remove** | **list[str]** | Email addresses of users that this shareable item has already been shared with that should be removed from the share | [optional] 
**notify_removed_users** | **bool** | Whether to notify existing users that the share has been updated | 
**removed_user_notification_message** | **str** | If removed users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message. | [optional] 
**notify_unchanged_users** | **bool** | Whether to notify users that the shareable item is shared with, but that haven&#39;t   been added or removed that the share has been updated | 
**unchanged_user_notification_message** | **str** | If unchanged users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


