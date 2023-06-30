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


class CollectionHitSummary(object):
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
        'collection_id': 'int',
        'timestamp': 'datetime',
        'user': 'UserDisplayDetails'
    }

    attribute_map = {
        'id': 'id',
        'collection_id': 'collectionId',
        'timestamp': 'timestamp',
        'user': 'user'
    }

    def __init__(self, id=None, collection_id=None, timestamp=None, user=None, local_vars_configuration=None):  # noqa: E501
        """CollectionHitSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._collection_id = None
        self._timestamp = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.collection_id = collection_id
        self.timestamp = timestamp
        self.user = user

    @property
    def id(self):
        """Gets the id of this CollectionHitSummary.  # noqa: E501

        The id of the hit itself  # noqa: E501

        :return: The id of this CollectionHitSummary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectionHitSummary.

        The id of the hit itself  # noqa: E501

        :param id: The id of this CollectionHitSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def collection_id(self):
        """Gets the collection_id of this CollectionHitSummary.  # noqa: E501

        The id of the collection viewed  # noqa: E501

        :return: The collection_id of this CollectionHitSummary.  # noqa: E501
        :rtype: int
        """
        return self._collection_id

    @collection_id.setter
    def collection_id(self, collection_id):
        """Sets the collection_id of this CollectionHitSummary.

        The id of the collection viewed  # noqa: E501

        :param collection_id: The collection_id of this CollectionHitSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and collection_id is None:  # noqa: E501
            raise ValueError("Invalid value for `collection_id`, must not be `None`")  # noqa: E501

        self._collection_id = collection_id

    @property
    def timestamp(self):
        """Gets the timestamp of this CollectionHitSummary.  # noqa: E501

        The timestamp of when the hit was recorded  # noqa: E501

        :return: The timestamp of this CollectionHitSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CollectionHitSummary.

        The timestamp of when the hit was recorded  # noqa: E501

        :param timestamp: The timestamp of this CollectionHitSummary.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def user(self):
        """Gets the user of this CollectionHitSummary.  # noqa: E501


        :return: The user of this CollectionHitSummary.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CollectionHitSummary.


        :param user: The user of this CollectionHitSummary.  # noqa: E501
        :type: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, CollectionHitSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionHitSummary):
            return True

        return self.to_dict() != other.to_dict()
