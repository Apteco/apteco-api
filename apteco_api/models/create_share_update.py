# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CreateShareUpdate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'notes': 'str',
        'email_addresses_to_add': 'list[str]',
        'notify_added_users': 'bool',
        'added_user_notification_message': 'str',
        'email_addresses_to_remove': 'list[str]',
        'notify_removed_users': 'bool',
        'removed_user_notification_message': 'str',
        'notify_unchanged_users': 'bool',
        'unchanged_user_notification_message': 'str'
    }

    attribute_map = {
        'notes': 'notes',
        'email_addresses_to_add': 'emailAddressesToAdd',
        'notify_added_users': 'notifyAddedUsers',
        'added_user_notification_message': 'addedUserNotificationMessage',
        'email_addresses_to_remove': 'emailAddressesToRemove',
        'notify_removed_users': 'notifyRemovedUsers',
        'removed_user_notification_message': 'removedUserNotificationMessage',
        'notify_unchanged_users': 'notifyUnchangedUsers',
        'unchanged_user_notification_message': 'unchangedUserNotificationMessage'
    }

    def __init__(self, notes=None, email_addresses_to_add=None, notify_added_users=None, added_user_notification_message=None, email_addresses_to_remove=None, notify_removed_users=None, removed_user_notification_message=None, notify_unchanged_users=None, unchanged_user_notification_message=None):  # noqa: E501
        """CreateShareUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._notes = None
        self._email_addresses_to_add = None
        self._notify_added_users = None
        self._added_user_notification_message = None
        self._email_addresses_to_remove = None
        self._notify_removed_users = None
        self._removed_user_notification_message = None
        self._notify_unchanged_users = None
        self._unchanged_user_notification_message = None
        self.discriminator = None

        if notes is not None:
            self.notes = notes
        if email_addresses_to_add is not None:
            self.email_addresses_to_add = email_addresses_to_add
        self.notify_added_users = notify_added_users
        if added_user_notification_message is not None:
            self.added_user_notification_message = added_user_notification_message
        if email_addresses_to_remove is not None:
            self.email_addresses_to_remove = email_addresses_to_remove
        self.notify_removed_users = notify_removed_users
        if removed_user_notification_message is not None:
            self.removed_user_notification_message = removed_user_notification_message
        self.notify_unchanged_users = notify_unchanged_users
        if unchanged_user_notification_message is not None:
            self.unchanged_user_notification_message = unchanged_user_notification_message

    @property
    def notes(self):
        """Gets the notes of this CreateShareUpdate.  # noqa: E501

        The notes associated with this share update  # noqa: E501

        :return: The notes of this CreateShareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreateShareUpdate.

        The notes associated with this share update  # noqa: E501

        :param notes: The notes of this CreateShareUpdate.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def email_addresses_to_add(self):
        """Gets the email_addresses_to_add of this CreateShareUpdate.  # noqa: E501

        Email addresses of new users to share this shareable item with  # noqa: E501

        :return: The email_addresses_to_add of this CreateShareUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses_to_add

    @email_addresses_to_add.setter
    def email_addresses_to_add(self, email_addresses_to_add):
        """Sets the email_addresses_to_add of this CreateShareUpdate.

        Email addresses of new users to share this shareable item with  # noqa: E501

        :param email_addresses_to_add: The email_addresses_to_add of this CreateShareUpdate.  # noqa: E501
        :type: list[str]
        """

        self._email_addresses_to_add = email_addresses_to_add

    @property
    def notify_added_users(self):
        """Gets the notify_added_users of this CreateShareUpdate.  # noqa: E501

        Whether to notify new users that the shareable item has now been shared with them  # noqa: E501

        :return: The notify_added_users of this CreateShareUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._notify_added_users

    @notify_added_users.setter
    def notify_added_users(self, notify_added_users):
        """Sets the notify_added_users of this CreateShareUpdate.

        Whether to notify new users that the shareable item has now been shared with them  # noqa: E501

        :param notify_added_users: The notify_added_users of this CreateShareUpdate.  # noqa: E501
        :type: bool
        """
        if notify_added_users is None:
            raise ValueError("Invalid value for `notify_added_users`, must not be `None`")  # noqa: E501

        self._notify_added_users = notify_added_users

    @property
    def added_user_notification_message(self):
        """Gets the added_user_notification_message of this CreateShareUpdate.  # noqa: E501

        If added users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message.  # noqa: E501

        :return: The added_user_notification_message of this CreateShareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._added_user_notification_message

    @added_user_notification_message.setter
    def added_user_notification_message(self, added_user_notification_message):
        """Sets the added_user_notification_message of this CreateShareUpdate.

        If added users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message.  # noqa: E501

        :param added_user_notification_message: The added_user_notification_message of this CreateShareUpdate.  # noqa: E501
        :type: str
        """

        self._added_user_notification_message = added_user_notification_message

    @property
    def email_addresses_to_remove(self):
        """Gets the email_addresses_to_remove of this CreateShareUpdate.  # noqa: E501

        Email addresses of users that this shareable item has already been shared with that should be removed from the share  # noqa: E501

        :return: The email_addresses_to_remove of this CreateShareUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses_to_remove

    @email_addresses_to_remove.setter
    def email_addresses_to_remove(self, email_addresses_to_remove):
        """Sets the email_addresses_to_remove of this CreateShareUpdate.

        Email addresses of users that this shareable item has already been shared with that should be removed from the share  # noqa: E501

        :param email_addresses_to_remove: The email_addresses_to_remove of this CreateShareUpdate.  # noqa: E501
        :type: list[str]
        """

        self._email_addresses_to_remove = email_addresses_to_remove

    @property
    def notify_removed_users(self):
        """Gets the notify_removed_users of this CreateShareUpdate.  # noqa: E501

        Whether to notify existing users that the share has been updated  # noqa: E501

        :return: The notify_removed_users of this CreateShareUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._notify_removed_users

    @notify_removed_users.setter
    def notify_removed_users(self, notify_removed_users):
        """Sets the notify_removed_users of this CreateShareUpdate.

        Whether to notify existing users that the share has been updated  # noqa: E501

        :param notify_removed_users: The notify_removed_users of this CreateShareUpdate.  # noqa: E501
        :type: bool
        """
        if notify_removed_users is None:
            raise ValueError("Invalid value for `notify_removed_users`, must not be `None`")  # noqa: E501

        self._notify_removed_users = notify_removed_users

    @property
    def removed_user_notification_message(self):
        """Gets the removed_user_notification_message of this CreateShareUpdate.  # noqa: E501

        If removed users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message.  # noqa: E501

        :return: The removed_user_notification_message of this CreateShareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._removed_user_notification_message

    @removed_user_notification_message.setter
    def removed_user_notification_message(self, removed_user_notification_message):
        """Sets the removed_user_notification_message of this CreateShareUpdate.

        If removed users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message.  # noqa: E501

        :param removed_user_notification_message: The removed_user_notification_message of this CreateShareUpdate.  # noqa: E501
        :type: str
        """

        self._removed_user_notification_message = removed_user_notification_message

    @property
    def notify_unchanged_users(self):
        """Gets the notify_unchanged_users of this CreateShareUpdate.  # noqa: E501

        Whether to notify users that the shareable item is shared with, but that haven't   been added or removed that the share has been updated  # noqa: E501

        :return: The notify_unchanged_users of this CreateShareUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._notify_unchanged_users

    @notify_unchanged_users.setter
    def notify_unchanged_users(self, notify_unchanged_users):
        """Sets the notify_unchanged_users of this CreateShareUpdate.

        Whether to notify users that the shareable item is shared with, but that haven't   been added or removed that the share has been updated  # noqa: E501

        :param notify_unchanged_users: The notify_unchanged_users of this CreateShareUpdate.  # noqa: E501
        :type: bool
        """
        if notify_unchanged_users is None:
            raise ValueError("Invalid value for `notify_unchanged_users`, must not be `None`")  # noqa: E501

        self._notify_unchanged_users = notify_unchanged_users

    @property
    def unchanged_user_notification_message(self):
        """Gets the unchanged_user_notification_message of this CreateShareUpdate.  # noqa: E501

        If unchanged users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message.  # noqa: E501

        :return: The unchanged_user_notification_message of this CreateShareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._unchanged_user_notification_message

    @unchanged_user_notification_message.setter
    def unchanged_user_notification_message(self, unchanged_user_notification_message):
        """Sets the unchanged_user_notification_message of this CreateShareUpdate.

        If unchanged users are to be notified, this is the message to be sent to them.  The URL of the view of the shareable item (specified when the shareable item was created)  will be added to the notification after this message.  # noqa: E501

        :param unchanged_user_notification_message: The unchanged_user_notification_message of this CreateShareUpdate.  # noqa: E501
        :type: str
        """

        self._unchanged_user_notification_message = unchanged_user_notification_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateShareUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
