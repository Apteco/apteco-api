# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from apteco_api.configuration import Configuration


class UserCollectionDetail(object):
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
        'id': 'int',
        'owner': 'UserDisplayDetails',
        'number_of_parts': 'int',
        'number_of_users_shared_with': 'int',
        'share_id': 'int',
        'number_of_hits': 'int',
        'system_name': 'str',
        'title': 'str',
        'description': 'str',
        'creation_date': 'datetime',
        'file_path': 'str',
        'deletion_date': 'datetime'
    }

    attribute_map = {
        'viewing_username': 'viewingUsername',
        'status': 'status',
        'shared_to_me': 'sharedToMe',
        'shared_by_me': 'sharedByMe',
        'id': 'id',
        'owner': 'owner',
        'number_of_parts': 'numberOfParts',
        'number_of_users_shared_with': 'numberOfUsersSharedWith',
        'share_id': 'shareId',
        'number_of_hits': 'numberOfHits',
        'system_name': 'systemName',
        'title': 'title',
        'description': 'description',
        'creation_date': 'creationDate',
        'file_path': 'filePath',
        'deletion_date': 'deletionDate'
    }

    def __init__(self, viewing_username=None, status=None, shared_to_me=None, shared_by_me=None, id=None, owner=None, number_of_parts=None, number_of_users_shared_with=None, share_id=None, number_of_hits=None, system_name=None, title=None, description=None, creation_date=None, file_path=None, deletion_date=None, local_vars_configuration=None):  # noqa: E501
        """UserCollectionDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._viewing_username = None
        self._status = None
        self._shared_to_me = None
        self._shared_by_me = None
        self._id = None
        self._owner = None
        self._number_of_parts = None
        self._number_of_users_shared_with = None
        self._share_id = None
        self._number_of_hits = None
        self._system_name = None
        self._title = None
        self._description = None
        self._creation_date = None
        self._file_path = None
        self._deletion_date = None
        self.discriminator = None

        self.viewing_username = viewing_username
        self.status = status
        self.shared_to_me = shared_to_me
        self.shared_by_me = shared_by_me
        self.id = id
        self.owner = owner
        if number_of_parts is not None:
            self.number_of_parts = number_of_parts
        self.number_of_users_shared_with = number_of_users_shared_with
        self.share_id = share_id
        self.number_of_hits = number_of_hits
        self.system_name = system_name
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.file_path = file_path
        if deletion_date is not None:
            self.deletion_date = deletion_date

    @property
    def viewing_username(self):
        """Gets the viewing_username of this UserCollectionDetail.  # noqa: E501

        The username of the user that has access to this collection  # noqa: E501

        :return: The viewing_username of this UserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._viewing_username

    @viewing_username.setter
    def viewing_username(self, viewing_username):
        """Sets the viewing_username of this UserCollectionDetail.

        The username of the user that has access to this collection  # noqa: E501

        :param viewing_username: The viewing_username of this UserCollectionDetail.  # noqa: E501
        :type viewing_username: str
        """
        if self.local_vars_configuration.client_side_validation and viewing_username is None:  # noqa: E501
            raise ValueError("Invalid value for `viewing_username`, must not be `None`")  # noqa: E501

        self._viewing_username = viewing_username

    @property
    def status(self):
        """Gets the status of this UserCollectionDetail.  # noqa: E501

        The status of the collection  # noqa: E501

        :return: The status of this UserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserCollectionDetail.

        The status of the collection  # noqa: E501

        :param status: The status of this UserCollectionDetail.  # noqa: E501
        :type status: str
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
        """Gets the shared_to_me of this UserCollectionDetail.  # noqa: E501

        Whether this collection has been shared to the given user by someone else  # noqa: E501

        :return: The shared_to_me of this UserCollectionDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_to_me

    @shared_to_me.setter
    def shared_to_me(self, shared_to_me):
        """Sets the shared_to_me of this UserCollectionDetail.

        Whether this collection has been shared to the given user by someone else  # noqa: E501

        :param shared_to_me: The shared_to_me of this UserCollectionDetail.  # noqa: E501
        :type shared_to_me: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_to_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_to_me`, must not be `None`")  # noqa: E501

        self._shared_to_me = shared_to_me

    @property
    def shared_by_me(self):
        """Gets the shared_by_me of this UserCollectionDetail.  # noqa: E501

        Whether this collection has been shared to others by the given user  # noqa: E501

        :return: The shared_by_me of this UserCollectionDetail.  # noqa: E501
        :rtype: bool
        """
        return self._shared_by_me

    @shared_by_me.setter
    def shared_by_me(self, shared_by_me):
        """Sets the shared_by_me of this UserCollectionDetail.

        Whether this collection has been shared to others by the given user  # noqa: E501

        :param shared_by_me: The shared_by_me of this UserCollectionDetail.  # noqa: E501
        :type shared_by_me: bool
        """
        if self.local_vars_configuration.client_side_validation and shared_by_me is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_by_me`, must not be `None`")  # noqa: E501

        self._shared_by_me = shared_by_me

    @property
    def id(self):
        """Gets the id of this UserCollectionDetail.  # noqa: E501

        The collection's id  # noqa: E501

        :return: The id of this UserCollectionDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserCollectionDetail.

        The collection's id  # noqa: E501

        :param id: The id of this UserCollectionDetail.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this UserCollectionDetail.  # noqa: E501


        :return: The owner of this UserCollectionDetail.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UserCollectionDetail.


        :param owner: The owner of this UserCollectionDetail.  # noqa: E501
        :type owner: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def number_of_parts(self):
        """Gets the number_of_parts of this UserCollectionDetail.  # noqa: E501

        The number of parts within this collection  # noqa: E501

        :return: The number_of_parts of this UserCollectionDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_parts

    @number_of_parts.setter
    def number_of_parts(self, number_of_parts):
        """Sets the number_of_parts of this UserCollectionDetail.

        The number of parts within this collection  # noqa: E501

        :param number_of_parts: The number_of_parts of this UserCollectionDetail.  # noqa: E501
        :type number_of_parts: int
        """

        self._number_of_parts = number_of_parts

    @property
    def number_of_users_shared_with(self):
        """Gets the number_of_users_shared_with of this UserCollectionDetail.  # noqa: E501

        The number of people this collection has been shared with  # noqa: E501

        :return: The number_of_users_shared_with of this UserCollectionDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_users_shared_with

    @number_of_users_shared_with.setter
    def number_of_users_shared_with(self, number_of_users_shared_with):
        """Sets the number_of_users_shared_with of this UserCollectionDetail.

        The number of people this collection has been shared with  # noqa: E501

        :param number_of_users_shared_with: The number_of_users_shared_with of this UserCollectionDetail.  # noqa: E501
        :type number_of_users_shared_with: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_users_shared_with is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_users_shared_with`, must not be `None`")  # noqa: E501

        self._number_of_users_shared_with = number_of_users_shared_with

    @property
    def share_id(self):
        """Gets the share_id of this UserCollectionDetail.  # noqa: E501

        The id of the share associated with this collection, or null if the  collection has not yet been shared  # noqa: E501

        :return: The share_id of this UserCollectionDetail.  # noqa: E501
        :rtype: int
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this UserCollectionDetail.

        The id of the share associated with this collection, or null if the  collection has not yet been shared  # noqa: E501

        :param share_id: The share_id of this UserCollectionDetail.  # noqa: E501
        :type share_id: int
        """
        if self.local_vars_configuration.client_side_validation and share_id is None:  # noqa: E501
            raise ValueError("Invalid value for `share_id`, must not be `None`")  # noqa: E501

        self._share_id = share_id

    @property
    def number_of_hits(self):
        """Gets the number_of_hits of this UserCollectionDetail.  # noqa: E501

        The number of hits associated with this collection  # noqa: E501

        :return: The number_of_hits of this UserCollectionDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_hits

    @number_of_hits.setter
    def number_of_hits(self, number_of_hits):
        """Sets the number_of_hits of this UserCollectionDetail.

        The number of hits associated with this collection  # noqa: E501

        :param number_of_hits: The number_of_hits of this UserCollectionDetail.  # noqa: E501
        :type number_of_hits: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_hits is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_hits`, must not be `None`")  # noqa: E501

        self._number_of_hits = number_of_hits

    @property
    def system_name(self):
        """Gets the system_name of this UserCollectionDetail.  # noqa: E501

        The FastStats system that this collection has been created against  # noqa: E501

        :return: The system_name of this UserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this UserCollectionDetail.

        The FastStats system that this collection has been created against  # noqa: E501

        :param system_name: The system_name of this UserCollectionDetail.  # noqa: E501
        :type system_name: str
        """
        if self.local_vars_configuration.client_side_validation and system_name is None:  # noqa: E501
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501

        self._system_name = system_name

    @property
    def title(self):
        """Gets the title of this UserCollectionDetail.  # noqa: E501

        The title of the collection  # noqa: E501

        :return: The title of this UserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserCollectionDetail.

        The title of the collection  # noqa: E501

        :param title: The title of this UserCollectionDetail.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this UserCollectionDetail.  # noqa: E501

        The description of the collection  # noqa: E501

        :return: The description of this UserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserCollectionDetail.

        The description of the collection  # noqa: E501

        :param description: The description of this UserCollectionDetail.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def creation_date(self):
        """Gets the creation_date of this UserCollectionDetail.  # noqa: E501

        The date the collection was created  # noqa: E501

        :return: The creation_date of this UserCollectionDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UserCollectionDetail.

        The date the collection was created  # noqa: E501

        :param creation_date: The creation_date of this UserCollectionDetail.  # noqa: E501
        :type creation_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_date is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def file_path(self):
        """Gets the file_path of this UserCollectionDetail.  # noqa: E501

        The path to the file that contains the parts of this collection  # noqa: E501

        :return: The file_path of this UserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this UserCollectionDetail.

        The path to the file that contains the parts of this collection  # noqa: E501

        :param file_path: The file_path of this UserCollectionDetail.  # noqa: E501
        :type file_path: str
        """
        if self.local_vars_configuration.client_side_validation and file_path is None:  # noqa: E501
            raise ValueError("Invalid value for `file_path`, must not be `None`")  # noqa: E501

        self._file_path = file_path

    @property
    def deletion_date(self):
        """Gets the deletion_date of this UserCollectionDetail.  # noqa: E501

        The date the collection was deleted, or null if it has not been deleted  # noqa: E501

        :return: The deletion_date of this UserCollectionDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_date

    @deletion_date.setter
    def deletion_date(self, deletion_date):
        """Sets the deletion_date of this UserCollectionDetail.

        The date the collection was deleted, or null if it has not been deleted  # noqa: E501

        :param deletion_date: The deletion_date of this UserCollectionDetail.  # noqa: E501
        :type deletion_date: datetime
        """

        self._deletion_date = deletion_date

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserCollectionDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserCollectionDetail):
            return True

        return self.to_dict() != other.to_dict()
