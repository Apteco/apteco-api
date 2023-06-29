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


class ResetPasswordRequestDetail(object):
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
        'reset_password_url': 'str',
        'has_notification_been_sent': 'bool',
        'token': 'str',
        'username': 'str',
        'email_address': 'str',
        'creation_date': 'datetime',
        'confirmed_date': 'datetime',
        'expired_date': 'datetime'
    }

    attribute_map = {
        'reset_password_url': 'resetPasswordUrl',
        'has_notification_been_sent': 'hasNotificationBeenSent',
        'token': 'token',
        'username': 'username',
        'email_address': 'emailAddress',
        'creation_date': 'creationDate',
        'confirmed_date': 'confirmedDate',
        'expired_date': 'expiredDate'
    }

    def __init__(self, reset_password_url=None, has_notification_been_sent=None, token=None, username=None, email_address=None, creation_date=None, confirmed_date=None, expired_date=None, local_vars_configuration=None):  # noqa: E501
        """ResetPasswordRequestDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._reset_password_url = None
        self._has_notification_been_sent = None
        self._token = None
        self._username = None
        self._email_address = None
        self._creation_date = None
        self._confirmed_date = None
        self._expired_date = None
        self.discriminator = None

        if reset_password_url is not None:
            self.reset_password_url = reset_password_url
        self.has_notification_been_sent = has_notification_been_sent
        self.token = token
        self.username = username
        self.email_address = email_address
        self.creation_date = creation_date
        if confirmed_date is not None:
            self.confirmed_date = confirmed_date
        if expired_date is not None:
            self.expired_date = expired_date

    @property
    def reset_password_url(self):
        """Gets the reset_password_url of this ResetPasswordRequestDetail.  # noqa: E501

        The URL sent in the notification to the user to allow them to confirm they want to reset their password.  # noqa: E501

        :return: The reset_password_url of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: str
        """
        return self._reset_password_url

    @reset_password_url.setter
    def reset_password_url(self, reset_password_url):
        """Sets the reset_password_url of this ResetPasswordRequestDetail.

        The URL sent in the notification to the user to allow them to confirm they want to reset their password.  # noqa: E501

        :param reset_password_url: The reset_password_url of this ResetPasswordRequestDetail.  # noqa: E501
        :type reset_password_url: str
        """

        self._reset_password_url = reset_password_url

    @property
    def has_notification_been_sent(self):
        """Gets the has_notification_been_sent of this ResetPasswordRequestDetail.  # noqa: E501

        Whether the notification has been sent to the user or not.  # noqa: E501

        :return: The has_notification_been_sent of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: bool
        """
        return self._has_notification_been_sent

    @has_notification_been_sent.setter
    def has_notification_been_sent(self, has_notification_been_sent):
        """Sets the has_notification_been_sent of this ResetPasswordRequestDetail.

        Whether the notification has been sent to the user or not.  # noqa: E501

        :param has_notification_been_sent: The has_notification_been_sent of this ResetPasswordRequestDetail.  # noqa: E501
        :type has_notification_been_sent: bool
        """
        if self.local_vars_configuration.client_side_validation and has_notification_been_sent is None:  # noqa: E501
            raise ValueError("Invalid value for `has_notification_been_sent`, must not be `None`")  # noqa: E501

        self._has_notification_been_sent = has_notification_been_sent

    @property
    def token(self):
        """Gets the token of this ResetPasswordRequestDetail.  # noqa: E501

        The token for this reset password request  # noqa: E501

        :return: The token of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ResetPasswordRequestDetail.

        The token for this reset password request  # noqa: E501

        :param token: The token of this ResetPasswordRequestDetail.  # noqa: E501
        :type token: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def username(self):
        """Gets the username of this ResetPasswordRequestDetail.  # noqa: E501

        The username of the user requesting the reset password  # noqa: E501

        :return: The username of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ResetPasswordRequestDetail.

        The username of the user requesting the reset password  # noqa: E501

        :param username: The username of this ResetPasswordRequestDetail.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email_address(self):
        """Gets the email_address of this ResetPasswordRequestDetail.  # noqa: E501

        The email address of the user requesting the reset password  # noqa: E501

        :return: The email_address of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ResetPasswordRequestDetail.

        The email address of the user requesting the reset password  # noqa: E501

        :param email_address: The email_address of this ResetPasswordRequestDetail.  # noqa: E501
        :type email_address: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def creation_date(self):
        """Gets the creation_date of this ResetPasswordRequestDetail.  # noqa: E501

        The date and time this request was created  # noqa: E501

        :return: The creation_date of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ResetPasswordRequestDetail.

        The date and time this request was created  # noqa: E501

        :param creation_date: The creation_date of this ResetPasswordRequestDetail.  # noqa: E501
        :type creation_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_date is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def confirmed_date(self):
        """Gets the confirmed_date of this ResetPasswordRequestDetail.  # noqa: E501

        The date and time this request was confirmed  # noqa: E501

        :return: The confirmed_date of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._confirmed_date

    @confirmed_date.setter
    def confirmed_date(self, confirmed_date):
        """Sets the confirmed_date of this ResetPasswordRequestDetail.

        The date and time this request was confirmed  # noqa: E501

        :param confirmed_date: The confirmed_date of this ResetPasswordRequestDetail.  # noqa: E501
        :type confirmed_date: datetime
        """

        self._confirmed_date = confirmed_date

    @property
    def expired_date(self):
        """Gets the expired_date of this ResetPasswordRequestDetail.  # noqa: E501

        The date and time this request expired  # noqa: E501

        :return: The expired_date of this ResetPasswordRequestDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._expired_date

    @expired_date.setter
    def expired_date(self, expired_date):
        """Sets the expired_date of this ResetPasswordRequestDetail.

        The date and time this request expired  # noqa: E501

        :param expired_date: The expired_date of this ResetPasswordRequestDetail.  # noqa: E501
        :type expired_date: datetime
        """

        self._expired_date = expired_date

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
        if not isinstance(other, ResetPasswordRequestDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetPasswordRequestDetail):
            return True

        return self.to_dict() != other.to_dict()
