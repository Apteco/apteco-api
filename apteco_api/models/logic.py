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


class Logic(object):
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
        'operation': 'str',
        'operands': 'list[Clause]',
        'table_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'operation': 'operation',
        'operands': 'operands',
        'table_name': 'tableName',
        'name': 'name'
    }

    def __init__(self, operation=None, operands=None, table_name=None, name=None):  # noqa: E501
        """Logic - a model defined in OpenAPI"""  # noqa: E501

        self._operation = None
        self._operands = None
        self._table_name = None
        self._name = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if operands is not None:
            self.operands = operands
        self.table_name = table_name
        if name is not None:
            self.name = name

    @property
    def operation(self):
        """Gets the operation of this Logic.  # noqa: E501


        :return: The operation of this Logic.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this Logic.


        :param operation: The operation of this Logic.  # noqa: E501
        :type: str
        """
        allowed_values = ["INCLUDE", "ANY", "AND", "OR", "NOT", "THE"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def operands(self):
        """Gets the operands of this Logic.  # noqa: E501


        :return: The operands of this Logic.  # noqa: E501
        :rtype: list[Clause]
        """
        return self._operands

    @operands.setter
    def operands(self, operands):
        """Sets the operands of this Logic.


        :param operands: The operands of this Logic.  # noqa: E501
        :type: list[Clause]
        """

        self._operands = operands

    @property
    def table_name(self):
        """Gets the table_name of this Logic.  # noqa: E501


        :return: The table_name of this Logic.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this Logic.


        :param table_name: The table_name of this Logic.  # noqa: E501
        :type: str
        """
        if table_name is None:
            raise ValueError("Invalid value for `table_name`, must not be `None`")  # noqa: E501

        self._table_name = table_name

    @property
    def name(self):
        """Gets the name of this Logic.  # noqa: E501


        :return: The name of this Logic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Logic.


        :param name: The name of this Logic.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Logic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
