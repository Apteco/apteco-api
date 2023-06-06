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


class ChannelSummary(object):
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
        'id': 'str',
        'schema_id': 'int',
        'description': 'str',
        'type': 'str',
        'parent_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'schema_id': 'schemaId',
        'description': 'description',
        'type': 'type',
        'parent_id': 'parentId'
    }

    def __init__(self, id=None, schema_id=None, description=None, type=None, parent_id=None, local_vars_configuration=None):  # noqa: E501
        """ChannelSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._schema_id = None
        self._description = None
        self._type = None
        self._parent_id = None
        self.discriminator = None

        self.id = id
        if schema_id is not None:
            self.schema_id = schema_id
        self.description = description
        self.type = type
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def id(self):
        """Gets the id of this ChannelSummary.  # noqa: E501

        The channel's id  # noqa: E501

        :return: The id of this ChannelSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChannelSummary.

        The channel's id  # noqa: E501

        :param id: The id of this ChannelSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def schema_id(self):
        """Gets the schema_id of this ChannelSummary.  # noqa: E501

        The channel's \"schema id\", used for looking up information about the channel in the run history of PeopleStage  # noqa: E501

        :return: The schema_id of this ChannelSummary.  # noqa: E501
        :rtype: int
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this ChannelSummary.

        The channel's \"schema id\", used for looking up information about the channel in the run history of PeopleStage  # noqa: E501

        :param schema_id: The schema_id of this ChannelSummary.  # noqa: E501
        :type: int
        """

        self._schema_id = schema_id

    @property
    def description(self):
        """Gets the description of this ChannelSummary.  # noqa: E501

        The channel's description  # noqa: E501

        :return: The description of this ChannelSummary.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChannelSummary.

        The channel's description  # noqa: E501

        :param description: The description of this ChannelSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this ChannelSummary.  # noqa: E501

        The channel's type  # noqa: E501

        :return: The type of this ChannelSummary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChannelSummary.

        The channel's type  # noqa: E501

        :param type: The type of this ChannelSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "Control", "Broadcast", "File", "Ftp", "Facebook", "MicrosoftDynamics", "SalesForce", "PushNotification", "Twitter", "Google", "LinkedIn", "Composite"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def parent_id(self):
        """Gets the parent_id of this ChannelSummary.  # noqa: E501

        The id of the channel's parent  # noqa: E501

        :return: The parent_id of this ChannelSummary.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ChannelSummary.

        The id of the channel's parent  # noqa: E501

        :param parent_id: The parent_id of this ChannelSummary.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

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
        if not isinstance(other, ChannelSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelSummary):
            return True

        return self.to_dict() != other.to_dict()
