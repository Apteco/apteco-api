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


class UsersLookup(object):
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
        'user_lookup': 'list[UserSummary]',
        'group_lookup': 'list[GroupSummary]',
        'team_lookup': 'list[TeamSummary]'
    }

    attribute_map = {
        'user_lookup': 'userLookup',
        'group_lookup': 'groupLookup',
        'team_lookup': 'teamLookup'
    }

    def __init__(self, user_lookup=None, group_lookup=None, team_lookup=None, local_vars_configuration=None):  # noqa: E501
        """UsersLookup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_lookup = None
        self._group_lookup = None
        self._team_lookup = None
        self.discriminator = None

        if user_lookup is not None:
            self.user_lookup = user_lookup
        if group_lookup is not None:
            self.group_lookup = group_lookup
        if team_lookup is not None:
            self.team_lookup = team_lookup

    @property
    def user_lookup(self):
        """Gets the user_lookup of this UsersLookup.  # noqa: E501

        A list of users  # noqa: E501

        :return: The user_lookup of this UsersLookup.  # noqa: E501
        :rtype: list[UserSummary]
        """
        return self._user_lookup

    @user_lookup.setter
    def user_lookup(self, user_lookup):
        """Sets the user_lookup of this UsersLookup.

        A list of users  # noqa: E501

        :param user_lookup: The user_lookup of this UsersLookup.  # noqa: E501
        :type: list[UserSummary]
        """

        self._user_lookup = user_lookup

    @property
    def group_lookup(self):
        """Gets the group_lookup of this UsersLookup.  # noqa: E501

        A list of groups  # noqa: E501

        :return: The group_lookup of this UsersLookup.  # noqa: E501
        :rtype: list[GroupSummary]
        """
        return self._group_lookup

    @group_lookup.setter
    def group_lookup(self, group_lookup):
        """Sets the group_lookup of this UsersLookup.

        A list of groups  # noqa: E501

        :param group_lookup: The group_lookup of this UsersLookup.  # noqa: E501
        :type: list[GroupSummary]
        """

        self._group_lookup = group_lookup

    @property
    def team_lookup(self):
        """Gets the team_lookup of this UsersLookup.  # noqa: E501

        A list of teams  # noqa: E501

        :return: The team_lookup of this UsersLookup.  # noqa: E501
        :rtype: list[TeamSummary]
        """
        return self._team_lookup

    @team_lookup.setter
    def team_lookup(self, team_lookup):
        """Sets the team_lookup of this UsersLookup.

        A list of teams  # noqa: E501

        :param team_lookup: The team_lookup of this UsersLookup.  # noqa: E501
        :type: list[TeamSummary]
        """

        self._team_lookup = team_lookup

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
        if not isinstance(other, UsersLookup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersLookup):
            return True

        return self.to_dict() != other.to_dict()
