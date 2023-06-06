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


class DataLicensingSystemDetail(object):
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
        'name': 'str',
        'is_velocity_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_velocity_enabled': 'isVelocityEnabled'
    }

    def __init__(self, name=None, is_velocity_enabled=None, local_vars_configuration=None):  # noqa: E501
        """DataLicensingSystemDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._is_velocity_enabled = None
        self.discriminator = None

        self.name = name
        if is_velocity_enabled is not None:
            self.is_velocity_enabled = is_velocity_enabled

    @property
    def name(self):
        """Gets the name of this DataLicensingSystemDetail.  # noqa: E501

        The name of the FastStats system held in the API's configuration  # noqa: E501

        :return: The name of this DataLicensingSystemDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataLicensingSystemDetail.

        The name of the FastStats system held in the API's configuration  # noqa: E501

        :param name: The name of this DataLicensingSystemDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_velocity_enabled(self):
        """Gets the is_velocity_enabled of this DataLicensingSystemDetail.  # noqa: E501

        Whether export velocity checking is enabled for this system  # noqa: E501

        :return: The is_velocity_enabled of this DataLicensingSystemDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_velocity_enabled

    @is_velocity_enabled.setter
    def is_velocity_enabled(self, is_velocity_enabled):
        """Sets the is_velocity_enabled of this DataLicensingSystemDetail.

        Whether export velocity checking is enabled for this system  # noqa: E501

        :param is_velocity_enabled: The is_velocity_enabled of this DataLicensingSystemDetail.  # noqa: E501
        :type: bool
        """

        self._is_velocity_enabled = is_velocity_enabled

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
        if not isinstance(other, DataLicensingSystemDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataLicensingSystemDetail):
            return True

        return self.to_dict() != other.to_dict()
