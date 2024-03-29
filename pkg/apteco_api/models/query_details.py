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


class QueryDetails(object):
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
        'description': 'str',
        'counts': 'list[QueryDetailCount]',
        'properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'description': 'description',
        'counts': 'counts',
        'properties': 'properties'
    }

    def __init__(self, description=None, counts=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """QueryDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._counts = None
        self._properties = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if counts is not None:
            self.counts = counts
        if properties is not None:
            self.properties = properties

    @property
    def description(self):
        """Gets the description of this QueryDetails.  # noqa: E501


        :return: The description of this QueryDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryDetails.


        :param description: The description of this QueryDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def counts(self):
        """Gets the counts of this QueryDetails.  # noqa: E501


        :return: The counts of this QueryDetails.  # noqa: E501
        :rtype: list[QueryDetailCount]
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this QueryDetails.


        :param counts: The counts of this QueryDetails.  # noqa: E501
        :type: list[QueryDetailCount]
        """

        self._counts = counts

    @property
    def properties(self):
        """Gets the properties of this QueryDetails.  # noqa: E501


        :return: The properties of this QueryDetails.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this QueryDetails.


        :param properties: The properties of this QueryDetails.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

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
        if not isinstance(other, QueryDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryDetails):
            return True

        return self.to_dict() != other.to_dict()
