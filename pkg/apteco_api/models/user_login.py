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


class UserLogin(object):
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
        'user_id': 'int',
        'username': 'str',
        'system_name': 'str',
        'client_type': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'user_id': 'userId',
        'username': 'username',
        'system_name': 'systemName',
        'client_type': 'clientType',
        'timestamp': 'timestamp'
    }

    def __init__(self, user_id=None, username=None, system_name=None, client_type=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """UserLogin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._username = None
        self._system_name = None
        self._client_type = None
        self._timestamp = None
        self.discriminator = None

        self.user_id = user_id
        self.username = username
        self.system_name = system_name
        self.client_type = client_type
        self.timestamp = timestamp

    @property
    def user_id(self):
        """Gets the user_id of this UserLogin.  # noqa: E501

        The user's id  # noqa: E501

        :return: The user_id of this UserLogin.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserLogin.

        The user's id  # noqa: E501

        :param user_id: The user_id of this UserLogin.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this UserLogin.  # noqa: E501

        The user's name  # noqa: E501

        :return: The username of this UserLogin.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserLogin.

        The user's name  # noqa: E501

        :param username: The username of this UserLogin.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def system_name(self):
        """Gets the system_name of this UserLogin.  # noqa: E501

        The system name logged in to  # noqa: E501

        :return: The system_name of this UserLogin.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this UserLogin.

        The system name logged in to  # noqa: E501

        :param system_name: The system_name of this UserLogin.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_name is None:  # noqa: E501
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501

        self._system_name = system_name

    @property
    def client_type(self):
        """Gets the client_type of this UserLogin.  # noqa: E501

        The Client Type logged in to  # noqa: E501

        :return: The client_type of this UserLogin.  # noqa: E501
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this UserLogin.

        The Client Type logged in to  # noqa: E501

        :param client_type: The client_type of this UserLogin.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_type is None:  # noqa: E501
            raise ValueError("Invalid value for `client_type`, must not be `None`")  # noqa: E501

        self._client_type = client_type

    @property
    def timestamp(self):
        """Gets the timestamp of this UserLogin.  # noqa: E501

        The DateTime of the users last login  # noqa: E501

        :return: The timestamp of this UserLogin.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UserLogin.

        The DateTime of the users last login  # noqa: E501

        :param timestamp: The timestamp of this UserLogin.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if not isinstance(other, UserLogin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserLogin):
            return True

        return self.to_dict() != other.to_dict()
