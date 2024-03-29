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


class DashboardContentItem(object):
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
        'id': 'str',
        'title': 'str',
        'breakpoints': 'list[Breakpoint]',
        'dashboard_item_details': 'list[DashboardContentItemDetail]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'breakpoints': 'breakpoints',
        'dashboard_item_details': 'dashboardItemDetails'
    }

    def __init__(self, id=None, title=None, breakpoints=None, dashboard_item_details=None, local_vars_configuration=None):  # noqa: E501
        """DashboardContentItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._breakpoints = None
        self._dashboard_item_details = None
        self.discriminator = None

        self.id = id
        self.title = title
        if breakpoints is not None:
            self.breakpoints = breakpoints
        if dashboard_item_details is not None:
            self.dashboard_item_details = dashboard_item_details

    @property
    def id(self):
        """Gets the id of this DashboardContentItem.  # noqa: E501

        The dashboard items id  # noqa: E501

        :return: The id of this DashboardContentItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardContentItem.

        The dashboard items id  # noqa: E501

        :param id: The id of this DashboardContentItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this DashboardContentItem.  # noqa: E501

        The dashboard items title  # noqa: E501

        :return: The title of this DashboardContentItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DashboardContentItem.

        The dashboard items title  # noqa: E501

        :param title: The title of this DashboardContentItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def breakpoints(self):
        """Gets the breakpoints of this DashboardContentItem.  # noqa: E501

        The breakpoint sizing data  # noqa: E501

        :return: The breakpoints of this DashboardContentItem.  # noqa: E501
        :rtype: list[Breakpoint]
        """
        return self._breakpoints

    @breakpoints.setter
    def breakpoints(self, breakpoints):
        """Sets the breakpoints of this DashboardContentItem.

        The breakpoint sizing data  # noqa: E501

        :param breakpoints: The breakpoints of this DashboardContentItem.  # noqa: E501
        :type: list[Breakpoint]
        """

        self._breakpoints = breakpoints

    @property
    def dashboard_item_details(self):
        """Gets the dashboard_item_details of this DashboardContentItem.  # noqa: E501

        The dashboard items details for each breakpoint  # noqa: E501

        :return: The dashboard_item_details of this DashboardContentItem.  # noqa: E501
        :rtype: list[DashboardContentItemDetail]
        """
        return self._dashboard_item_details

    @dashboard_item_details.setter
    def dashboard_item_details(self, dashboard_item_details):
        """Sets the dashboard_item_details of this DashboardContentItem.

        The dashboard items details for each breakpoint  # noqa: E501

        :param dashboard_item_details: The dashboard_item_details of this DashboardContentItem.  # noqa: E501
        :type: list[DashboardContentItemDetail]
        """

        self._dashboard_item_details = dashboard_item_details

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
        if not isinstance(other, DashboardContentItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardContentItem):
            return True

        return self.to_dict() != other.to_dict()
