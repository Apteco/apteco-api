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


class UserSummary(object):
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
        'username': 'str',
        'group_id': 'int',
        'firstname': 'str',
        'surname': 'str',
        'email_address': 'str',
        'user_disabled_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'group_id': 'groupId',
        'firstname': 'firstname',
        'surname': 'surname',
        'email_address': 'emailAddress',
        'user_disabled_date': 'userDisabledDate'
    }

    def __init__(self, id=None, username=None, group_id=None, firstname=None, surname=None, email_address=None, user_disabled_date=None, local_vars_configuration=None):  # noqa: E501
        """UserSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._group_id = None
        self._firstname = None
        self._surname = None
        self._email_address = None
        self._user_disabled_date = None
        self.discriminator = None

        self.id = id
        self.username = username
        self.group_id = group_id
        self.firstname = firstname
        self.surname = surname
        self.email_address = email_address
        self.user_disabled_date = user_disabled_date

    @property
    def id(self):
        """Gets the id of this UserSummary.  # noqa: E501

        The user's id  # noqa: E501

        :return: The id of this UserSummary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSummary.

        The user's id  # noqa: E501

        :param id: The id of this UserSummary.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserSummary.  # noqa: E501

        The user's username  # noqa: E501

        :return: The username of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserSummary.

        The user's username  # noqa: E501

        :param username: The username of this UserSummary.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def group_id(self):
        """Gets the group_id of this UserSummary.  # noqa: E501

        The id of the group the user is in (or null if they aren't allocated to a group)  # noqa: E501

        :return: The group_id of this UserSummary.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UserSummary.

        The id of the group the user is in (or null if they aren't allocated to a group)  # noqa: E501

        :param group_id: The group_id of this UserSummary.  # noqa: E501
        :type group_id: int
        """
        if self.local_vars_configuration.client_side_validation and group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def firstname(self):
        """Gets the firstname of this UserSummary.  # noqa: E501

        The user's first name  # noqa: E501

        :return: The firstname of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserSummary.

        The user's first name  # noqa: E501

        :param firstname: The firstname of this UserSummary.  # noqa: E501
        :type firstname: str
        """
        if self.local_vars_configuration.client_side_validation and firstname is None:  # noqa: E501
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501

        self._firstname = firstname

    @property
    def surname(self):
        """Gets the surname of this UserSummary.  # noqa: E501

        The user's surname  # noqa: E501

        :return: The surname of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this UserSummary.

        The user's surname  # noqa: E501

        :param surname: The surname of this UserSummary.  # noqa: E501
        :type surname: str
        """
        if self.local_vars_configuration.client_side_validation and surname is None:  # noqa: E501
            raise ValueError("Invalid value for `surname`, must not be `None`")  # noqa: E501

        self._surname = surname

    @property
    def email_address(self):
        """Gets the email_address of this UserSummary.  # noqa: E501

        The user's email address  # noqa: E501

        :return: The email_address of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserSummary.

        The user's email address  # noqa: E501

        :param email_address: The email_address of this UserSummary.  # noqa: E501
        :type email_address: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def user_disabled_date(self):
        """Gets the user_disabled_date of this UserSummary.  # noqa: E501

        The date on which the user was or will become disabled,  or null if the user has not been disabled  # noqa: E501

        :return: The user_disabled_date of this UserSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._user_disabled_date

    @user_disabled_date.setter
    def user_disabled_date(self, user_disabled_date):
        """Sets the user_disabled_date of this UserSummary.

        The date on which the user was or will become disabled,  or null if the user has not been disabled  # noqa: E501

        :param user_disabled_date: The user_disabled_date of this UserSummary.  # noqa: E501
        :type user_disabled_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and user_disabled_date is None:  # noqa: E501
            raise ValueError("Invalid value for `user_disabled_date`, must not be `None`")  # noqa: E501

        self._user_disabled_date = user_disabled_date

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
        if not isinstance(other, UserSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSummary):
            return True

        return self.to_dict() != other.to_dict()
