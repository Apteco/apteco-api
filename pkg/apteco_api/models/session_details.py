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


class SessionDetails(object):
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
        'access_token': 'str',
        'user': 'UserDisplayDetails',
        'session_id': 'str',
        'last_login': 'datetime',
        'licence': 'Licence'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'user': 'user',
        'session_id': 'sessionId',
        'last_login': 'lastLogin',
        'licence': 'licence'
    }

    def __init__(self, access_token=None, user=None, session_id=None, last_login=None, licence=None, local_vars_configuration=None):  # noqa: E501
        """SessionDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._user = None
        self._session_id = None
        self._last_login = None
        self._licence = None
        self.discriminator = None

        self.access_token = access_token
        self.user = user
        self.session_id = session_id
        if last_login is not None:
            self.last_login = last_login
        self.licence = licence

    @property
    def access_token(self):
        """Gets the access_token of this SessionDetails.  # noqa: E501

        The access token that needs to be included when making requests that require authentication  # noqa: E501

        :return: The access_token of this SessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this SessionDetails.

        The access token that needs to be included when making requests that require authentication  # noqa: E501

        :param access_token: The access_token of this SessionDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def user(self):
        """Gets the user of this SessionDetails.  # noqa: E501


        :return: The user of this SessionDetails.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SessionDetails.


        :param user: The user of this SessionDetails.  # noqa: E501
        :type: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def session_id(self):
        """Gets the session_id of this SessionDetails.  # noqa: E501

        The id for this current session  # noqa: E501

        :return: The session_id of this SessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this SessionDetails.

        The id for this current session  # noqa: E501

        :param session_id: The session_id of this SessionDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and session_id is None:  # noqa: E501
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def last_login(self):
        """Gets the last_login of this SessionDetails.  # noqa: E501

        The last login for the user  # noqa: E501

        :return: The last_login of this SessionDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this SessionDetails.

        The last login for the user  # noqa: E501

        :param last_login: The last_login of this SessionDetails.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

    @property
    def licence(self):
        """Gets the licence of this SessionDetails.  # noqa: E501


        :return: The licence of this SessionDetails.  # noqa: E501
        :rtype: Licence
        """
        return self._licence

    @licence.setter
    def licence(self, licence):
        """Sets the licence of this SessionDetails.


        :param licence: The licence of this SessionDetails.  # noqa: E501
        :type: Licence
        """
        if self.local_vars_configuration.client_side_validation and licence is None:  # noqa: E501
            raise ValueError("Invalid value for `licence`, must not be `None`")  # noqa: E501

        self._licence = licence

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
        if not isinstance(other, SessionDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionDetails):
            return True

        return self.to_dict() != other.to_dict()