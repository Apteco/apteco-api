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


class UserAudienceDetail(object):
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
        'status': 'str',
        'shared_to_me': 'bool',
        'shared_by_me': 'bool',
        'brief_text': 'str',
        'exclude_query': 'Query',
        'include_query': 'Query',
        'body_query': 'Query',
        'selection_modifiers': 'SelectionModifiers',
        'queries_lookup': 'SystemLookup',
        'last_result': 'AudienceResultDetail',
        'id': 'int',
        'title': 'str',
        'description': 'str',
        'creation_date': 'datetime',
        'owner': 'UserDisplayDetails',
        'deletion_date': 'datetime',
        'resolve_table_name': 'str',
        'resolve_table_nett_count': 'int',
        'number_of_users_shared_with': 'int',
        'shared_to_all': 'bool',
        'share_id': 'int',
        'number_of_hits': 'int',
        'system_name': 'str',
        'last_updated_user': 'UserDisplayDetails',
        'last_updated_date': 'datetime',
        'last_update_id': 'int'
    }

    attribute_map = {
        'viewing_username': 'viewingUsername',
        'status': 'status',
        'shared_to_me': 'sharedToMe',
        'shared_by_me': 'sharedByMe',
        'brief_text': 'briefText',
        'exclude_query': 'excludeQuery',
        'include_query': 'includeQuery',
        'body_query': 'bodyQuery',
        'selection_modifiers': 'selectionModifiers',
        'queries_lookup': 'queriesLookup',
        'last_result': 'lastResult',
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'creation_date': 'creationDate',
        'owner': 'owner',
        'deletion_date': 'deletionDate',
        'resolve_table_name': 'resolveTableName',
        'resolve_table_nett_count': 'resolveTableNettCount',
        'number_of_users_shared_with': 'numberOfUsersSharedWith',
        'shared_to_all': 'sharedToAll',
        'share_id': 'shareId',
        'number_of_hits': 'numberOfHits',
        'system_name': 'systemName',
        'last_updated_user': 'lastUpdatedUser',
        'last_updated_date': 'lastUpdatedDate',
        'last_update_id': 'lastUpdateId'
    }

    def __init__(self, viewing_username=None, status=None, shared_to_me=None, shared_by_me=None, brief_text=None, exclude_query=None, include_query=None, body_query=None, selection_modifiers=None, queries_lookup=None, last_result=None, id=None, title=None, description=None, creation_date=None, owner=None, deletion_date=None, resolve_table_name=None, resolve_table_nett_count=None, number_of_users_shared_with=None, shared_to_all=None, share_id=None, number_of_hits=None, system_name=None, last_updated_user=None, last_updated_date=None, last_update_id=None, local_vars_configuration=None):  # noqa: E501
        """UserAudienceDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._viewing_username = None
        self._status = None
        self._shared_to_me = None
        self._shared_by_me = None
        self._brief_text = None
        self._exclude_query = None
        self._include_query = None
        self._body_query = None
        self._selection_modifiers = None
        self._queries_lookup = None
        self._last_result = None
        self._id = None
        self._title = None
        self._description = None
        self._creation_date = None
        self._owner = None
        self._deletion_date = None
        self._resolve_table_name = None
        self._resolve_table_nett_count = None
        self._number_of_users_shared_with = None
        self._shared_to_all = None
        self._share_id = None
        self._number_of_hits = None
        self._system_name = None
        self._last_updated_user = None
        self._last_updated_date = None
        self._last_update_id = None
        self.discriminator = None

        self.viewing_username = viewing_username
        self.status = status
        self.shared_to_me = shared_to_me
        self.shared_by_me = shared_by_me
        if brief_text is not None:
            self.brief_text = brief_text
        if exclude_query is not None:
            self.exclude_query = exclude_query
        if include_query is not None:
            self.include_query = include_query
        if body_query is not None:
            self.body_query = body_query
        if selection_modifiers is not None:
            self.selection_modifiers = selection_modifiers
        if queries_lookup is not None:
            self.queries_lookup = queries_lookup
        if last_result is not None:
            self.last_result = last_result
        self.id = id
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.owner = owner
        if deletion_date is not None:
            self.deletion_date = deletion_date
        self.resolve_table_name = resolve_table_name
        if resolve_table_nett_count is not None:
            self.resolve_table_nett_count = resolve_table_nett_count
        self.number_of_users_shared_with = number_of_users_shared_with
        self.shared_to_all = shared_to_all
        if share_id is not None:
            self.share_id = share_id
        self.number_of_hits = number_of_hits
        self.system_name = system_name
        self.last_updated_user = last_updated_user
        self.last_updated_date = last_updated_date
        self.last_update_id = last_update_id

    @property
    def viewing_username(self):
        """Gets the viewing_username of this UserAudienceDetail.  # noqa: E501

        The username of the user that has access to this audience  # noqa: E501

        :return: The viewing_username of this UserAudienceDetail.  # noqa: E501
        :rtype: str
        """
        return self._viewing_username

    @viewing_username.setter
    def viewing_username(self, viewing_username):
        """Sets the viewing_username of this UserAudienceDetail.

        The username of the user that has access to this audience  # noqa: E501

        :param viewing_username: The viewing_username of this UserAudienceDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and viewing_username is None:  # noqa: E501
            raise ValueError("Invalid value for `viewing_username`, must not be `None`")  # noqa: E501

        self._viewing_username = viewing_username

    @property
    def status(self):
        """Gets the status of this UserAudienceDetail.  # noqa: E501

        The status of the audience  # noqa: E501

        :return: The status of this UserAudienceDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserAudienceDetail.

        The status of the audience  # noqa: E501

        :param status: The status of this UserAudienceDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "Pinned", "Archived"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def shared_to_me(self):
        """Gets the shared_to_me of this UserAudienceDetail.  # noqa: E501

        Whether this audience has been shared to the given user by someone else  # noqa: E501

        :return: The shared_to_me of this UserAudienceDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_me

    @shared_to_me.setter
    def shared_to_me(self, shared_to_me):
        """Sets the shared_to_me of this UserAudienceDetail.

        Whether this audience has been shared to the given user by someone else  # noqa: E501

        :param shared_to_me: The shared_to_me of this UserAudienceDetail.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_me`, must not be `None`")  # noqa: E501

        self._shared_to_me = shared_to_me

    @property
    def shared_by_me(self):
        """Gets the shared_by_me of this UserAudienceDetail.  # noqa: E501

        Whether this audience has been shared to others by the given user  # noqa: E501

        :return: The shared_by_me of this UserAudienceDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_by_me

    @shared_by_me.setter
    def shared_by_me(self, shared_by_me):
        """Sets the shared_by_me of this UserAudienceDetail.

        Whether this audience has been shared to others by the given user  # noqa: E501

        :param shared_by_me: The shared_by_me of this UserAudienceDetail.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_by_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_by_me`, must not be `None`")  # noqa: E501

        self._shared_by_me = shared_by_me

    @property
    def brief_text(self):
        """Gets the brief_text of this UserAudienceDetail.  # noqa: E501

        Notes associated with the audience  # noqa: E501

        :return: The brief_text of this UserAudienceDetail.  # noqa: E501
        :rtype: str
        """
        return self._brief_text

    @brief_text.setter
    def brief_text(self, brief_text):
        """Sets the brief_text of this UserAudienceDetail.

        Notes associated with the audience  # noqa: E501

        :param brief_text: The brief_text of this UserAudienceDetail.  # noqa: E501
        :type: str
        """

        self._brief_text = brief_text

    @property
    def exclude_query(self):
        """Gets the exclude_query of this UserAudienceDetail.  # noqa: E501


        :return: The exclude_query of this UserAudienceDetail.  # noqa: E501
        :rtype: Query
        """
        return self._exclude_query

    @exclude_query.setter
    def exclude_query(self, exclude_query):
        """Sets the exclude_query of this UserAudienceDetail.


        :param exclude_query: The exclude_query of this UserAudienceDetail.  # noqa: E501
        :type: Query
        """

        self._exclude_query = exclude_query

    @property
    def include_query(self):
        """Gets the include_query of this UserAudienceDetail.  # noqa: E501


        :return: The include_query of this UserAudienceDetail.  # noqa: E501
        :rtype: Query
        """
        return self._include_query

    @include_query.setter
    def include_query(self, include_query):
        """Sets the include_query of this UserAudienceDetail.


        :param include_query: The include_query of this UserAudienceDetail.  # noqa: E501
        :type: Query
        """

        self._include_query = include_query

    @property
    def body_query(self):
        """Gets the body_query of this UserAudienceDetail.  # noqa: E501


        :return: The body_query of this UserAudienceDetail.  # noqa: E501
        :rtype: Query
        """
        return self._body_query

    @body_query.setter
    def body_query(self, body_query):
        """Sets the body_query of this UserAudienceDetail.


        :param body_query: The body_query of this UserAudienceDetail.  # noqa: E501
        :type: Query
        """

        self._body_query = body_query

    @property
    def selection_modifiers(self):
        """Gets the selection_modifiers of this UserAudienceDetail.  # noqa: E501


        :return: The selection_modifiers of this UserAudienceDetail.  # noqa: E501
        :rtype: SelectionModifiers
        """
        return self._selection_modifiers

    @selection_modifiers.setter
    def selection_modifiers(self, selection_modifiers):
        """Sets the selection_modifiers of this UserAudienceDetail.


        :param selection_modifiers: The selection_modifiers of this UserAudienceDetail.  # noqa: E501
        :type: SelectionModifiers
        """

        self._selection_modifiers = selection_modifiers

    @property
    def queries_lookup(self):
        """Gets the queries_lookup of this UserAudienceDetail.  # noqa: E501


        :return: The queries_lookup of this UserAudienceDetail.  # noqa: E501
        :rtype: SystemLookup
        """
        return self._queries_lookup

    @queries_lookup.setter
    def queries_lookup(self, queries_lookup):
        """Sets the queries_lookup of this UserAudienceDetail.


        :param queries_lookup: The queries_lookup of this UserAudienceDetail.  # noqa: E501
        :type: SystemLookup
        """

        self._queries_lookup = queries_lookup

    @property
    def last_result(self):
        """Gets the last_result of this UserAudienceDetail.  # noqa: E501


        :return: The last_result of this UserAudienceDetail.  # noqa: E501
        :rtype: AudienceResultDetail
        """
        return self._last_result

    @last_result.setter
    def last_result(self, last_result):
        """Sets the last_result of this UserAudienceDetail.


        :param last_result: The last_result of this UserAudienceDetail.  # noqa: E501
        :type: AudienceResultDetail
        """

        self._last_result = last_result

    @property
    def id(self):
        """Gets the id of this UserAudienceDetail.  # noqa: E501

        The audience's id  # noqa: E501

        :return: The id of this UserAudienceDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAudienceDetail.

        The audience's id  # noqa: E501

        :param id: The id of this UserAudienceDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this UserAudienceDetail.  # noqa: E501

        The title of the audience  # noqa: E501

        :return: The title of this UserAudienceDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserAudienceDetail.

        The title of the audience  # noqa: E501

        :param title: The title of this UserAudienceDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this UserAudienceDetail.  # noqa: E501

        The description of the audience  # noqa: E501

        :return: The description of this UserAudienceDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserAudienceDetail.

        The description of the audience  # noqa: E501

        :param description: The description of this UserAudienceDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def creation_date(self):
        """Gets the creation_date of this UserAudienceDetail.  # noqa: E501

        The date the audience was created  # noqa: E501

        :return: The creation_date of this UserAudienceDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UserAudienceDetail.

        The date the audience was created  # noqa: E501

        :param creation_date: The creation_date of this UserAudienceDetail.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_date is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def owner(self):
        """Gets the owner of this UserAudienceDetail.  # noqa: E501


        :return: The owner of this UserAudienceDetail.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UserAudienceDetail.


        :param owner: The owner of this UserAudienceDetail.  # noqa: E501
        :type: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def deletion_date(self):
        """Gets the deletion_date of this UserAudienceDetail.  # noqa: E501

        The date the audience was deleted, or null if it has not been deleted  # noqa: E501

        :return: The deletion_date of this UserAudienceDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_date

    @deletion_date.setter
    def deletion_date(self, deletion_date):
        """Sets the deletion_date of this UserAudienceDetail.

        The date the audience was deleted, or null if it has not been deleted  # noqa: E501

        :param deletion_date: The deletion_date of this UserAudienceDetail.  # noqa: E501
        :type: datetime
        """

        self._deletion_date = deletion_date

    @property
    def resolve_table_name(self):
        """Gets the resolve_table_name of this UserAudienceDetail.  # noqa: E501

        The FastStats table that the audience is defined against  # noqa: E501

        :return: The resolve_table_name of this UserAudienceDetail.  # noqa: E501
        :rtype: str
        """
        return self._resolve_table_name

    @resolve_table_name.setter
    def resolve_table_name(self, resolve_table_name):
        """Sets the resolve_table_name of this UserAudienceDetail.

        The FastStats table that the audience is defined against  # noqa: E501

        :param resolve_table_name: The resolve_table_name of this UserAudienceDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resolve_table_name is None:  # noqa: E501
            raise ValueError("Invalid value for `resolve_table_name`, must not be `None`")  # noqa: E501

        self._resolve_table_name = resolve_table_name

    @property
    def resolve_table_nett_count(self):
        """Gets the resolve_table_nett_count of this UserAudienceDetail.  # noqa: E501

        If the audience has been counted, the latest overall count for the resolve table  # noqa: E501

        :return: The resolve_table_nett_count of this UserAudienceDetail.  # noqa: E501
        :rtype: int
        """
        return self._resolve_table_nett_count

    @resolve_table_nett_count.setter
    def resolve_table_nett_count(self, resolve_table_nett_count):
        """Sets the resolve_table_nett_count of this UserAudienceDetail.

        If the audience has been counted, the latest overall count for the resolve table  # noqa: E501

        :param resolve_table_nett_count: The resolve_table_nett_count of this UserAudienceDetail.  # noqa: E501
        :type: int
        """

        self._resolve_table_nett_count = resolve_table_nett_count

    @property
    def number_of_users_shared_with(self):
        """Gets the number_of_users_shared_with of this UserAudienceDetail.  # noqa: E501

        The number of people this audience has been shared with  # noqa: E501

        :return: The number_of_users_shared_with of this UserAudienceDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_users_shared_with

    @number_of_users_shared_with.setter
    def number_of_users_shared_with(self, number_of_users_shared_with):
        """Sets the number_of_users_shared_with of this UserAudienceDetail.

        The number of people this audience has been shared with  # noqa: E501

        :param number_of_users_shared_with: The number_of_users_shared_with of this UserAudienceDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_users_shared_with is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_users_shared_with`, must not be `None`")  # noqa: E501

        self._number_of_users_shared_with = number_of_users_shared_with

    @property
    def shared_to_all(self):
        """Gets the shared_to_all of this UserAudienceDetail.  # noqa: E501

        Whether the audience has been shared to all users  # noqa: E501

        :return: The shared_to_all of this UserAudienceDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_all

    @shared_to_all.setter
    def shared_to_all(self, shared_to_all):
        """Sets the shared_to_all of this UserAudienceDetail.

        Whether the audience has been shared to all users  # noqa: E501

        :param shared_to_all: The shared_to_all of this UserAudienceDetail.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_all is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_all`, must not be `None`")  # noqa: E501

        self._shared_to_all = shared_to_all

    @property
    def share_id(self):
        """Gets the share_id of this UserAudienceDetail.  # noqa: E501

        The id of the share associated with this audience, or null if the  audience has not yet been shared  # noqa: E501

        :return: The share_id of this UserAudienceDetail.  # noqa: E501
        :rtype: int
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this UserAudienceDetail.

        The id of the share associated with this audience, or null if the  audience has not yet been shared  # noqa: E501

        :param share_id: The share_id of this UserAudienceDetail.  # noqa: E501
        :type: int
        """

        self._share_id = share_id

    @property
    def number_of_hits(self):
        """Gets the number_of_hits of this UserAudienceDetail.  # noqa: E501

        The number of hits associated with this audience  # noqa: E501

        :return: The number_of_hits of this UserAudienceDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_hits

    @number_of_hits.setter
    def number_of_hits(self, number_of_hits):
        """Sets the number_of_hits of this UserAudienceDetail.

        The number of hits associated with this audience  # noqa: E501

        :param number_of_hits: The number_of_hits of this UserAudienceDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_hits is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_hits`, must not be `None`")  # noqa: E501

        self._number_of_hits = number_of_hits

    @property
    def system_name(self):
        """Gets the system_name of this UserAudienceDetail.  # noqa: E501

        The FastStats system that this audience has been created against  # noqa: E501

        :return: The system_name of this UserAudienceDetail.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this UserAudienceDetail.

        The FastStats system that this audience has been created against  # noqa: E501

        :param system_name: The system_name of this UserAudienceDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_name is None:  # noqa: E501
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501

        self._system_name = system_name

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this UserAudienceDetail.  # noqa: E501


        :return: The last_updated_user of this UserAudienceDetail.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this UserAudienceDetail.


        :param last_updated_user: The last_updated_user of this UserAudienceDetail.  # noqa: E501
        :type: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and last_updated_user is None:  # noqa: E501
            raise ValueError("Invalid value for `last_updated_user`, must not be `None`")  # noqa: E501

        self._last_updated_user = last_updated_user

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this UserAudienceDetail.  # noqa: E501

        The date the audience was last updated  # noqa: E501

        :return: The last_updated_date of this UserAudienceDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this UserAudienceDetail.

        The date the audience was last updated  # noqa: E501

        :param last_updated_date: The last_updated_date of this UserAudienceDetail.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_updated_date is None:  # noqa: E501
            raise ValueError("Invalid value for `last_updated_date`, must not be `None`")  # noqa: E501

        self._last_updated_date = last_updated_date

    @property
    def last_update_id(self):
        """Gets the last_update_id of this UserAudienceDetail.  # noqa: E501

        The id of the last update for this audience  # noqa: E501

        :return: The last_update_id of this UserAudienceDetail.  # noqa: E501
        :rtype: int
        """
        return self._last_update_id

    @last_update_id.setter
    def last_update_id(self, last_update_id):
        """Sets the last_update_id of this UserAudienceDetail.

        The id of the last update for this audience  # noqa: E501

        :param last_update_id: The last_update_id of this UserAudienceDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and last_update_id is None:  # noqa: E501
            raise ValueError("Invalid value for `last_update_id`, must not be `None`")  # noqa: E501

        self._last_update_id = last_update_id

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
        if not isinstance(other, UserAudienceDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAudienceDetail):
            return True

        return self.to_dict() != other.to_dict()
