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


class DashboardItemCategoryDisplay(object):
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
        'display_type': 'str',
        'limit': 'int',
        'auto_adjust': 'bool',
        'user_adjust': 'bool'
    }

    attribute_map = {
        'display_type': 'displayType',
        'limit': 'limit',
        'auto_adjust': 'autoAdjust',
        'user_adjust': 'userAdjust'
    }

    def __init__(self, display_type=None, limit=None, auto_adjust=None, user_adjust=None, local_vars_configuration=None):  # noqa: E501
        """DashboardItemCategoryDisplay - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_type = None
        self._limit = None
        self._auto_adjust = None
        self._user_adjust = None
        self.discriminator = None

        self.display_type = display_type
        self.limit = limit
        if auto_adjust is not None:
            self.auto_adjust = auto_adjust
        if user_adjust is not None:
            self.user_adjust = user_adjust

    @property
    def display_type(self):
        """Gets the display_type of this DashboardItemCategoryDisplay.  # noqa: E501

        The filter type to filter the dashboard item categories  # noqa: E501

        :return: The display_type of this DashboardItemCategoryDisplay.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this DashboardItemCategoryDisplay.

        The filter type to filter the dashboard item categories  # noqa: E501

        :param display_type: The display_type of this DashboardItemCategoryDisplay.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and display_type is None:  # noqa: E501
            raise ValueError("Invalid value for `display_type`, must not be `None`")  # noqa: E501
        allowed_values = ["All", "Top", "Bottom", "PercentageTotal", "CategoryPercentageTotal"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and display_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `display_type` ({0}), must be one of {1}"  # noqa: E501
                .format(display_type, allowed_values)
            )

        self._display_type = display_type

    @property
    def limit(self):
        """Gets the limit of this DashboardItemCategoryDisplay.  # noqa: E501

        The limit to use when displaying the dashboard item categories  # noqa: E501

        :return: The limit of this DashboardItemCategoryDisplay.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DashboardItemCategoryDisplay.

        The limit to use when displaying the dashboard item categories  # noqa: E501

        :param limit: The limit of this DashboardItemCategoryDisplay.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def auto_adjust(self):
        """Gets the auto_adjust of this DashboardItemCategoryDisplay.  # noqa: E501

        Whether to auto adjust the limit to the optimum value given the available tile space  # noqa: E501

        :return: The auto_adjust of this DashboardItemCategoryDisplay.  # noqa: E501
        :rtype: bool
        """
        return self._auto_adjust

    @auto_adjust.setter
    def auto_adjust(self, auto_adjust):
        """Sets the auto_adjust of this DashboardItemCategoryDisplay.

        Whether to auto adjust the limit to the optimum value given the available tile space  # noqa: E501

        :param auto_adjust: The auto_adjust of this DashboardItemCategoryDisplay.  # noqa: E501
        :type: bool
        """

        self._auto_adjust = auto_adjust

    @property
    def user_adjust(self):
        """Gets the user_adjust of this DashboardItemCategoryDisplay.  # noqa: E501

        Whether to allow the user to adjust the category display  # noqa: E501

        :return: The user_adjust of this DashboardItemCategoryDisplay.  # noqa: E501
        :rtype: bool
        """
        return self._user_adjust

    @user_adjust.setter
    def user_adjust(self, user_adjust):
        """Sets the user_adjust of this DashboardItemCategoryDisplay.

        Whether to allow the user to adjust the category display  # noqa: E501

        :param user_adjust: The user_adjust of this DashboardItemCategoryDisplay.  # noqa: E501
        :type: bool
        """

        self._user_adjust = user_adjust

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
        if not isinstance(other, DashboardItemCategoryDisplay):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardItemCategoryDisplay):
            return True

        return self.to_dict() != other.to_dict()
