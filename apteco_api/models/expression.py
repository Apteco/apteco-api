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


class Expression(object):
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
        'table_name': 'str',
        'queries': 'list[Query]',
        'desc': 'str',
        'display_text': 'str',
        'server_text': 'str',
        'query_descriptions': 'list[str]',
        'output_type': 'str',
        'string_size': 'int'
    }

    attribute_map = {
        'table_name': 'tableName',
        'queries': 'queries',
        'desc': 'desc',
        'display_text': 'displayText',
        'server_text': 'serverText',
        'query_descriptions': 'queryDescriptions',
        'output_type': 'outputType',
        'string_size': 'stringSize'
    }

    def __init__(self, table_name=None, queries=None, desc=None, display_text=None, server_text=None, query_descriptions=None, output_type=None, string_size=None):  # noqa: E501
        """Expression - a model defined in OpenAPI"""  # noqa: E501

        self._table_name = None
        self._queries = None
        self._desc = None
        self._display_text = None
        self._server_text = None
        self._query_descriptions = None
        self._output_type = None
        self._string_size = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if queries is not None:
            self.queries = queries
        if desc is not None:
            self.desc = desc
        if display_text is not None:
            self.display_text = display_text
        if server_text is not None:
            self.server_text = server_text
        if query_descriptions is not None:
            self.query_descriptions = query_descriptions
        if output_type is not None:
            self.output_type = output_type
        if string_size is not None:
            self.string_size = string_size

    @property
    def table_name(self):
        """Gets the table_name of this Expression.  # noqa: E501


        :return: The table_name of this Expression.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this Expression.


        :param table_name: The table_name of this Expression.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    @property
    def queries(self):
        """Gets the queries of this Expression.  # noqa: E501


        :return: The queries of this Expression.  # noqa: E501
        :rtype: list[Query]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this Expression.


        :param queries: The queries of this Expression.  # noqa: E501
        :type: list[Query]
        """

        self._queries = queries

    @property
    def desc(self):
        """Gets the desc of this Expression.  # noqa: E501


        :return: The desc of this Expression.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Expression.


        :param desc: The desc of this Expression.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def display_text(self):
        """Gets the display_text of this Expression.  # noqa: E501


        :return: The display_text of this Expression.  # noqa: E501
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this Expression.


        :param display_text: The display_text of this Expression.  # noqa: E501
        :type: str
        """

        self._display_text = display_text

    @property
    def server_text(self):
        """Gets the server_text of this Expression.  # noqa: E501


        :return: The server_text of this Expression.  # noqa: E501
        :rtype: str
        """
        return self._server_text

    @server_text.setter
    def server_text(self, server_text):
        """Sets the server_text of this Expression.


        :param server_text: The server_text of this Expression.  # noqa: E501
        :type: str
        """

        self._server_text = server_text

    @property
    def query_descriptions(self):
        """Gets the query_descriptions of this Expression.  # noqa: E501


        :return: The query_descriptions of this Expression.  # noqa: E501
        :rtype: list[str]
        """
        return self._query_descriptions

    @query_descriptions.setter
    def query_descriptions(self, query_descriptions):
        """Sets the query_descriptions of this Expression.


        :param query_descriptions: The query_descriptions of this Expression.  # noqa: E501
        :type: list[str]
        """

        self._query_descriptions = query_descriptions

    @property
    def output_type(self):
        """Gets the output_type of this Expression.  # noqa: E501


        :return: The output_type of this Expression.  # noqa: E501
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """Sets the output_type of this Expression.


        :param output_type: The output_type of this Expression.  # noqa: E501
        :type: str
        """
        allowed_values = ["Double", "Integer", "String", "Date", "DateTime", "Selector"]  # noqa: E501
        if output_type not in allowed_values:
            raise ValueError(
                "Invalid value for `output_type` ({0}), must be one of {1}"  # noqa: E501
                .format(output_type, allowed_values)
            )

        self._output_type = output_type

    @property
    def string_size(self):
        """Gets the string_size of this Expression.  # noqa: E501


        :return: The string_size of this Expression.  # noqa: E501
        :rtype: int
        """
        return self._string_size

    @string_size.setter
    def string_size(self, string_size):
        """Sets the string_size of this Expression.


        :param string_size: The string_size of this Expression.  # noqa: E501
        :type: int
        """

        self._string_size = string_size

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
        if not isinstance(other, Expression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
