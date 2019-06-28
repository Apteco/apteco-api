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


class ShareUpdate(object):
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
        'id': 'int',
        'timestamp': 'datetime',
        'user': 'UserDisplayDetails',
        'notes': 'str',
        'number_of_added_users': 'int',
        'first_added_user': 'UserDisplayDetails',
        'number_of_removed_users': 'int',
        'first_removed_user': 'UserDisplayDetails'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'user': 'user',
        'notes': 'notes',
        'number_of_added_users': 'numberOfAddedUsers',
        'first_added_user': 'firstAddedUser',
        'number_of_removed_users': 'numberOfRemovedUsers',
        'first_removed_user': 'firstRemovedUser'
    }

    def __init__(self, id=None, timestamp=None, user=None, notes=None, number_of_added_users=None, first_added_user=None, number_of_removed_users=None, first_removed_user=None):  # noqa: E501
        """ShareUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._timestamp = None
        self._user = None
        self._notes = None
        self._number_of_added_users = None
        self._first_added_user = None
        self._number_of_removed_users = None
        self._first_removed_user = None
        self.discriminator = None

        self.id = id
        self.timestamp = timestamp
        self.user = user
        self.notes = notes
        self.number_of_added_users = number_of_added_users
        self.first_added_user = first_added_user
        self.number_of_removed_users = number_of_removed_users
        self.first_removed_user = first_removed_user

    @property
    def id(self):
        """Gets the id of this ShareUpdate.  # noqa: E501

        The id of the update  # noqa: E501

        :return: The id of this ShareUpdate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShareUpdate.

        The id of the update  # noqa: E501

        :param id: The id of this ShareUpdate.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this ShareUpdate.  # noqa: E501

        The timestamp of when the update happened  # noqa: E501

        :return: The timestamp of this ShareUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShareUpdate.

        The timestamp of when the update happened  # noqa: E501

        :param timestamp: The timestamp of this ShareUpdate.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def user(self):
        """Gets the user of this ShareUpdate.  # noqa: E501


        :return: The user of this ShareUpdate.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ShareUpdate.


        :param user: The user of this ShareUpdate.  # noqa: E501
        :type: UserDisplayDetails
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def notes(self):
        """Gets the notes of this ShareUpdate.  # noqa: E501

        The notes associated with this share update  # noqa: E501

        :return: The notes of this ShareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ShareUpdate.

        The notes associated with this share update  # noqa: E501

        :param notes: The notes of this ShareUpdate.  # noqa: E501
        :type: str
        """
        if notes is None:
            raise ValueError("Invalid value for `notes`, must not be `None`")  # noqa: E501

        self._notes = notes

    @property
    def number_of_added_users(self):
        """Gets the number_of_added_users of this ShareUpdate.  # noqa: E501

        The number of users that were added to this share as part of this update  # noqa: E501

        :return: The number_of_added_users of this ShareUpdate.  # noqa: E501
        :rtype: int
        """
        return self._number_of_added_users

    @number_of_added_users.setter
    def number_of_added_users(self, number_of_added_users):
        """Sets the number_of_added_users of this ShareUpdate.

        The number of users that were added to this share as part of this update  # noqa: E501

        :param number_of_added_users: The number_of_added_users of this ShareUpdate.  # noqa: E501
        :type: int
        """
        if number_of_added_users is None:
            raise ValueError("Invalid value for `number_of_added_users`, must not be `None`")  # noqa: E501

        self._number_of_added_users = number_of_added_users

    @property
    def first_added_user(self):
        """Gets the first_added_user of this ShareUpdate.  # noqa: E501


        :return: The first_added_user of this ShareUpdate.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._first_added_user

    @first_added_user.setter
    def first_added_user(self, first_added_user):
        """Sets the first_added_user of this ShareUpdate.


        :param first_added_user: The first_added_user of this ShareUpdate.  # noqa: E501
        :type: UserDisplayDetails
        """
        if first_added_user is None:
            raise ValueError("Invalid value for `first_added_user`, must not be `None`")  # noqa: E501

        self._first_added_user = first_added_user

    @property
    def number_of_removed_users(self):
        """Gets the number_of_removed_users of this ShareUpdate.  # noqa: E501

        The number of users that were removed from this share as part of this update  # noqa: E501

        :return: The number_of_removed_users of this ShareUpdate.  # noqa: E501
        :rtype: int
        """
        return self._number_of_removed_users

    @number_of_removed_users.setter
    def number_of_removed_users(self, number_of_removed_users):
        """Sets the number_of_removed_users of this ShareUpdate.

        The number of users that were removed from this share as part of this update  # noqa: E501

        :param number_of_removed_users: The number_of_removed_users of this ShareUpdate.  # noqa: E501
        :type: int
        """
        if number_of_removed_users is None:
            raise ValueError("Invalid value for `number_of_removed_users`, must not be `None`")  # noqa: E501

        self._number_of_removed_users = number_of_removed_users

    @property
    def first_removed_user(self):
        """Gets the first_removed_user of this ShareUpdate.  # noqa: E501


        :return: The first_removed_user of this ShareUpdate.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._first_removed_user

    @first_removed_user.setter
    def first_removed_user(self, first_removed_user):
        """Sets the first_removed_user of this ShareUpdate.


        :param first_removed_user: The first_removed_user of this ShareUpdate.  # noqa: E501
        :type: UserDisplayDetails
        """
        if first_removed_user is None:
            raise ValueError("Invalid value for `first_removed_user`, must not be `None`")  # noqa: E501

        self._first_removed_user = first_removed_user

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
        if not isinstance(other, ShareUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
