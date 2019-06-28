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


class Cube(object):
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
        'base_query': 'Query',
        'resolve_table_name': 'str',
        'storage': 'str',
        'dimensions': 'list[Dimension]',
        'measures': 'list[Measure]'
    }

    attribute_map = {
        'base_query': 'baseQuery',
        'resolve_table_name': 'resolveTableName',
        'storage': 'storage',
        'dimensions': 'dimensions',
        'measures': 'measures'
    }

    def __init__(self, base_query=None, resolve_table_name=None, storage=None, dimensions=None, measures=None):  # noqa: E501
        """Cube - a model defined in OpenAPI"""  # noqa: E501

        self._base_query = None
        self._resolve_table_name = None
        self._storage = None
        self._dimensions = None
        self._measures = None
        self.discriminator = None

        self.base_query = base_query
        self.resolve_table_name = resolve_table_name
        self.storage = storage
        self.dimensions = dimensions
        self.measures = measures

    @property
    def base_query(self):
        """Gets the base_query of this Cube.  # noqa: E501


        :return: The base_query of this Cube.  # noqa: E501
        :rtype: Query
        """
        return self._base_query

    @base_query.setter
    def base_query(self, base_query):
        """Sets the base_query of this Cube.


        :param base_query: The base_query of this Cube.  # noqa: E501
        :type: Query
        """
        if base_query is None:
            raise ValueError("Invalid value for `base_query`, must not be `None`")  # noqa: E501

        self._base_query = base_query

    @property
    def resolve_table_name(self):
        """Gets the resolve_table_name of this Cube.  # noqa: E501

        The name of the table to resolve this cube to.  I.e. all the counts in the cube will be counts of entities from this table  # noqa: E501

        :return: The resolve_table_name of this Cube.  # noqa: E501
        :rtype: str
        """
        return self._resolve_table_name

    @resolve_table_name.setter
    def resolve_table_name(self, resolve_table_name):
        """Sets the resolve_table_name of this Cube.

        The name of the table to resolve this cube to.  I.e. all the counts in the cube will be counts of entities from this table  # noqa: E501

        :param resolve_table_name: The resolve_table_name of this Cube.  # noqa: E501
        :type: str
        """
        if resolve_table_name is None:
            raise ValueError("Invalid value for `resolve_table_name`, must not be `None`")  # noqa: E501

        self._resolve_table_name = resolve_table_name

    @property
    def storage(self):
        """Gets the storage of this Cube.  # noqa: E501

        How the results of the cube will be returned  # noqa: E501

        :return: The storage of this Cube.  # noqa: E501
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this Cube.

        How the results of the cube will be returned  # noqa: E501

        :param storage: The storage of this Cube.  # noqa: E501
        :type: str
        """
        if storage is None:
            raise ValueError("Invalid value for `storage`, must not be `None`")  # noqa: E501
        allowed_values = ["Full", "Sparse"]  # noqa: E501
        if storage not in allowed_values:
            raise ValueError(
                "Invalid value for `storage` ({0}), must be one of {1}"  # noqa: E501
                .format(storage, allowed_values)
            )

        self._storage = storage

    @property
    def dimensions(self):
        """Gets the dimensions of this Cube.  # noqa: E501

        The dimensions to build the cube with.  This can be one or more variables, queries, etc.  # noqa: E501

        :return: The dimensions of this Cube.  # noqa: E501
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this Cube.

        The dimensions to build the cube with.  This can be one or more variables, queries, etc.  # noqa: E501

        :param dimensions: The dimensions of this Cube.  # noqa: E501
        :type: list[Dimension]
        """
        if dimensions is None:
            raise ValueError("Invalid value for `dimensions`, must not be `None`")  # noqa: E501

        self._dimensions = dimensions

    @property
    def measures(self):
        """Gets the measures of this Cube.  # noqa: E501

        The measures to build the cube with.  This can be one or more aggregations to calculate for the specified dimensions such as counts, sums, means, etc.  # noqa: E501

        :return: The measures of this Cube.  # noqa: E501
        :rtype: list[Measure]
        """
        return self._measures

    @measures.setter
    def measures(self, measures):
        """Sets the measures of this Cube.

        The measures to build the cube with.  This can be one or more aggregations to calculate for the specified dimensions such as counts, sums, means, etc.  # noqa: E501

        :param measures: The measures of this Cube.  # noqa: E501
        :type: list[Measure]
        """
        if measures is None:
            raise ValueError("Invalid value for `measures`, must not be `None`")  # noqa: E501

        self._measures = measures

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
        if not isinstance(other, Cube):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
