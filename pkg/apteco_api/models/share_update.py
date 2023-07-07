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

from apteco_api.configuration import Configuration


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
        'shared_to_all': 'bool',
        'number_of_removed_users': 'int',
        'first_removed_user': 'UserDisplayDetails',
        'number_of_added_groups': 'int',
        'first_added_group': 'GroupSummary',
        'number_of_removed_groups': 'int',
        'first_removed_group': 'GroupSummary'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'user': 'user',
        'notes': 'notes',
        'number_of_added_users': 'numberOfAddedUsers',
        'first_added_user': 'firstAddedUser',
        'shared_to_all': 'sharedToAll',
        'number_of_removed_users': 'numberOfRemovedUsers',
        'first_removed_user': 'firstRemovedUser',
        'number_of_added_groups': 'numberOfAddedGroups',
        'first_added_group': 'firstAddedGroup',
        'number_of_removed_groups': 'numberOfRemovedGroups',
        'first_removed_group': 'firstRemovedGroup'
    }

    def __init__(self, id=None, timestamp=None, user=None, notes=None, number_of_added_users=None, first_added_user=None, shared_to_all=None, number_of_removed_users=None, first_removed_user=None, number_of_added_groups=None, first_added_group=None, number_of_removed_groups=None, first_removed_group=None, local_vars_configuration=None):  # noqa: E501
        """ShareUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._timestamp = None
        self._user = None
        self._notes = None
        self._number_of_added_users = None
        self._first_added_user = None
        self._shared_to_all = None
        self._number_of_removed_users = None
        self._first_removed_user = None
        self._number_of_added_groups = None
        self._first_added_group = None
        self._number_of_removed_groups = None
        self._first_removed_group = None
        self.discriminator = None

        self.id = id
        self.timestamp = timestamp
        self.user = user
        self.notes = notes
        self.number_of_added_users = number_of_added_users
        self.first_added_user = first_added_user
        self.shared_to_all = shared_to_all
        self.number_of_removed_users = number_of_removed_users
        self.first_removed_user = first_removed_user
        self.number_of_added_groups = number_of_added_groups
        self.first_added_group = first_added_group
        self.number_of_removed_groups = number_of_removed_groups
        self.first_removed_group = first_removed_group

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
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
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
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
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
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
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
        if self.local_vars_configuration.client_side_validation and notes is None:  # noqa: E501
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
        if self.local_vars_configuration.client_side_validation and number_of_added_users is None:  # noqa: E501
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
        if self.local_vars_configuration.client_side_validation and first_added_user is None:  # noqa: E501
            raise ValueError("Invalid value for `first_added_user`, must not be `None`")  # noqa: E501

        self._first_added_user = first_added_user

    @property
    def shared_to_all(self):
        """Gets the shared_to_all of this ShareUpdate.  # noqa: E501

        Whether this share was shared to all as part of this update  # noqa: E501

        :return: The shared_to_all of this ShareUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_all

    @shared_to_all.setter
    def shared_to_all(self, shared_to_all):
        """Sets the shared_to_all of this ShareUpdate.

        Whether this share was shared to all as part of this update  # noqa: E501

        :param shared_to_all: The shared_to_all of this ShareUpdate.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_all is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_all`, must not be `None`")  # noqa: E501

        self._shared_to_all = shared_to_all

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
        if self.local_vars_configuration.client_side_validation and number_of_removed_users is None:  # noqa: E501
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
        if self.local_vars_configuration.client_side_validation and first_removed_user is None:  # noqa: E501
            raise ValueError("Invalid value for `first_removed_user`, must not be `None`")  # noqa: E501

        self._first_removed_user = first_removed_user

    @property
    def number_of_added_groups(self):
        """Gets the number_of_added_groups of this ShareUpdate.  # noqa: E501

        The number of groups that were added to this share as part of this update  # noqa: E501

        :return: The number_of_added_groups of this ShareUpdate.  # noqa: E501
        :rtype: int
        """
        return self._number_of_added_groups

    @number_of_added_groups.setter
    def number_of_added_groups(self, number_of_added_groups):
        """Sets the number_of_added_groups of this ShareUpdate.

        The number of groups that were added to this share as part of this update  # noqa: E501

        :param number_of_added_groups: The number_of_added_groups of this ShareUpdate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_added_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_added_groups`, must not be `None`")  # noqa: E501

        self._number_of_added_groups = number_of_added_groups

    @property
    def first_added_group(self):
        """Gets the first_added_group of this ShareUpdate.  # noqa: E501


        :return: The first_added_group of this ShareUpdate.  # noqa: E501
        :rtype: GroupSummary
        """
        return self._first_added_group

    @first_added_group.setter
    def first_added_group(self, first_added_group):
        """Sets the first_added_group of this ShareUpdate.


        :param first_added_group: The first_added_group of this ShareUpdate.  # noqa: E501
        :type: GroupSummary
        """
        if self.local_vars_configuration.client_side_validation and first_added_group is None:  # noqa: E501
            raise ValueError("Invalid value for `first_added_group`, must not be `None`")  # noqa: E501

        self._first_added_group = first_added_group

    @property
    def number_of_removed_groups(self):
        """Gets the number_of_removed_groups of this ShareUpdate.  # noqa: E501

        The number of groups that were removed from this share as part of this update  # noqa: E501

        :return: The number_of_removed_groups of this ShareUpdate.  # noqa: E501
        :rtype: int
        """
        return self._number_of_removed_groups

    @number_of_removed_groups.setter
    def number_of_removed_groups(self, number_of_removed_groups):
        """Sets the number_of_removed_groups of this ShareUpdate.

        The number of groups that were removed from this share as part of this update  # noqa: E501

        :param number_of_removed_groups: The number_of_removed_groups of this ShareUpdate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_removed_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_removed_groups`, must not be `None`")  # noqa: E501

        self._number_of_removed_groups = number_of_removed_groups

    @property
    def first_removed_group(self):
        """Gets the first_removed_group of this ShareUpdate.  # noqa: E501


        :return: The first_removed_group of this ShareUpdate.  # noqa: E501
        :rtype: GroupSummary
        """
        return self._first_removed_group

    @first_removed_group.setter
    def first_removed_group(self, first_removed_group):
        """Sets the first_removed_group of this ShareUpdate.


        :param first_removed_group: The first_removed_group of this ShareUpdate.  # noqa: E501
        :type: GroupSummary
        """
        if self.local_vars_configuration.client_side_validation and first_removed_group is None:  # noqa: E501
            raise ValueError("Invalid value for `first_removed_group`, must not be `None`")  # noqa: E501

        self._first_removed_group = first_removed_group

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

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShareUpdate):
            return True

        return self.to_dict() != other.to_dict()