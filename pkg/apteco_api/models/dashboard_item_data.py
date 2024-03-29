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
        'global_filter_applied': 'Query',
        'drill_down_level': 'int',
        'dimension_filter': 'Query',
        'sort_order': 'str'
    }

    attribute_map = {
        'global_filter_applied': 'globalFilterApplied',
        'drill_down_level': 'drillDownLevel',
        'dimension_filter': 'dimensionFilter',
        'sort_order': 'sortOrder'
    }

    def __init__(self, global_filter_applied=None, drill_down_level=None, dimension_filter=None, sort_order=None, local_vars_configuration=None):  # noqa: E501
        """DashboardItemData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._global_filter_applied = None
        self._drill_down_level = None
        self._dimension_filter = None
        self._sort_order = None
        self.discriminator = None

        if global_filter_applied is not None:
            self.global_filter_applied = global_filter_applied
        if drill_down_level is not None:
            self.drill_down_level = drill_down_level
        if dimension_filter is not None:
            self.dimension_filter = dimension_filter
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def global_filter_applied(self):
        """Gets the global_filter_applied of this DashboardItemData.  # noqa: E501


        :return: The global_filter_applied of this DashboardItemData.  # noqa: E501
        :rtype: Query
        """
        return self._global_filter_applied

    @global_filter_applied.setter
    def global_filter_applied(self, global_filter_applied):
        """Sets the global_filter_applied of this DashboardItemData.


        :param global_filter_applied: The global_filter_applied of this DashboardItemData.  # noqa: E501
        :type: Query
        """

        self._global_filter_applied = global_filter_applied

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
        :type: int
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
        :type: Query
        """

        self._dimension_filter = dimension_filter

    @property
    def sort_order(self):
        """Gets the sort_order of this DashboardItemData.  # noqa: E501


        :return: The sort_order of this DashboardItemData.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this DashboardItemData.


        :param sort_order: The sort_order of this DashboardItemData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Natural", "AscendingByValue", "DescendingByValue"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sort_order not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

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
        if not isinstance(other, DashboardItemData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardItemData):
            return True

        return self.to_dict() != other.to_dict()
