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


class ResourceSummary(object):
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
        'size': 'int',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'last_modified': 'lastModified'
    }

    def __init__(self, name=None, size=None, last_modified=None):  # noqa: E501
        """ResourceSummary - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._size = None
        self._last_modified = None
        self.discriminator = None

        self.name = name
        self.size = size
        self.last_modified = last_modified

    @property
    def name(self):
        """Gets the name of this ResourceSummary.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The name of this ResourceSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceSummary.

        The name of the resource  # noqa: E501

        :param name: The name of this ResourceSummary.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this ResourceSummary.  # noqa: E501

        The size of the resource in bytes  # noqa: E501

        :return: The size of this ResourceSummary.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResourceSummary.

        The size of the resource in bytes  # noqa: E501

        :param size: The size of this ResourceSummary.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def last_modified(self):
        """Gets the last_modified of this ResourceSummary.  # noqa: E501

        The datetime that the resource was last modified  # noqa: E501

        :return: The last_modified of this ResourceSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ResourceSummary.

        The datetime that the resource was last modified  # noqa: E501

        :param last_modified: The last_modified of this ResourceSummary.  # noqa: E501
        :type: datetime
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

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
        if not isinstance(other, ResourceSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
