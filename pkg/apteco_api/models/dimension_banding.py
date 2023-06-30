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


class DimensionBanding(object):
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
        'type': 'str',
        'custom_values': 'str'
    }

    attribute_map = {
        'type': 'type',
        'custom_values': 'customValues'
    }

    def __init__(self, type=None, custom_values=None, local_vars_configuration=None):  # noqa: E501
        """DimensionBanding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._custom_values = None
        self.discriminator = None

        self.type = type
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def type(self):
        """Gets the type of this DimensionBanding.  # noqa: E501

        The type of banding to use  # noqa: E501

        :return: The type of this DimensionBanding.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DimensionBanding.

        The type of banding to use  # noqa: E501

        :param type: The type of this DimensionBanding.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Years", "Quarters", "Months", "Weeks", "DayOfWeek", "WeekOfYear", "MonthOfYear", "QuarterOfYear", "DayMonthOfYear", "HourOfDay", "DayHour", "DayHourMinute", "Day", "AgeInYears", "AgeInMonths", "AgeInQuarters", "AgeInWeeks", "AgeInDays", "YearsBusiness", "QuartersBusiness", "QuarterOfYearBusiness", "MonthsBusiness", "MonthOfYearBusiness", "WeeksBusiness", "DaysBusiness", "WeekOfYearBusiness", "Custom"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def custom_values(self):
        """Gets the custom_values of this DimensionBanding.  # noqa: E501

        If the banding type is custom, than a tab-delimited list of bands to use  # noqa: E501

        :return: The custom_values of this DimensionBanding.  # noqa: E501
        :rtype: str
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this DimensionBanding.

        If the banding type is custom, than a tab-delimited list of bands to use  # noqa: E501

        :param custom_values: The custom_values of this DimensionBanding.  # noqa: E501
        :type: str
        """

        self._custom_values = custom_values

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
        if not isinstance(other, DimensionBanding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionBanding):
            return True

        return self.to_dict() != other.to_dict()
