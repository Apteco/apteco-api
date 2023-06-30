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


class ModifyUserDashboard(object):
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
        'dashboard': 'ModifyUserDashboardDetail',
        'id': 'int',
        'modification_type': 'str'
    }

    attribute_map = {
        'dashboard': 'dashboard',
        'id': 'id',
        'modification_type': 'modificationType'
    }

    def __init__(self, dashboard=None, id=None, modification_type=None, local_vars_configuration=None):  # noqa: E501
        """ModifyUserDashboard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dashboard = None
        self._id = None
        self._modification_type = None
        self.discriminator = None

        self.dashboard = dashboard
        self.id = id
        self.modification_type = modification_type

    @property
    def dashboard(self):
        """Gets the dashboard of this ModifyUserDashboard.  # noqa: E501


        :return: The dashboard of this ModifyUserDashboard.  # noqa: E501
        :rtype: ModifyUserDashboardDetail
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this ModifyUserDashboard.


        :param dashboard: The dashboard of this ModifyUserDashboard.  # noqa: E501
        :type: ModifyUserDashboardDetail
        """
        if self.local_vars_configuration.client_side_validation and dashboard is None:  # noqa: E501
            raise ValueError("Invalid value for `dashboard`, must not be `None`")  # noqa: E501

        self._dashboard = dashboard

    @property
    def id(self):
        """Gets the id of this ModifyUserDashboard.  # noqa: E501

        The id of the item to update  # noqa: E501

        :return: The id of this ModifyUserDashboard.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModifyUserDashboard.

        The id of the item to update  # noqa: E501

        :param id: The id of this ModifyUserDashboard.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def modification_type(self):
        """Gets the modification_type of this ModifyUserDashboard.  # noqa: E501

        The type of modification to perform.  If the type is delete or undelete, any other specified item details will be ignored  # noqa: E501

        :return: The modification_type of this ModifyUserDashboard.  # noqa: E501
        :rtype: str
        """
        return self._modification_type

    @modification_type.setter
    def modification_type(self, modification_type):
        """Sets the modification_type of this ModifyUserDashboard.

        The type of modification to perform.  If the type is delete or undelete, any other specified item details will be ignored  # noqa: E501

        :param modification_type: The modification_type of this ModifyUserDashboard.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and modification_type is None:  # noqa: E501
            raise ValueError("Invalid value for `modification_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Modify", "Delete", "Undelete"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and modification_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `modification_type` ({0}), must be one of {1}"  # noqa: E501
                .format(modification_type, allowed_values)
            )

        self._modification_type = modification_type

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
        if not isinstance(other, ModifyUserDashboard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyUserDashboard):
            return True

        return self.to_dict() != other.to_dict()
