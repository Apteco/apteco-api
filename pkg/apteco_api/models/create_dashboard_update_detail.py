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


class CreateDashboardUpdateDetail(object):
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
        'title': 'str',
        'description': 'str',
        'theme_id': 'int',
        'logo_id': 'int',
        'base_query': 'Query',
        'dashboard_items': 'list[DashboardContentItem]',
        'system_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'theme_id': 'themeId',
        'logo_id': 'logoId',
        'base_query': 'baseQuery',
        'dashboard_items': 'dashboardItems',
        'system_name': 'systemName'
    }

    def __init__(self, id=None, title=None, description=None, theme_id=None, logo_id=None, base_query=None, dashboard_items=None, system_name=None, local_vars_configuration=None):  # noqa: E501
        """CreateDashboardUpdateDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._description = None
        self._theme_id = None
        self._logo_id = None
        self._base_query = None
        self._dashboard_items = None
        self._system_name = None
        self.discriminator = None

        self.id = id
        self.title = title
        if description is not None:
            self.description = description
        if theme_id is not None:
            self.theme_id = theme_id
        if logo_id is not None:
            self.logo_id = logo_id
        if base_query is not None:
            self.base_query = base_query
        if dashboard_items is not None:
            self.dashboard_items = dashboard_items
        if system_name is not None:
            self.system_name = system_name

    @property
    def id(self):
        """Gets the id of this CreateDashboardUpdateDetail.  # noqa: E501

        The dashboard's id  # noqa: E501

        :return: The id of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateDashboardUpdateDetail.

        The dashboard's id  # noqa: E501

        :param id: The id of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this CreateDashboardUpdateDetail.  # noqa: E501

        The title of the dashboard  # noqa: E501

        :return: The title of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateDashboardUpdateDetail.

        The title of the dashboard  # noqa: E501

        :param title: The title of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this CreateDashboardUpdateDetail.  # noqa: E501

        The description of the dashboard  # noqa: E501

        :return: The description of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDashboardUpdateDetail.

        The description of the dashboard  # noqa: E501

        :param description: The description of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def theme_id(self):
        """Gets the theme_id of this CreateDashboardUpdateDetail.  # noqa: E501

        The dashboard theme id  # noqa: E501

        :return: The theme_id of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: int
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this CreateDashboardUpdateDetail.

        The dashboard theme id  # noqa: E501

        :param theme_id: The theme_id of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: int
        """

        self._theme_id = theme_id

    @property
    def logo_id(self):
        """Gets the logo_id of this CreateDashboardUpdateDetail.  # noqa: E501

        The dashboard logo id  # noqa: E501

        :return: The logo_id of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: int
        """
        return self._logo_id

    @logo_id.setter
    def logo_id(self, logo_id):
        """Sets the logo_id of this CreateDashboardUpdateDetail.

        The dashboard logo id  # noqa: E501

        :param logo_id: The logo_id of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: int
        """

        self._logo_id = logo_id

    @property
    def base_query(self):
        """Gets the base_query of this CreateDashboardUpdateDetail.  # noqa: E501


        :return: The base_query of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: Query
        """
        return self._base_query

    @base_query.setter
    def base_query(self, base_query):
        """Sets the base_query of this CreateDashboardUpdateDetail.


        :param base_query: The base_query of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: Query
        """

        self._base_query = base_query

    @property
    def dashboard_items(self):
        """Gets the dashboard_items of this CreateDashboardUpdateDetail.  # noqa: E501

        The items that are contained within the dashboard  # noqa: E501

        :return: The dashboard_items of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: list[DashboardContentItem]
        """
        return self._dashboard_items

    @dashboard_items.setter
    def dashboard_items(self, dashboard_items):
        """Sets the dashboard_items of this CreateDashboardUpdateDetail.

        The items that are contained within the dashboard  # noqa: E501

        :param dashboard_items: The dashboard_items of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: list[DashboardContentItem]
        """

        self._dashboard_items = dashboard_items

    @property
    def system_name(self):
        """Gets the system_name of this CreateDashboardUpdateDetail.  # noqa: E501

        The connected system of the dashboard  # noqa: E501

        :return: The system_name of this CreateDashboardUpdateDetail.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this CreateDashboardUpdateDetail.

        The connected system of the dashboard  # noqa: E501

        :param system_name: The system_name of this CreateDashboardUpdateDetail.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

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
        if not isinstance(other, CreateDashboardUpdateDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDashboardUpdateDetail):
            return True

        return self.to_dict() != other.to_dict()
