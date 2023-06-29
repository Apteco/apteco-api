# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from apteco_api.configuration import Configuration


class DashboardItemDataResult(object):
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
        'dimension_results': 'list[DimensionResult]',
        'measure_results': 'list[MeasureResult]',
        'count': 'Count'
    }

    attribute_map = {
        'dimension_results': 'dimensionResults',
        'measure_results': 'measureResults',
        'count': 'count'
    }

    def __init__(self, dimension_results=None, measure_results=None, count=None, local_vars_configuration=None):  # noqa: E501
        """DashboardItemDataResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dimension_results = None
        self._measure_results = None
        self._count = None
        self.discriminator = None

        if dimension_results is not None:
            self.dimension_results = dimension_results
        if measure_results is not None:
            self.measure_results = measure_results
        if count is not None:
            self.count = count

    @property
    def dimension_results(self):
        """Gets the dimension_results of this DashboardItemDataResult.  # noqa: E501

        The set of dimension results for this cube, containing the category codes and descriptions for each dimension in the cube  # noqa: E501

        :return: The dimension_results of this DashboardItemDataResult.  # noqa: E501
        :rtype: list[DimensionResult]
        """
        return self._dimension_results

    @dimension_results.setter
    def dimension_results(self, dimension_results):
        """Sets the dimension_results of this DashboardItemDataResult.

        The set of dimension results for this cube, containing the category codes and descriptions for each dimension in the cube  # noqa: E501

        :param dimension_results: The dimension_results of this DashboardItemDataResult.  # noqa: E501
        :type dimension_results: list[DimensionResult]
        """

        self._dimension_results = dimension_results

    @property
    def measure_results(self):
        """Gets the measure_results of this DashboardItemDataResult.  # noqa: E501

        The set of measure results for this cube, containing the values for each measure in the cube  # noqa: E501

        :return: The measure_results of this DashboardItemDataResult.  # noqa: E501
        :rtype: list[MeasureResult]
        """
        return self._measure_results

    @measure_results.setter
    def measure_results(self, measure_results):
        """Sets the measure_results of this DashboardItemDataResult.

        The set of measure results for this cube, containing the values for each measure in the cube  # noqa: E501

        :param measure_results: The measure_results of this DashboardItemDataResult.  # noqa: E501
        :type measure_results: list[MeasureResult]
        """

        self._measure_results = measure_results

    @property
    def count(self):
        """Gets the count of this DashboardItemDataResult.  # noqa: E501


        :return: The count of this DashboardItemDataResult.  # noqa: E501
        :rtype: Count
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DashboardItemDataResult.


        :param count: The count of this DashboardItemDataResult.  # noqa: E501
        :type count: Count
        """

        self._count = count

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
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
        if not isinstance(other, DashboardItemDataResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardItemDataResult):
            return True

        return self.to_dict() != other.to_dict()
