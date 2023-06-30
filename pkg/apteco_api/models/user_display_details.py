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


class UserDisplayDetails(object):
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
        'username': 'str',
        'firstname': 'str',
        'surname': 'str',
        'email_address': 'str'
    }

    attribute_map = {
        'username': 'username',
        'firstname': 'firstname',
        'surname': 'surname',
        'email_address': 'emailAddress'
    }

    def __init__(self, username=None, firstname=None, surname=None, email_address=None, local_vars_configuration=None):  # noqa: E501
        """UserDisplayDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._firstname = None
        self._surname = None
        self._email_address = None
        self.discriminator = None

        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.email_address = email_address

    @property
    def username(self):
        """Gets the username of this UserDisplayDetails.  # noqa: E501

        The user's username  # noqa: E501

        :return: The username of this UserDisplayDetails.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserDisplayDetails.

        The user's username  # noqa: E501

        :param username: The username of this UserDisplayDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def firstname(self):
        """Gets the firstname of this UserDisplayDetails.  # noqa: E501

        The user's first name  # noqa: E501

        :return: The firstname of this UserDisplayDetails.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserDisplayDetails.

        The user's first name  # noqa: E501

        :param firstname: The firstname of this UserDisplayDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and firstname is None:  # noqa: E501
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501

        self._firstname = firstname

    @property
    def surname(self):
        """Gets the surname of this UserDisplayDetails.  # noqa: E501

        The user's surname  # noqa: E501

        :return: The surname of this UserDisplayDetails.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this UserDisplayDetails.

        The user's surname  # noqa: E501

        :param surname: The surname of this UserDisplayDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and surname is None:  # noqa: E501
            raise ValueError("Invalid value for `surname`, must not be `None`")  # noqa: E501

        self._surname = surname

    @property
    def email_address(self):
        """Gets the email_address of this UserDisplayDetails.  # noqa: E501

        The user's email address  # noqa: E501

        :return: The email_address of this UserDisplayDetails.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserDisplayDetails.

        The user's email address  # noqa: E501

        :param email_address: The email_address of this UserDisplayDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

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
        if not isinstance(other, UserDisplayDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserDisplayDetails):
            return True

        return self.to_dict() != other.to_dict()
