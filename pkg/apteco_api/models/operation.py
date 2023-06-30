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


class Operation(object):
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
        'value': 'object',
        'path': 'str',
        'op': 'str',
        '_from': 'str'
    }

    attribute_map = {
        'value': 'value',
        'path': 'path',
        'op': 'op',
        '_from': 'from'
    }

    def __init__(self, value=None, path=None, op=None, _from=None, local_vars_configuration=None):  # noqa: E501
        """Operation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._path = None
        self._op = None
        self.__from = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if path is not None:
            self.path = path
        if op is not None:
            self.op = op
        if _from is not None:
            self._from = _from

    @property
    def value(self):
        """Gets the value of this Operation.  # noqa: E501


        :return: The value of this Operation.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Operation.


        :param value: The value of this Operation.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def path(self):
        """Gets the path of this Operation.  # noqa: E501


        :return: The path of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Operation.


        :param path: The path of this Operation.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def op(self):
        """Gets the op of this Operation.  # noqa: E501


        :return: The op of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this Operation.


        :param op: The op of this Operation.  # noqa: E501
        :type: str
        """

        self._op = op

    @property
    def _from(self):
        """Gets the _from of this Operation.  # noqa: E501


        :return: The _from of this Operation.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Operation.


        :param _from: The _from of this Operation.  # noqa: E501
        :type: str
        """

        self.__from = _from

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
        if not isinstance(other, Operation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Operation):
            return True

        return self.to_dict() != other.to_dict()
