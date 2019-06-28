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


class SessionAndUserDetails(object):
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
        'user': 'UserDisplayDetails',
        'session_id': 'str'
    }

    attribute_map = {
        'user': 'user',
        'session_id': 'sessionId'
    }

    def __init__(self, user=None, session_id=None):  # noqa: E501
        """SessionAndUserDetails - a model defined in OpenAPI"""  # noqa: E501

        self._user = None
        self._session_id = None
        self.discriminator = None

        self.user = user
        self.session_id = session_id

    @property
    def user(self):
        """Gets the user of this SessionAndUserDetails.  # noqa: E501


        :return: The user of this SessionAndUserDetails.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SessionAndUserDetails.


        :param user: The user of this SessionAndUserDetails.  # noqa: E501
        :type: UserDisplayDetails
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def session_id(self):
        """Gets the session_id of this SessionAndUserDetails.  # noqa: E501

        The id for this session  # noqa: E501

        :return: The session_id of this SessionAndUserDetails.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this SessionAndUserDetails.

        The id for this session  # noqa: E501

        :param session_id: The session_id of this SessionAndUserDetails.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

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
        if not isinstance(other, SessionAndUserDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
