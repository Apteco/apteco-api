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


class PerChannelStatistics(object):
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
        'communications_counts': 'list[int]',
        'costs': 'list[float]',
        'total_communications_count': 'int',
        'total_cost': 'float'
    }

    attribute_map = {
        'communications_counts': 'communicationsCounts',
        'costs': 'costs',
        'total_communications_count': 'totalCommunicationsCount',
        'total_cost': 'totalCost'
    }

    def __init__(self, communications_counts=None, costs=None, total_communications_count=None, total_cost=None, local_vars_configuration=None):  # noqa: E501
        """PerChannelStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._communications_counts = None
        self._costs = None
        self._total_communications_count = None
        self._total_cost = None
        self.discriminator = None

        self.communications_counts = communications_counts
        self.costs = costs
        self.total_communications_count = total_communications_count
        self.total_cost = total_cost

    @property
    def communications_counts(self):
        """Gets the communications_counts of this PerChannelStatistics.  # noqa: E501

        The set of counts representing the number of communications for the corresponding channel.  The first figure is data for the first day in the days list in the parent object, and so on.  # noqa: E501

        :return: The communications_counts of this PerChannelStatistics.  # noqa: E501
        :rtype: list[int]
        """
        return self._communications_counts

    @communications_counts.setter
    def communications_counts(self, communications_counts):
        """Sets the communications_counts of this PerChannelStatistics.

        The set of counts representing the number of communications for the corresponding channel.  The first figure is data for the first day in the days list in the parent object, and so on.  # noqa: E501

        :param communications_counts: The communications_counts of this PerChannelStatistics.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and communications_counts is None:  # noqa: E501
            raise ValueError("Invalid value for `communications_counts`, must not be `None`")  # noqa: E501

        self._communications_counts = communications_counts

    @property
    def costs(self):
        """Gets the costs of this PerChannelStatistics.  # noqa: E501

        The set of figures representing the total cost for the corresponding channel.  The first figure is data for the first day in the days list in the parent object, and so on.  # noqa: E501

        :return: The costs of this PerChannelStatistics.  # noqa: E501
        :rtype: list[float]
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this PerChannelStatistics.

        The set of figures representing the total cost for the corresponding channel.  The first figure is data for the first day in the days list in the parent object, and so on.  # noqa: E501

        :param costs: The costs of this PerChannelStatistics.  # noqa: E501
        :type: list[float]
        """
        if self.local_vars_configuration.client_side_validation and costs is None:  # noqa: E501
            raise ValueError("Invalid value for `costs`, must not be `None`")  # noqa: E501

        self._costs = costs

    @property
    def total_communications_count(self):
        """Gets the total_communications_count of this PerChannelStatistics.  # noqa: E501

        The total number of communications  # noqa: E501

        :return: The total_communications_count of this PerChannelStatistics.  # noqa: E501
        :rtype: int
        """
        return self._total_communications_count

    @total_communications_count.setter
    def total_communications_count(self, total_communications_count):
        """Sets the total_communications_count of this PerChannelStatistics.

        The total number of communications  # noqa: E501

        :param total_communications_count: The total_communications_count of this PerChannelStatistics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_communications_count is None:  # noqa: E501
            raise ValueError("Invalid value for `total_communications_count`, must not be `None`")  # noqa: E501

        self._total_communications_count = total_communications_count

    @property
    def total_cost(self):
        """Gets the total_cost of this PerChannelStatistics.  # noqa: E501

        The total cost  # noqa: E501

        :return: The total_cost of this PerChannelStatistics.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this PerChannelStatistics.

        The total cost  # noqa: E501

        :param total_cost: The total_cost of this PerChannelStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_cost is None:  # noqa: E501
            raise ValueError("Invalid value for `total_cost`, must not be `None`")  # noqa: E501

        self._total_cost = total_cost

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
        if not isinstance(other, PerChannelStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerChannelStatistics):
            return True

        return self.to_dict() != other.to_dict()
