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


class SystemLookup(object):
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
        'variables_lookup': 'list[VariableLookup]'
    }

    attribute_map = {
        'variables_lookup': 'variablesLookup'
    }

    def __init__(self, variables_lookup=None):  # noqa: E501
        """SystemLookup - a model defined in OpenAPI"""  # noqa: E501

        self._variables_lookup = None
        self.discriminator = None

        self.variables_lookup = variables_lookup

    @property
    def variables_lookup(self):
        """Gets the variables_lookup of this SystemLookup.  # noqa: E501

        A list of variable and var code descriptions  # noqa: E501

        :return: The variables_lookup of this SystemLookup.  # noqa: E501
        :rtype: list[VariableLookup]
        """
        return self._variables_lookup

    @variables_lookup.setter
    def variables_lookup(self, variables_lookup):
        """Sets the variables_lookup of this SystemLookup.

        A list of variable and var code descriptions  # noqa: E501

        :param variables_lookup: The variables_lookup of this SystemLookup.  # noqa: E501
        :type: list[VariableLookup]
        """
        if variables_lookup is None:
            raise ValueError("Invalid value for `variables_lookup`, must not be `None`")  # noqa: E501

        self._variables_lookup = variables_lookup

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
        if not isinstance(other, SystemLookup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
