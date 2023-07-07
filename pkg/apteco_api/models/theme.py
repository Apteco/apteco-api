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


class Theme(object):
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
        'id': 'int',
        'name': 'str',
        'default': 'bool',
        'system_theme_id': 'int',
        'published': 'bool',
        'definition': 'ThemeDefinition',
        'logo_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'default': 'default',
        'system_theme_id': 'systemThemeId',
        'published': 'published',
        'definition': 'definition',
        'logo_id': 'logoId'
    }

    def __init__(self, id=None, name=None, default=None, system_theme_id=None, published=None, definition=None, logo_id=None, local_vars_configuration=None):  # noqa: E501
        """Theme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._default = None
        self._system_theme_id = None
        self._published = None
        self._definition = None
        self._logo_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.default = default
        self.system_theme_id = system_theme_id
        self.published = published
        self.definition = definition
        self.logo_id = logo_id

    @property
    def id(self):
        """Gets the id of this Theme.  # noqa: E501

        The theme's id  # noqa: E501

        :return: The id of this Theme.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Theme.

        The theme's id  # noqa: E501

        :param id: The id of this Theme.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Theme.  # noqa: E501

        The name of the theme  # noqa: E501

        :return: The name of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Theme.

        The name of the theme  # noqa: E501

        :param name: The name of this Theme.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def default(self):
        """Gets the default of this Theme.  # noqa: E501

        If this is the default theme to use  # noqa: E501

        :return: The default of this Theme.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Theme.

        If this is the default theme to use  # noqa: E501

        :param default: The default of this Theme.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and default is None:  # noqa: E501
            raise ValueError("Invalid value for `default`, must not be `None`")  # noqa: E501

        self._default = default

    @property
    def system_theme_id(self):
        """Gets the system_theme_id of this Theme.  # noqa: E501

        If this is a system theme - the Id of the theme  # noqa: E501

        :return: The system_theme_id of this Theme.  # noqa: E501
        :rtype: int
        """
        return self._system_theme_id

    @system_theme_id.setter
    def system_theme_id(self, system_theme_id):
        """Sets the system_theme_id of this Theme.

        If this is a system theme - the Id of the theme  # noqa: E501

        :param system_theme_id: The system_theme_id of this Theme.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and system_theme_id is None:  # noqa: E501
            raise ValueError("Invalid value for `system_theme_id`, must not be `None`")  # noqa: E501

        self._system_theme_id = system_theme_id

    @property
    def published(self):
        """Gets the published of this Theme.  # noqa: E501

        If this theme has been published  # noqa: E501

        :return: The published of this Theme.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this Theme.

        If this theme has been published  # noqa: E501

        :param published: The published of this Theme.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and published is None:  # noqa: E501
            raise ValueError("Invalid value for `published`, must not be `None`")  # noqa: E501

        self._published = published

    @property
    def definition(self):
        """Gets the definition of this Theme.  # noqa: E501


        :return: The definition of this Theme.  # noqa: E501
        :rtype: ThemeDefinition
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this Theme.


        :param definition: The definition of this Theme.  # noqa: E501
        :type: ThemeDefinition
        """
        if self.local_vars_configuration.client_side_validation and definition is None:  # noqa: E501
            raise ValueError("Invalid value for `definition`, must not be `None`")  # noqa: E501

        self._definition = definition

    @property
    def logo_id(self):
        """Gets the logo_id of this Theme.  # noqa: E501

        The Id of the Logo to use  # noqa: E501

        :return: The logo_id of this Theme.  # noqa: E501
        :rtype: int
        """
        return self._logo_id

    @logo_id.setter
    def logo_id(self, logo_id):
        """Sets the logo_id of this Theme.

        The Id of the Logo to use  # noqa: E501

        :param logo_id: The logo_id of this Theme.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and logo_id is None:  # noqa: E501
            raise ValueError("Invalid value for `logo_id`, must not be `None`")  # noqa: E501

        self._logo_id = logo_id

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
        if not isinstance(other, Theme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Theme):
            return True

        return self.to_dict() != other.to_dict()