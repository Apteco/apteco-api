# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from apteco_api.configuration import Configuration


class DashboardItemData(object):
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
        'filter': 'Query',
        'drill_down_level': 'int',
        'dimension_filter': 'Query'
    }

    attribute_map = {
        'filter': 'filter',
        'drill_down_level': 'drillDownLevel',
        'dimension_filter': 'dimensionFilter'
    }

    def __init__(self, filter=None, drill_down_level=None, dimension_filter=None, local_vars_configuration=None):  # noqa: E501
        """DashboardItemData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter = None
        self._drill_down_level = None
        self._dimension_filter = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if drill_down_level is not None:
            self.drill_down_level = drill_down_level
        if dimension_filter is not None:
            self.dimension_filter = dimension_filter

    @property
    def filter(self):
        """Gets the filter of this DashboardItemData.  # noqa: E501


        :return: The filter of this DashboardItemData.  # noqa: E501
        :rtype: Query
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this DashboardItemData.


        :param filter: The filter of this DashboardItemData.  # noqa: E501
        :type filter: Query
        """

        self._filter = filter

    @property
    def drill_down_level(self):
        """Gets the drill_down_level of this DashboardItemData.  # noqa: E501


        :return: The drill_down_level of this DashboardItemData.  # noqa: E501
        :rtype: int
        """
        return self._drill_down_level

    @drill_down_level.setter
    def drill_down_level(self, drill_down_level):
        """Sets the drill_down_level of this DashboardItemData.


        :param drill_down_level: The drill_down_level of this DashboardItemData.  # noqa: E501
        :type drill_down_level: int
        """

        self._drill_down_level = drill_down_level

    @property
    def dimension_filter(self):
        """Gets the dimension_filter of this DashboardItemData.  # noqa: E501


        :return: The dimension_filter of this DashboardItemData.  # noqa: E501
        :rtype: Query
        """
        return self._dimension_filter

    @dimension_filter.setter
    def dimension_filter(self, dimension_filter):
        """Sets the dimension_filter of this DashboardItemData.


        :param dimension_filter: The dimension_filter of this DashboardItemData.  # noqa: E501
        :type dimension_filter: Query
        """

        self._dimension_filter = dimension_filter

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DashboardItemData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardItemData):
            return True

        return self.to_dict() != other.to_dict()
