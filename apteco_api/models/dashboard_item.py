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


class DashboardItem(object):
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
        'variable_name': 'str',
        'size': 'Size',
        'chart_type': 'str',
        'omit_zeros': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'variable_name': 'variableName',
        'size': 'size',
        'chart_type': 'chartType',
        'omit_zeros': 'omitZeros',
        'description': 'description'
    }

    def __init__(self, variable_name=None, size=None, chart_type=None, omit_zeros=None, description=None):  # noqa: E501
        """DashboardItem - a model defined in OpenAPI"""  # noqa: E501

        self._variable_name = None
        self._size = None
        self._chart_type = None
        self._omit_zeros = None
        self._description = None
        self.discriminator = None

        self.variable_name = variable_name
        self.size = size
        self.chart_type = chart_type
        self.omit_zeros = omit_zeros
        self.description = description

    @property
    def variable_name(self):
        """Gets the variable_name of this DashboardItem.  # noqa: E501

        The name of the FastStats variable to use to calculate this dashboard item  # noqa: E501

        :return: The variable_name of this DashboardItem.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this DashboardItem.

        The name of the FastStats variable to use to calculate this dashboard item  # noqa: E501

        :param variable_name: The variable_name of this DashboardItem.  # noqa: E501
        :type: str
        """
        if variable_name is None:
            raise ValueError("Invalid value for `variable_name`, must not be `None`")  # noqa: E501

        self._variable_name = variable_name

    @property
    def size(self):
        """Gets the size of this DashboardItem.  # noqa: E501


        :return: The size of this DashboardItem.  # noqa: E501
        :rtype: Size
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DashboardItem.


        :param size: The size of this DashboardItem.  # noqa: E501
        :type: Size
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def chart_type(self):
        """Gets the chart_type of this DashboardItem.  # noqa: E501

        The type of chart to use to display this dashboard item  # noqa: E501

        :return: The chart_type of this DashboardItem.  # noqa: E501
        :rtype: str
        """
        return self._chart_type

    @chart_type.setter
    def chart_type(self, chart_type):
        """Sets the chart_type of this DashboardItem.

        The type of chart to use to display this dashboard item  # noqa: E501

        :param chart_type: The chart_type of this DashboardItem.  # noqa: E501
        :type: str
        """
        if chart_type is None:
            raise ValueError("Invalid value for `chart_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Bar", "Column", "Pie", "Donut", "Line", "UKPostArea", "NLProvinces", "NLMunicipalities", "DE2DigitPostCode", "CH2DigitPostCode", "AU2DigitPostCode", "USStates"]  # noqa: E501
        if chart_type not in allowed_values:
            raise ValueError(
                "Invalid value for `chart_type` ({0}), must be one of {1}"  # noqa: E501
                .format(chart_type, allowed_values)
            )

        self._chart_type = chart_type

    @property
    def omit_zeros(self):
        """Gets the omit_zeros of this DashboardItem.  # noqa: E501

        Whether the chart should omit categories with zero counts  # noqa: E501

        :return: The omit_zeros of this DashboardItem.  # noqa: E501
        :rtype: bool
        """
        return self._omit_zeros

    @omit_zeros.setter
    def omit_zeros(self, omit_zeros):
        """Sets the omit_zeros of this DashboardItem.

        Whether the chart should omit categories with zero counts  # noqa: E501

        :param omit_zeros: The omit_zeros of this DashboardItem.  # noqa: E501
        :type: bool
        """
        if omit_zeros is None:
            raise ValueError("Invalid value for `omit_zeros`, must not be `None`")  # noqa: E501

        self._omit_zeros = omit_zeros

    @property
    def description(self):
        """Gets the description of this DashboardItem.  # noqa: E501

        The description to use for this item  # noqa: E501

        :return: The description of this DashboardItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DashboardItem.

        The description to use for this item  # noqa: E501

        :param description: The description of this DashboardItem.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, DashboardItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
