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


class UserDashboardDetail(object):
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
        'viewing_username': 'str',
        'shared_to_me': 'bool',
        'shared_by_me': 'bool',
        'base_query': 'Query',
        'dashboard_items': 'list[DashboardContentItem]',
        'base_query_lookup': 'SystemLookup',
        'theme_id': 'int',
        'logo_id': 'int',
        'id': 'int',
        'title': 'str',
        'description': 'str',
        'system_name': 'str',
        'created_on': 'datetime',
        'owner': 'UserDisplayDetails',
        'last_updated_on': 'datetime',
        'last_updated_by': 'UserDisplayDetails',
        'last_update_id': 'int',
        'number_of_users_shared_with': 'int',
        'shared_to_all': 'bool',
        'share_id': 'int',
        'deleted_on': 'datetime'
    }

    attribute_map = {
        'viewing_username': 'viewingUsername',
        'shared_to_me': 'sharedToMe',
        'shared_by_me': 'sharedByMe',
        'base_query': 'baseQuery',
        'dashboard_items': 'dashboardItems',
        'base_query_lookup': 'baseQueryLookup',
        'theme_id': 'themeId',
        'logo_id': 'logoId',
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'system_name': 'systemName',
        'created_on': 'createdOn',
        'owner': 'owner',
        'last_updated_on': 'lastUpdatedOn',
        'last_updated_by': 'lastUpdatedBy',
        'last_update_id': 'lastUpdateId',
        'number_of_users_shared_with': 'numberOfUsersSharedWith',
        'shared_to_all': 'sharedToAll',
        'share_id': 'shareId',
        'deleted_on': 'deletedOn'
    }

    def __init__(self, viewing_username=None, shared_to_me=None, shared_by_me=None, base_query=None, dashboard_items=None, base_query_lookup=None, theme_id=None, logo_id=None, id=None, title=None, description=None, system_name=None, created_on=None, owner=None, last_updated_on=None, last_updated_by=None, last_update_id=None, number_of_users_shared_with=None, shared_to_all=None, share_id=None, deleted_on=None, local_vars_configuration=None):  # noqa: E501
        """UserDashboardDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._viewing_username = None
        self._shared_to_me = None
        self._shared_by_me = None
        self._base_query = None
        self._dashboard_items = None
        self._base_query_lookup = None
        self._theme_id = None
        self._logo_id = None
        self._id = None
        self._title = None
        self._description = None
        self._system_name = None
        self._created_on = None
        self._owner = None
        self._last_updated_on = None
        self._last_updated_by = None
        self._last_update_id = None
        self._number_of_users_shared_with = None
        self._shared_to_all = None
        self._share_id = None
        self._deleted_on = None
        self.discriminator = None

        self.viewing_username = viewing_username
        self.shared_to_me = shared_to_me
        self.shared_by_me = shared_by_me
        if base_query is not None:
            self.base_query = base_query
        if dashboard_items is not None:
            self.dashboard_items = dashboard_items
        if base_query_lookup is not None:
            self.base_query_lookup = base_query_lookup
        if theme_id is not None:
            self.theme_id = theme_id
        if logo_id is not None:
            self.logo_id = logo_id
        self.id = id
        self.title = title
        if description is not None:
            self.description = description
        self.system_name = system_name
        if created_on is not None:
            self.created_on = created_on
        self.owner = owner
        if last_updated_on is not None:
            self.last_updated_on = last_updated_on
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        self.last_update_id = last_update_id
        self.number_of_users_shared_with = number_of_users_shared_with
        self.shared_to_all = shared_to_all
        if share_id is not None:
            self.share_id = share_id
        if deleted_on is not None:
            self.deleted_on = deleted_on

    @property
    def viewing_username(self):
        """Gets the viewing_username of this UserDashboardDetail.  # noqa: E501

        The username of the user that has access to this dashboard  # noqa: E501

        :return: The viewing_username of this UserDashboardDetail.  # noqa: E501
        :rtype: str
        """
        return self._viewing_username

    @viewing_username.setter
    def viewing_username(self, viewing_username):
        """Sets the viewing_username of this UserDashboardDetail.

        The username of the user that has access to this dashboard  # noqa: E501

        :param viewing_username: The viewing_username of this UserDashboardDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and viewing_username is None:  # noqa: E501
            raise ValueError("Invalid value for `viewing_username`, must not be `None`")  # noqa: E501

        self._viewing_username = viewing_username

    @property
    def shared_to_me(self):
        """Gets the shared_to_me of this UserDashboardDetail.  # noqa: E501

        Whether this dashboard has been shared to the given user by someone else  # noqa: E501

        :return: The shared_to_me of this UserDashboardDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_me

    @shared_to_me.setter
    def shared_to_me(self, shared_to_me):
        """Sets the shared_to_me of this UserDashboardDetail.

        Whether this dashboard has been shared to the given user by someone else  # noqa: E501

        :param shared_to_me: The shared_to_me of this UserDashboardDetail.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_me`, must not be `None`")  # noqa: E501

        self._shared_to_me = shared_to_me

    @property
    def shared_by_me(self):
        """Gets the shared_by_me of this UserDashboardDetail.  # noqa: E501

        Whether this dashboard has been shared to others by the given user  # noqa: E501

        :return: The shared_by_me of this UserDashboardDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_by_me

    @shared_by_me.setter
    def shared_by_me(self, shared_by_me):
        """Sets the shared_by_me of this UserDashboardDetail.

        Whether this dashboard has been shared to others by the given user  # noqa: E501

        :param shared_by_me: The shared_by_me of this UserDashboardDetail.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_by_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_by_me`, must not be `None`")  # noqa: E501

        self._shared_by_me = shared_by_me

    @property
    def base_query(self):
        """Gets the base_query of this UserDashboardDetail.  # noqa: E501


        :return: The base_query of this UserDashboardDetail.  # noqa: E501
        :rtype: Query
        """
        return self._base_query

    @base_query.setter
    def base_query(self, base_query):
        """Sets the base_query of this UserDashboardDetail.


        :param base_query: The base_query of this UserDashboardDetail.  # noqa: E501
        :type: Query
        """

        self._base_query = base_query

    @property
    def dashboard_items(self):
        """Gets the dashboard_items of this UserDashboardDetail.  # noqa: E501

        The items that are contained within the dashboard  # noqa: E501

        :return: The dashboard_items of this UserDashboardDetail.  # noqa: E501
        :rtype: list[DashboardContentItem]
        """
        return self._dashboard_items

    @dashboard_items.setter
    def dashboard_items(self, dashboard_items):
        """Sets the dashboard_items of this UserDashboardDetail.

        The items that are contained within the dashboard  # noqa: E501

        :param dashboard_items: The dashboard_items of this UserDashboardDetail.  # noqa: E501
        :type: list[DashboardContentItem]
        """

        self._dashboard_items = dashboard_items

    @property
    def base_query_lookup(self):
        """Gets the base_query_lookup of this UserDashboardDetail.  # noqa: E501


        :return: The base_query_lookup of this UserDashboardDetail.  # noqa: E501
        :rtype: SystemLookup
        """
        return self._base_query_lookup

    @base_query_lookup.setter
    def base_query_lookup(self, base_query_lookup):
        """Sets the base_query_lookup of this UserDashboardDetail.


        :param base_query_lookup: The base_query_lookup of this UserDashboardDetail.  # noqa: E501
        :type: SystemLookup
        """

        self._base_query_lookup = base_query_lookup

    @property
    def theme_id(self):
        """Gets the theme_id of this UserDashboardDetail.  # noqa: E501

        The themeId of the dashboard  # noqa: E501

        :return: The theme_id of this UserDashboardDetail.  # noqa: E501
        :rtype: int
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this UserDashboardDetail.

        The themeId of the dashboard  # noqa: E501

        :param theme_id: The theme_id of this UserDashboardDetail.  # noqa: E501
        :type: int
        """

        self._theme_id = theme_id

    @property
    def logo_id(self):
        """Gets the logo_id of this UserDashboardDetail.  # noqa: E501

        The logoId of the dashboard  # noqa: E501

        :return: The logo_id of this UserDashboardDetail.  # noqa: E501
        :rtype: int
        """
        return self._logo_id

    @logo_id.setter
    def logo_id(self, logo_id):
        """Sets the logo_id of this UserDashboardDetail.

        The logoId of the dashboard  # noqa: E501

        :param logo_id: The logo_id of this UserDashboardDetail.  # noqa: E501
        :type: int
        """

        self._logo_id = logo_id

    @property
    def id(self):
        """Gets the id of this UserDashboardDetail.  # noqa: E501

        The dashboard's id  # noqa: E501

        :return: The id of this UserDashboardDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDashboardDetail.

        The dashboard's id  # noqa: E501

        :param id: The id of this UserDashboardDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this UserDashboardDetail.  # noqa: E501

        The title of the dashboard  # noqa: E501

        :return: The title of this UserDashboardDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserDashboardDetail.

        The title of the dashboard  # noqa: E501

        :param title: The title of this UserDashboardDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this UserDashboardDetail.  # noqa: E501

        The description of the dashboard  # noqa: E501

        :return: The description of this UserDashboardDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserDashboardDetail.

        The description of the dashboard  # noqa: E501

        :param description: The description of this UserDashboardDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def system_name(self):
        """Gets the system_name of this UserDashboardDetail.  # noqa: E501

        The FastStats system that this dashboard has been created against  # noqa: E501

        :return: The system_name of this UserDashboardDetail.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this UserDashboardDetail.

        The FastStats system that this dashboard has been created against  # noqa: E501

        :param system_name: The system_name of this UserDashboardDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_name is None:  # noqa: E501
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501

        self._system_name = system_name

    @property
    def created_on(self):
        """Gets the created_on of this UserDashboardDetail.  # noqa: E501

        The date the dashboard was created  # noqa: E501

        :return: The created_on of this UserDashboardDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this UserDashboardDetail.

        The date the dashboard was created  # noqa: E501

        :param created_on: The created_on of this UserDashboardDetail.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def owner(self):
        """Gets the owner of this UserDashboardDetail.  # noqa: E501


        :return: The owner of this UserDashboardDetail.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UserDashboardDetail.


        :param owner: The owner of this UserDashboardDetail.  # noqa: E501
        :type: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def last_updated_on(self):
        """Gets the last_updated_on of this UserDashboardDetail.  # noqa: E501

        The date the dashboard was last updated  # noqa: E501

        :return: The last_updated_on of this UserDashboardDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_on

    @last_updated_on.setter
    def last_updated_on(self, last_updated_on):
        """Sets the last_updated_on of this UserDashboardDetail.

        The date the dashboard was last updated  # noqa: E501

        :param last_updated_on: The last_updated_on of this UserDashboardDetail.  # noqa: E501
        :type: datetime
        """

        self._last_updated_on = last_updated_on

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this UserDashboardDetail.  # noqa: E501


        :return: The last_updated_by of this UserDashboardDetail.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this UserDashboardDetail.


        :param last_updated_by: The last_updated_by of this UserDashboardDetail.  # noqa: E501
        :type: UserDisplayDetails
        """

        self._last_updated_by = last_updated_by

    @property
    def last_update_id(self):
        """Gets the last_update_id of this UserDashboardDetail.  # noqa: E501

        The id of the last update for this dashboard  # noqa: E501

        :return: The last_update_id of this UserDashboardDetail.  # noqa: E501
        :rtype: int
        """
        return self._last_update_id

    @last_update_id.setter
    def last_update_id(self, last_update_id):
        """Sets the last_update_id of this UserDashboardDetail.

        The id of the last update for this dashboard  # noqa: E501

        :param last_update_id: The last_update_id of this UserDashboardDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and last_update_id is None:  # noqa: E501
            raise ValueError("Invalid value for `last_update_id`, must not be `None`")  # noqa: E501

        self._last_update_id = last_update_id

    @property
    def number_of_users_shared_with(self):
        """Gets the number_of_users_shared_with of this UserDashboardDetail.  # noqa: E501

        The number of people this dashboard has been shared with  # noqa: E501

        :return: The number_of_users_shared_with of this UserDashboardDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_users_shared_with

    @number_of_users_shared_with.setter
    def number_of_users_shared_with(self, number_of_users_shared_with):
        """Sets the number_of_users_shared_with of this UserDashboardDetail.

        The number of people this dashboard has been shared with  # noqa: E501

        :param number_of_users_shared_with: The number_of_users_shared_with of this UserDashboardDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_users_shared_with is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_users_shared_with`, must not be `None`")  # noqa: E501

        self._number_of_users_shared_with = number_of_users_shared_with

    @property
    def shared_to_all(self):
        """Gets the shared_to_all of this UserDashboardDetail.  # noqa: E501

        Whether this dashboard has been shared to all users  # noqa: E501

        :return: The shared_to_all of this UserDashboardDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_all

    @shared_to_all.setter
    def shared_to_all(self, shared_to_all):
        """Sets the shared_to_all of this UserDashboardDetail.

        Whether this dashboard has been shared to all users  # noqa: E501

        :param shared_to_all: The shared_to_all of this UserDashboardDetail.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_all is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_all`, must not be `None`")  # noqa: E501

        self._shared_to_all = shared_to_all

    @property
    def share_id(self):
        """Gets the share_id of this UserDashboardDetail.  # noqa: E501

        The id of the share associated with this dashboard, or null if the  dashboard has not yet been shared  # noqa: E501

        :return: The share_id of this UserDashboardDetail.  # noqa: E501
        :rtype: int
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this UserDashboardDetail.

        The id of the share associated with this dashboard, or null if the  dashboard has not yet been shared  # noqa: E501

        :param share_id: The share_id of this UserDashboardDetail.  # noqa: E501
        :type: int
        """

        self._share_id = share_id

    @property
    def deleted_on(self):
        """Gets the deleted_on of this UserDashboardDetail.  # noqa: E501

        The date the dashboard was deleted, or null if it has not been deleted  # noqa: E501

        :return: The deleted_on of this UserDashboardDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_on

    @deleted_on.setter
    def deleted_on(self, deleted_on):
        """Sets the deleted_on of this UserDashboardDetail.

        The date the dashboard was deleted, or null if it has not been deleted  # noqa: E501

        :param deleted_on: The deleted_on of this UserDashboardDetail.  # noqa: E501
        :type: datetime
        """

        self._deleted_on = deleted_on

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
        if not isinstance(other, UserDashboardDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserDashboardDetail):
            return True

        return self.to_dict() != other.to_dict()
