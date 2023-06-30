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


class UserConfigurationDetails(object):
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
        'password_requirements': 'PasswordRequirements',
        'email_requirements': 'EmailRequirements'
    }

    attribute_map = {
        'password_requirements': 'passwordRequirements',
        'email_requirements': 'emailRequirements'
    }

    def __init__(self, password_requirements=None, email_requirements=None, local_vars_configuration=None):  # noqa: E501
        """UserConfigurationDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._password_requirements = None
        self._email_requirements = None
        self.discriminator = None

        self.password_requirements = password_requirements
        self.email_requirements = email_requirements

    @property
    def password_requirements(self):
        """Gets the password_requirements of this UserConfigurationDetails.  # noqa: E501


        :return: The password_requirements of this UserConfigurationDetails.  # noqa: E501
        :rtype: PasswordRequirements
        """
        return self._password_requirements

    @password_requirements.setter
    def password_requirements(self, password_requirements):
        """Sets the password_requirements of this UserConfigurationDetails.


        :param password_requirements: The password_requirements of this UserConfigurationDetails.  # noqa: E501
        :type: PasswordRequirements
        """
        if self.local_vars_configuration.client_side_validation and password_requirements is None:  # noqa: E501
            raise ValueError("Invalid value for `password_requirements`, must not be `None`")  # noqa: E501

        self._password_requirements = password_requirements

    @property
    def email_requirements(self):
        """Gets the email_requirements of this UserConfigurationDetails.  # noqa: E501


        :return: The email_requirements of this UserConfigurationDetails.  # noqa: E501
        :rtype: EmailRequirements
        """
        return self._email_requirements

    @email_requirements.setter
    def email_requirements(self, email_requirements):
        """Sets the email_requirements of this UserConfigurationDetails.


        :param email_requirements: The email_requirements of this UserConfigurationDetails.  # noqa: E501
        :type: EmailRequirements
        """
        if self.local_vars_configuration.client_side_validation and email_requirements is None:  # noqa: E501
            raise ValueError("Invalid value for `email_requirements`, must not be `None`")  # noqa: E501

        self._email_requirements = email_requirements

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
        if not isinstance(other, UserConfigurationDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserConfigurationDetails):
            return True

        return self.to_dict() != other.to_dict()
