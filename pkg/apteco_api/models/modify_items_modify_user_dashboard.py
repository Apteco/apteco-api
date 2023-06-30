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


class ModifyItemsModifyUserDashboard(object):
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
        'return_modified_item': 'bool',
        'list': 'list[ModifyUserDashboard]'
    }

    attribute_map = {
        'return_modified_item': 'returnModifiedItem',
        'list': 'list'
    }

    def __init__(self, return_modified_item=None, list=None, local_vars_configuration=None):  # noqa: E501
        """ModifyItemsModifyUserDashboard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._return_modified_item = None
        self._list = None
        self.discriminator = None

        self.return_modified_item = return_modified_item
        self.list = list

    @property
    def return_modified_item(self):
        """Gets the return_modified_item of this ModifyItemsModifyUserDashboard.  # noqa: E501

        Whether to return the modified item in the results  # noqa: E501

        :return: The return_modified_item of this ModifyItemsModifyUserDashboard.  # noqa: E501
        :rtype: bool
        """
        return self._return_modified_item

    @return_modified_item.setter
    def return_modified_item(self, return_modified_item):
        """Sets the return_modified_item of this ModifyItemsModifyUserDashboard.

        Whether to return the modified item in the results  # noqa: E501

        :param return_modified_item: The return_modified_item of this ModifyItemsModifyUserDashboard.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and return_modified_item is None:  # noqa: E501
            raise ValueError("Invalid value for `return_modified_item`, must not be `None`")  # noqa: E501

        self._return_modified_item = return_modified_item

    @property
    def list(self):
        """Gets the list of this ModifyItemsModifyUserDashboard.  # noqa: E501

        The list of items to modify  # noqa: E501

        :return: The list of this ModifyItemsModifyUserDashboard.  # noqa: E501
        :rtype: list[ModifyUserDashboard]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ModifyItemsModifyUserDashboard.

        The list of items to modify  # noqa: E501

        :param list: The list of this ModifyItemsModifyUserDashboard.  # noqa: E501
        :type: list[ModifyUserDashboard]
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
        if not isinstance(other, ModifyItemsModifyUserDashboard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyItemsModifyUserDashboard):
            return True

        return self.to_dict() != other.to_dict()
