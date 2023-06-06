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


class PagedResultsDashboardSummary(object):
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
        'offset': 'int',
        'count': 'int',
        'total_count': 'int',
        'list': 'list[DashboardSummary]'
    }

    attribute_map = {
        'offset': 'offset',
        'count': 'count',
        'total_count': 'totalCount',
        'list': 'list'
    }

    def __init__(self, offset=None, count=None, total_count=None, list=None, local_vars_configuration=None):  # noqa: E501
        """PagedResultsDashboardSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._offset = None
        self._count = None
        self._total_count = None
        self._list = None
        self.discriminator = None

        self.offset = offset
        self.count = count
        self.total_count = total_count
        self.list = list

    @property
    def offset(self):
        """Gets the offset of this PagedResultsDashboardSummary.  # noqa: E501

        The number of items that were skipped over from the (potentially filtered) result set  # noqa: E501

        :return: The offset of this PagedResultsDashboardSummary.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PagedResultsDashboardSummary.

        The number of items that were skipped over from the (potentially filtered) result set  # noqa: E501

        :param offset: The offset of this PagedResultsDashboardSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def count(self):
        """Gets the count of this PagedResultsDashboardSummary.  # noqa: E501

        The number of items returned in this page of the result set  # noqa: E501

        :return: The count of this PagedResultsDashboardSummary.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PagedResultsDashboardSummary.

        The number of items returned in this page of the result set  # noqa: E501

        :param count: The count of this PagedResultsDashboardSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def total_count(self):
        """Gets the total_count of this PagedResultsDashboardSummary.  # noqa: E501

        The total number of items available in the (potentially filtered) result set  # noqa: E501

        :return: The total_count of this PagedResultsDashboardSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PagedResultsDashboardSummary.

        The total number of items available in the (potentially filtered) result set  # noqa: E501

        :param total_count: The total_count of this PagedResultsDashboardSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_count is None:  # noqa: E501
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

    @property
    def list(self):
        """Gets the list of this PagedResultsDashboardSummary.  # noqa: E501

        The list of results  # noqa: E501

        :return: The list of this PagedResultsDashboardSummary.  # noqa: E501
        :rtype: list[DashboardSummary]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this PagedResultsDashboardSummary.

        The list of results  # noqa: E501

        :param list: The list of this PagedResultsDashboardSummary.  # noqa: E501
        :type: list[DashboardSummary]
        """
        if self.local_vars_configuration.client_side_validation and list is None:  # noqa: E501
            raise ValueError("Invalid value for `list`, must not be `None`")  # noqa: E501

        self._list = list

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
        if not isinstance(other, PagedResultsDashboardSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagedResultsDashboardSummary):
            return True

        return self.to_dict() != other.to_dict()
