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


class DiagramMetadata(object):
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
        'default_currency_locale': 'str'
    }

    attribute_map = {
        'default_currency_locale': 'defaultCurrencyLocale'
    }

    def __init__(self, default_currency_locale=None, local_vars_configuration=None):  # noqa: E501
        """DiagramMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_currency_locale = None
        self.discriminator = None

        self.default_currency_locale = default_currency_locale

    @property
    def default_currency_locale(self):
        """Gets the default_currency_locale of this DiagramMetadata.  # noqa: E501

        The locale string for the default currency for cost and revenue data in the PeopleStage diagram  # noqa: E501

        :return: The default_currency_locale of this DiagramMetadata.  # noqa: E501
        :rtype: str
        """
        return self._default_currency_locale

    @default_currency_locale.setter
    def default_currency_locale(self, default_currency_locale):
        """Sets the default_currency_locale of this DiagramMetadata.

        The locale string for the default currency for cost and revenue data in the PeopleStage diagram  # noqa: E501

        :param default_currency_locale: The default_currency_locale of this DiagramMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_currency_locale is None:  # noqa: E501
            raise ValueError("Invalid value for `default_currency_locale`, must not be `None`")  # noqa: E501

        self._default_currency_locale = default_currency_locale

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
        if not isinstance(other, DiagramMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiagramMetadata):
            return True

        return self.to_dict() != other.to_dict()
