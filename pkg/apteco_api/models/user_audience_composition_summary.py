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


class UserAudienceCompositionSummary(object):
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
        'id': 'int',
        'description': 'str',
        'type': 'str',
        'system_name': 'str',
        'owner': 'UserDisplayDetails',
        'number_of_users_shared_with': 'int',
        'shared_to_all': 'bool',
        'share_id': 'int'
    }

    attribute_map = {
        'viewing_username': 'viewingUsername',
        'shared_to_me': 'sharedToMe',
        'shared_by_me': 'sharedByMe',
        'id': 'id',
        'description': 'description',
        'type': 'type',
        'system_name': 'systemName',
        'owner': 'owner',
        'number_of_users_shared_with': 'numberOfUsersSharedWith',
        'shared_to_all': 'sharedToAll',
        'share_id': 'shareId'
    }

    def __init__(self, viewing_username=None, shared_to_me=None, shared_by_me=None, id=None, description=None, type=None, system_name=None, owner=None, number_of_users_shared_with=None, shared_to_all=None, share_id=None, local_vars_configuration=None):  # noqa: E501
        """UserAudienceCompositionSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._viewing_username = None
        self._shared_to_me = None
        self._shared_by_me = None
        self._id = None
        self._description = None
        self._type = None
        self._system_name = None
        self._owner = None
        self._number_of_users_shared_with = None
        self._shared_to_all = None
        self._share_id = None
        self.discriminator = None

        self.viewing_username = viewing_username
        self.shared_to_me = shared_to_me
        self.shared_by_me = shared_by_me
        self.id = id
        self.description = description
        self.type = type
        self.system_name = system_name
        self.owner = owner
        self.number_of_users_shared_with = number_of_users_shared_with
        self.shared_to_all = shared_to_all
        if share_id is not None:
            self.share_id = share_id

    @property
    def viewing_username(self):
        """Gets the viewing_username of this UserAudienceCompositionSummary.  # noqa: E501

        The username of the user that has access to this audience composition  # noqa: E501

        :return: The viewing_username of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: str
        """
        return self._viewing_username

    @viewing_username.setter
    def viewing_username(self, viewing_username):
        """Sets the viewing_username of this UserAudienceCompositionSummary.

        The username of the user that has access to this audience composition  # noqa: E501

        :param viewing_username: The viewing_username of this UserAudienceCompositionSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and viewing_username is None:  # noqa: E501
            raise ValueError("Invalid value for `viewing_username`, must not be `None`")  # noqa: E501

        self._viewing_username = viewing_username

    @property
    def shared_to_me(self):
        """Gets the shared_to_me of this UserAudienceCompositionSummary.  # noqa: E501

        Whether this audience composition has been shared to the given user by someone else  # noqa: E501

        :return: The shared_to_me of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_me

    @shared_to_me.setter
    def shared_to_me(self, shared_to_me):
        """Sets the shared_to_me of this UserAudienceCompositionSummary.

        Whether this audience composition has been shared to the given user by someone else  # noqa: E501

        :param shared_to_me: The shared_to_me of this UserAudienceCompositionSummary.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_me`, must not be `None`")  # noqa: E501

        self._shared_to_me = shared_to_me

    @property
    def shared_by_me(self):
        """Gets the shared_by_me of this UserAudienceCompositionSummary.  # noqa: E501

        Whether this audience composition has been shared to others by the given user  # noqa: E501

        :return: The shared_by_me of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._shared_by_me

    @shared_by_me.setter
    def shared_by_me(self, shared_by_me):
        """Sets the shared_by_me of this UserAudienceCompositionSummary.

        Whether this audience composition has been shared to others by the given user  # noqa: E501

        :param shared_by_me: The shared_by_me of this UserAudienceCompositionSummary.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_by_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_by_me`, must not be `None`")  # noqa: E501

        self._shared_by_me = shared_by_me

    @property
    def id(self):
        """Gets the id of this UserAudienceCompositionSummary.  # noqa: E501

        The id of this composition  # noqa: E501

        :return: The id of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAudienceCompositionSummary.

        The id of this composition  # noqa: E501

        :param id: The id of this UserAudienceCompositionSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this UserAudienceCompositionSummary.  # noqa: E501

        The description of this composition  # noqa: E501

        :return: The description of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserAudienceCompositionSummary.

        The description of this composition  # noqa: E501

        :param description: The description of this UserAudienceCompositionSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this UserAudienceCompositionSummary.  # noqa: E501

        The type of this composition  # noqa: E501

        :return: The type of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserAudienceCompositionSummary.

        The type of this composition  # noqa: E501

        :param type: The type of this UserAudienceCompositionSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Check", "Export"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def system_name(self):
        """Gets the system_name of this UserAudienceCompositionSummary.  # noqa: E501

        The name of the FastStats system that this composition is for  # noqa: E501

        :return: The system_name of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this UserAudienceCompositionSummary.

        The name of the FastStats system that this composition is for  # noqa: E501

        :param system_name: The system_name of this UserAudienceCompositionSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_name is None:  # noqa: E501
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501

        self._system_name = system_name

    @property
    def owner(self):
        """Gets the owner of this UserAudienceCompositionSummary.  # noqa: E501


        :return: The owner of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UserAudienceCompositionSummary.


        :param owner: The owner of this UserAudienceCompositionSummary.  # noqa: E501
        :type: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def number_of_users_shared_with(self):
        """Gets the number_of_users_shared_with of this UserAudienceCompositionSummary.  # noqa: E501

        The number of people this composition has been shared with  # noqa: E501

        :return: The number_of_users_shared_with of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_of_users_shared_with

    @number_of_users_shared_with.setter
    def number_of_users_shared_with(self, number_of_users_shared_with):
        """Sets the number_of_users_shared_with of this UserAudienceCompositionSummary.

        The number of people this composition has been shared with  # noqa: E501

        :param number_of_users_shared_with: The number_of_users_shared_with of this UserAudienceCompositionSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_users_shared_with is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_users_shared_with`, must not be `None`")  # noqa: E501

        self._number_of_users_shared_with = number_of_users_shared_with

    @property
    def shared_to_all(self):
        """Gets the shared_to_all of this UserAudienceCompositionSummary.  # noqa: E501

        Whether this composition has been shared to all users  # noqa: E501

        :return: The shared_to_all of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_all

    @shared_to_all.setter
    def shared_to_all(self, shared_to_all):
        """Sets the shared_to_all of this UserAudienceCompositionSummary.

        Whether this composition has been shared to all users  # noqa: E501

        :param shared_to_all: The shared_to_all of this UserAudienceCompositionSummary.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_all is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_all`, must not be `None`")  # noqa: E501

        self._shared_to_all = shared_to_all

    @property
    def share_id(self):
        """Gets the share_id of this UserAudienceCompositionSummary.  # noqa: E501

        The id of the share associated with this composition, or null if the  composition has not yet been shared  # noqa: E501

        :return: The share_id of this UserAudienceCompositionSummary.  # noqa: E501
        :rtype: int
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this UserAudienceCompositionSummary.

        The id of the share associated with this composition, or null if the  composition has not yet been shared  # noqa: E501

        :param share_id: The share_id of this UserAudienceCompositionSummary.  # noqa: E501
        :type: int
        """

        self._share_id = share_id

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
        if not isinstance(other, UserAudienceCompositionSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAudienceCompositionSummary):
            return True

        return self.to_dict() != other.to_dict()
