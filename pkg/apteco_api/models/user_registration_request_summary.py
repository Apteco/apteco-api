# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from apteco_api.configuration import Configuration


class UserRegistrationRequestSummary(object):
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
        'token': 'str',
        'username': 'str',
        'firstname': 'str',
        'surname': 'str',
        'email_address': 'str',
        'creation_date': 'datetime',
        'confirmed_date': 'datetime',
        'expired_date': 'datetime'
    }

    attribute_map = {
        'token': 'token',
        'username': 'username',
        'firstname': 'firstname',
        'surname': 'surname',
        'email_address': 'emailAddress',
        'creation_date': 'creationDate',
        'confirmed_date': 'confirmedDate',
        'expired_date': 'expiredDate'
    }

    def __init__(self, token=None, username=None, firstname=None, surname=None, email_address=None, creation_date=None, confirmed_date=None, expired_date=None, local_vars_configuration=None):  # noqa: E501
        """UserRegistrationRequestSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._username = None
        self._firstname = None
        self._surname = None
        self._email_address = None
        self._creation_date = None
        self._confirmed_date = None
        self._expired_date = None
        self.discriminator = None

        self.token = token
        self.username = username
        if firstname is not None:
            self.firstname = firstname
        if surname is not None:
            self.surname = surname
        self.email_address = email_address
        self.creation_date = creation_date
        if confirmed_date is not None:
            self.confirmed_date = confirmed_date
        if expired_date is not None:
            self.expired_date = expired_date

    @property
    def token(self):
        """Gets the token of this UserRegistrationRequestSummary.  # noqa: E501

        The token for this registration request  # noqa: E501

        :return: The token of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UserRegistrationRequestSummary.

        The token for this registration request  # noqa: E501

        :param token: The token of this UserRegistrationRequestSummary.  # noqa: E501
        :type token: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def username(self):
        """Gets the username of this UserRegistrationRequestSummary.  # noqa: E501

        The requested username  # noqa: E501

        :return: The username of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserRegistrationRequestSummary.

        The requested username  # noqa: E501

        :param username: The username of this UserRegistrationRequestSummary.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def firstname(self):
        """Gets the firstname of this UserRegistrationRequestSummary.  # noqa: E501

        The requested first name  # noqa: E501

        :return: The firstname of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserRegistrationRequestSummary.

        The requested first name  # noqa: E501

        :param firstname: The firstname of this UserRegistrationRequestSummary.  # noqa: E501
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def surname(self):
        """Gets the surname of this UserRegistrationRequestSummary.  # noqa: E501

        The requested surname  # noqa: E501

        :return: The surname of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this UserRegistrationRequestSummary.

        The requested surname  # noqa: E501

        :param surname: The surname of this UserRegistrationRequestSummary.  # noqa: E501
        :type surname: str
        """

        self._surname = surname

    @property
    def email_address(self):
        """Gets the email_address of this UserRegistrationRequestSummary.  # noqa: E501

        The requested email address  # noqa: E501

        :return: The email_address of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserRegistrationRequestSummary.

        The requested email address  # noqa: E501

        :param email_address: The email_address of this UserRegistrationRequestSummary.  # noqa: E501
        :type email_address: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def creation_date(self):
        """Gets the creation_date of this UserRegistrationRequestSummary.  # noqa: E501

        The date and time this request was created  # noqa: E501

        :return: The creation_date of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UserRegistrationRequestSummary.

        The date and time this request was created  # noqa: E501

        :param creation_date: The creation_date of this UserRegistrationRequestSummary.  # noqa: E501
        :type creation_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_date is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def confirmed_date(self):
        """Gets the confirmed_date of this UserRegistrationRequestSummary.  # noqa: E501

        The date and time this request was confirmed  # noqa: E501

        :return: The confirmed_date of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._confirmed_date

    @confirmed_date.setter
    def confirmed_date(self, confirmed_date):
        """Sets the confirmed_date of this UserRegistrationRequestSummary.

        The date and time this request was confirmed  # noqa: E501

        :param confirmed_date: The confirmed_date of this UserRegistrationRequestSummary.  # noqa: E501
        :type confirmed_date: datetime
        """

        self._confirmed_date = confirmed_date

    @property
    def expired_date(self):
        """Gets the expired_date of this UserRegistrationRequestSummary.  # noqa: E501

        The date and time this request expired  # noqa: E501

        :return: The expired_date of this UserRegistrationRequestSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._expired_date

    @expired_date.setter
    def expired_date(self, expired_date):
        """Sets the expired_date of this UserRegistrationRequestSummary.

        The date and time this request expired  # noqa: E501

        :param expired_date: The expired_date of this UserRegistrationRequestSummary.  # noqa: E501
        :type expired_date: datetime
        """

        self._expired_date = expired_date

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, UserRegistrationRequestSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRegistrationRequestSummary):
            return True

        return self.to_dict() != other.to_dict()
