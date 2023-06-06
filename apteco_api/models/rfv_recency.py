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


class RFVRecency(object):
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
        'variable_name': 'str',
        'sequence': 'str',
        'direction': 'str',
        'value': 'int',
        'distinct': 'bool'
    }

    attribute_map = {
        'variable_name': 'variableName',
        'sequence': 'sequence',
        'direction': 'direction',
        'value': 'value',
        'distinct': 'distinct'
    }

    def __init__(self, variable_name=None, sequence=None, direction=None, value=None, distinct=None, local_vars_configuration=None):  # noqa: E501
        """RFVRecency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._variable_name = None
        self._sequence = None
        self._direction = None
        self._value = None
        self._distinct = None
        self.discriminator = None

        if variable_name is not None:
            self.variable_name = variable_name
        if sequence is not None:
            self.sequence = sequence
        if direction is not None:
            self.direction = direction
        if value is not None:
            self.value = value
        if distinct is not None:
            self.distinct = distinct

    @property
    def variable_name(self):
        """Gets the variable_name of this RFVRecency.  # noqa: E501


        :return: The variable_name of this RFVRecency.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this RFVRecency.


        :param variable_name: The variable_name of this RFVRecency.  # noqa: E501
        :type: str
        """

        self._variable_name = variable_name

    @property
    def sequence(self):
        """Gets the sequence of this RFVRecency.  # noqa: E501


        :return: The sequence of this RFVRecency.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this RFVRecency.


        :param sequence: The sequence of this RFVRecency.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

    @property
    def direction(self):
        """Gets the direction of this RFVRecency.  # noqa: E501


        :return: The direction of this RFVRecency.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this RFVRecency.


        :param direction: The direction of this RFVRecency.  # noqa: E501
        :type: str
        """
        allowed_values = ["Any", "First", "Last", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and direction not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def value(self):
        """Gets the value of this RFVRecency.  # noqa: E501


        :return: The value of this RFVRecency.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RFVRecency.


        :param value: The value of this RFVRecency.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def distinct(self):
        """Gets the distinct of this RFVRecency.  # noqa: E501


        :return: The distinct of this RFVRecency.  # noqa: E501
        :rtype: bool
        """
        return self._distinct

    @distinct.setter
    def distinct(self, distinct):
        """Sets the distinct of this RFVRecency.


        :param distinct: The distinct of this RFVRecency.  # noqa: E501
        :type: bool
        """

        self._distinct = distinct

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
        if not isinstance(other, RFVRecency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RFVRecency):
            return True

        return self.to_dict() != other.to_dict()
