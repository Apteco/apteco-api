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


class FileEntry(object):
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
        'name': 'str',
        'path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'type': 'type'
    }

    def __init__(self, name=None, path=None, type=None, local_vars_configuration=None):  # noqa: E501
        """FileEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._path = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.path = path
        self.type = type

    @property
    def name(self):
        """Gets the name of this FileEntry.  # noqa: E501

        The file entry's name  # noqa: E501

        :return: The name of this FileEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileEntry.

        The file entry's name  # noqa: E501

        :param name: The name of this FileEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this FileEntry.  # noqa: E501

        The file entry's full path  # noqa: E501

        :return: The path of this FileEntry.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileEntry.

        The file entry's full path  # noqa: E501

        :param path: The path of this FileEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def type(self):
        """Gets the type of this FileEntry.  # noqa: E501

        The visualisation's type  # noqa: E501

        :return: The type of this FileEntry.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileEntry.

        The visualisation's type  # noqa: E501

        :param type: The type of this FileEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "File", "Directory", "FTPDirectory", "Chart", "Cluster", "Map", "Cube", "Tree", "Venn", "DataGrid", "DecisionTree", "Expression", "ModellingEnvironment", "ModelReport", "Profile", "Report", "Segmentation", "Selection", "Storyboard", "WordCloud"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, FileEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileEntry):
            return True

        return self.to_dict() != other.to_dict()
