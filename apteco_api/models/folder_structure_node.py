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


class FolderStructureNode(object):
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
        'folder': 'Folder',
        'variable': 'Variable'
    }

    attribute_map = {
        'folder': 'folder',
        'variable': 'variable'
    }

    def __init__(self, folder=None, variable=None):  # noqa: E501
        """FolderStructureNode - a model defined in OpenAPI"""  # noqa: E501

        self._folder = None
        self._variable = None
        self.discriminator = None

        if folder is not None:
            self.folder = folder
        if variable is not None:
            self.variable = variable

    @property
    def folder(self):
        """Gets the folder of this FolderStructureNode.  # noqa: E501


        :return: The folder of this FolderStructureNode.  # noqa: E501
        :rtype: Folder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this FolderStructureNode.


        :param folder: The folder of this FolderStructureNode.  # noqa: E501
        :type: Folder
        """

        self._folder = folder

    @property
    def variable(self):
        """Gets the variable of this FolderStructureNode.  # noqa: E501


        :return: The variable of this FolderStructureNode.  # noqa: E501
        :rtype: Variable
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this FolderStructureNode.


        :param variable: The variable of this FolderStructureNode.  # noqa: E501
        :type: Variable
        """

        self._variable = variable

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
        if not isinstance(other, FolderStructureNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
