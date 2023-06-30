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


class Capabilities(object):
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
        'supports_audiences': 'bool'
    }

    attribute_map = {
        'supports_audiences': 'supportsAudiences'
    }

    def __init__(self, supports_audiences=None, local_vars_configuration=None):  # noqa: E501
        """Capabilities - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._supports_audiences = None
        self.discriminator = None

        self.supports_audiences = supports_audiences

    @property
    def supports_audiences(self):
        """Gets the supports_audiences of this Capabilities.  # noqa: E501

        Whether the DataView in question can support audiences functionality  # noqa: E501

        :return: The supports_audiences of this Capabilities.  # noqa: E501
        :rtype: bool
        """
        return self._supports_audiences

    @supports_audiences.setter
    def supports_audiences(self, supports_audiences):
        """Sets the supports_audiences of this Capabilities.

        Whether the DataView in question can support audiences functionality  # noqa: E501

        :param supports_audiences: The supports_audiences of this Capabilities.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and supports_audiences is None:  # noqa: E501
            raise ValueError("Invalid value for `supports_audiences`, must not be `None`")  # noqa: E501

        self._supports_audiences = supports_audiences

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
        if not isinstance(other, Capabilities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Capabilities):
            return True

        return self.to_dict() != other.to_dict()
