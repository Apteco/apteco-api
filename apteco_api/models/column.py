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


class Column(object):
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
        'id': 'str',
        'variable_name': 'str',
        'query': 'Query',
        'column_header': 'str',
        'detail': 'str',
        'unclassified_format': 'str'
    }

    attribute_map = {
        'id': 'id',
        'variable_name': 'variableName',
        'query': 'query',
        'column_header': 'columnHeader',
        'detail': 'detail',
        'unclassified_format': 'unclassifiedFormat'
    }

    def __init__(self, id=None, variable_name=None, query=None, column_header=None, detail=None, unclassified_format=None, local_vars_configuration=None):  # noqa: E501
        """Column - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._variable_name = None
        self._query = None
        self._column_header = None
        self._detail = None
        self._unclassified_format = None
        self.discriminator = None

        self.id = id
        if variable_name is not None:
            self.variable_name = variable_name
        if query is not None:
            self.query = query
        self.column_header = column_header
        if detail is not None:
            self.detail = detail
        if unclassified_format is not None:
            self.unclassified_format = unclassified_format

    @property
    def id(self):
        """Gets the id of this Column.  # noqa: E501

        The id of the column  # noqa: E501

        :return: The id of this Column.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Column.

        The id of the column  # noqa: E501

        :param id: The id of this Column.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def variable_name(self):
        """Gets the variable_name of this Column.  # noqa: E501

        The variable to output in this column  # noqa: E501

        :return: The variable_name of this Column.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this Column.

        The variable to output in this column  # noqa: E501

        :param variable_name: The variable_name of this Column.  # noqa: E501
        :type: str
        """

        self._variable_name = variable_name

    @property
    def query(self):
        """Gets the query of this Column.  # noqa: E501


        :return: The query of this Column.  # noqa: E501
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Column.


        :param query: The query of this Column.  # noqa: E501
        :type: Query
        """

        self._query = query

    @property
    def column_header(self):
        """Gets the column_header of this Column.  # noqa: E501

        The text to use as the column header  # noqa: E501

        :return: The column_header of this Column.  # noqa: E501
        :rtype: str
        """
        return self._column_header

    @column_header.setter
    def column_header(self, column_header):
        """Sets the column_header of this Column.

        The text to use as the column header  # noqa: E501

        :param column_header: The column_header of this Column.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and column_header is None:  # noqa: E501
            raise ValueError("Invalid value for `column_header`, must not be `None`")  # noqa: E501

        self._column_header = column_header

    @property
    def detail(self):
        """Gets the detail of this Column.  # noqa: E501

        Whether to output the codes or descriptions for this column when data is exported to a file  # noqa: E501

        :return: The detail of this Column.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Column.

        Whether to output the codes or descriptions for this column when data is exported to a file  # noqa: E501

        :param detail: The detail of this Column.  # noqa: E501
        :type: str
        """
        allowed_values = ["Code", "Description"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and detail not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `detail` ({0}), must be one of {1}"  # noqa: E501
                .format(detail, allowed_values)
            )

        self._detail = detail

    @property
    def unclassified_format(self):
        """Gets the unclassified_format of this Column.  # noqa: E501

        How to format unclassified values for selector variables  # noqa: E501

        :return: The unclassified_format of this Column.  # noqa: E501
        :rtype: str
        """
        return self._unclassified_format

    @unclassified_format.setter
    def unclassified_format(self, unclassified_format):
        """Sets the unclassified_format of this Column.

        How to format unclassified values for selector variables  # noqa: E501

        :param unclassified_format: The unclassified_format of this Column.  # noqa: E501
        :type: str
        """
        allowed_values = ["FromDesign", "Empty"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unclassified_format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unclassified_format` ({0}), must be one of {1}"  # noqa: E501
                .format(unclassified_format, allowed_values)
            )

        self._unclassified_format = unclassified_format

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
        if not isinstance(other, Column):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Column):
            return True

        return self.to_dict() != other.to_dict()
