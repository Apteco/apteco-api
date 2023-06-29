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


class ElementStatus(object):
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
        'description': 'str',
        'type': 'str',
        'successful_campaigns_count': 'int',
        'errored_campaigns_count': 'int',
        'inactive_campaigns_count': 'int',
        'needs_approval_campaigns_count': 'int',
        'channel_types': 'list[str]',
        'first_ran': 'datetime',
        'last_ran': 'datetime',
        'statistics_timestamp': 'datetime',
        'path': 'list[ElementKey]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'type': 'type',
        'successful_campaigns_count': 'successfulCampaignsCount',
        'errored_campaigns_count': 'erroredCampaignsCount',
        'inactive_campaigns_count': 'inactiveCampaignsCount',
        'needs_approval_campaigns_count': 'needsApprovalCampaignsCount',
        'channel_types': 'channelTypes',
        'first_ran': 'firstRan',
        'last_ran': 'lastRan',
        'statistics_timestamp': 'statisticsTimestamp',
        'path': 'path'
    }

    def __init__(self, id=None, description=None, type=None, successful_campaigns_count=None, errored_campaigns_count=None, inactive_campaigns_count=None, needs_approval_campaigns_count=None, channel_types=None, first_ran=None, last_ran=None, statistics_timestamp=None, path=None, local_vars_configuration=None):  # noqa: E501
        """ElementStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._description = None
        self._type = None
        self._successful_campaigns_count = None
        self._errored_campaigns_count = None
        self._inactive_campaigns_count = None
        self._needs_approval_campaigns_count = None
        self._channel_types = None
        self._first_ran = None
        self._last_ran = None
        self._statistics_timestamp = None
        self._path = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.type = type
        if successful_campaigns_count is not None:
            self.successful_campaigns_count = successful_campaigns_count
        if errored_campaigns_count is not None:
            self.errored_campaigns_count = errored_campaigns_count
        if inactive_campaigns_count is not None:
            self.inactive_campaigns_count = inactive_campaigns_count
        if needs_approval_campaigns_count is not None:
            self.needs_approval_campaigns_count = needs_approval_campaigns_count
        if channel_types is not None:
            self.channel_types = channel_types
        if first_ran is not None:
            self.first_ran = first_ran
        if last_ran is not None:
            self.last_ran = last_ran
        if statistics_timestamp is not None:
            self.statistics_timestamp = statistics_timestamp
        if path is not None:
            self.path = path

    @property
    def id(self):
        """Gets the id of this ElementStatus.  # noqa: E501

        The element's id  # noqa: E501

        :return: The id of this ElementStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElementStatus.

        The element's id  # noqa: E501

        :param id: The id of this ElementStatus.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this ElementStatus.  # noqa: E501

        The element's description  # noqa: E501

        :return: The description of this ElementStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ElementStatus.

        The element's description  # noqa: E501

        :param description: The description of this ElementStatus.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this ElementStatus.  # noqa: E501

        The element's type  # noqa: E501

        :return: The type of this ElementStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElementStatus.

        The element's type  # noqa: E501

        :param type: The type of this ElementStatus.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "Diagram", "Programme", "Area", "Campaign", "Message", "Group", "Audience", "Content", "Delivery", "Pool", "Responses", "Transition", "PauseAction"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def successful_campaigns_count(self):
        """Gets the successful_campaigns_count of this ElementStatus.  # noqa: E501

        The number of campaigns that currently have a success status within this element  # noqa: E501

        :return: The successful_campaigns_count of this ElementStatus.  # noqa: E501
        :rtype: int
        """
        return self._successful_campaigns_count

    @successful_campaigns_count.setter
    def successful_campaigns_count(self, successful_campaigns_count):
        """Sets the successful_campaigns_count of this ElementStatus.

        The number of campaigns that currently have a success status within this element  # noqa: E501

        :param successful_campaigns_count: The successful_campaigns_count of this ElementStatus.  # noqa: E501
        :type successful_campaigns_count: int
        """

        self._successful_campaigns_count = successful_campaigns_count

    @property
    def errored_campaigns_count(self):
        """Gets the errored_campaigns_count of this ElementStatus.  # noqa: E501

        The number of campaigns that currently have an errored status within this element  # noqa: E501

        :return: The errored_campaigns_count of this ElementStatus.  # noqa: E501
        :rtype: int
        """
        return self._errored_campaigns_count

    @errored_campaigns_count.setter
    def errored_campaigns_count(self, errored_campaigns_count):
        """Sets the errored_campaigns_count of this ElementStatus.

        The number of campaigns that currently have an errored status within this element  # noqa: E501

        :param errored_campaigns_count: The errored_campaigns_count of this ElementStatus.  # noqa: E501
        :type errored_campaigns_count: int
        """

        self._errored_campaigns_count = errored_campaigns_count

    @property
    def inactive_campaigns_count(self):
        """Gets the inactive_campaigns_count of this ElementStatus.  # noqa: E501

        The number of campaigns that currently have an inactive status within this element  # noqa: E501

        :return: The inactive_campaigns_count of this ElementStatus.  # noqa: E501
        :rtype: int
        """
        return self._inactive_campaigns_count

    @inactive_campaigns_count.setter
    def inactive_campaigns_count(self, inactive_campaigns_count):
        """Sets the inactive_campaigns_count of this ElementStatus.

        The number of campaigns that currently have an inactive status within this element  # noqa: E501

        :param inactive_campaigns_count: The inactive_campaigns_count of this ElementStatus.  # noqa: E501
        :type inactive_campaigns_count: int
        """

        self._inactive_campaigns_count = inactive_campaigns_count

    @property
    def needs_approval_campaigns_count(self):
        """Gets the needs_approval_campaigns_count of this ElementStatus.  # noqa: E501

        The number of campaigns that currently have a message that needs approval within this element  # noqa: E501

        :return: The needs_approval_campaigns_count of this ElementStatus.  # noqa: E501
        :rtype: int
        """
        return self._needs_approval_campaigns_count

    @needs_approval_campaigns_count.setter
    def needs_approval_campaigns_count(self, needs_approval_campaigns_count):
        """Sets the needs_approval_campaigns_count of this ElementStatus.

        The number of campaigns that currently have a message that needs approval within this element  # noqa: E501

        :param needs_approval_campaigns_count: The needs_approval_campaigns_count of this ElementStatus.  # noqa: E501
        :type needs_approval_campaigns_count: int
        """

        self._needs_approval_campaigns_count = needs_approval_campaigns_count

    @property
    def channel_types(self):
        """Gets the channel_types of this ElementStatus.  # noqa: E501

        The different types of channel that have been used by deliveries within this element  # noqa: E501

        :return: The channel_types of this ElementStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._channel_types

    @channel_types.setter
    def channel_types(self, channel_types):
        """Sets the channel_types of this ElementStatus.

        The different types of channel that have been used by deliveries within this element  # noqa: E501

        :param channel_types: The channel_types of this ElementStatus.  # noqa: E501
        :type channel_types: list[str]
        """
        allowed_values = ["Unknown", "Control", "Broadcast", "File", "Ftp", "Facebook", "MicrosoftDynamics", "SalesForce", "PushNotification", "Twitter", "Google", "LinkedIn", "Composite"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(channel_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `channel_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(channel_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._channel_types = channel_types

    @property
    def first_ran(self):
        """Gets the first_ran of this ElementStatus.  # noqa: E501

        The first time that any deliveries ran within this element  # noqa: E501

        :return: The first_ran of this ElementStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._first_ran

    @first_ran.setter
    def first_ran(self, first_ran):
        """Sets the first_ran of this ElementStatus.

        The first time that any deliveries ran within this element  # noqa: E501

        :param first_ran: The first_ran of this ElementStatus.  # noqa: E501
        :type first_ran: datetime
        """

        self._first_ran = first_ran

    @property
    def last_ran(self):
        """Gets the last_ran of this ElementStatus.  # noqa: E501

        The last time that any deliveries ran within this element  # noqa: E501

        :return: The last_ran of this ElementStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_ran

    @last_ran.setter
    def last_ran(self, last_ran):
        """Sets the last_ran of this ElementStatus.

        The last time that any deliveries ran within this element  # noqa: E501

        :param last_ran: The last_ran of this ElementStatus.  # noqa: E501
        :type last_ran: datetime
        """

        self._last_ran = last_ran

    @property
    def statistics_timestamp(self):
        """Gets the statistics_timestamp of this ElementStatus.  # noqa: E501

        The date and time that the statistics were calculated  # noqa: E501

        :return: The statistics_timestamp of this ElementStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._statistics_timestamp

    @statistics_timestamp.setter
    def statistics_timestamp(self, statistics_timestamp):
        """Sets the statistics_timestamp of this ElementStatus.

        The date and time that the statistics were calculated  # noqa: E501

        :param statistics_timestamp: The statistics_timestamp of this ElementStatus.  # noqa: E501
        :type statistics_timestamp: datetime
        """

        self._statistics_timestamp = statistics_timestamp

    @property
    def path(self):
        """Gets the path of this ElementStatus.  # noqa: E501

        The element's path  # noqa: E501

        :return: The path of this ElementStatus.  # noqa: E501
        :rtype: list[ElementKey]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ElementStatus.

        The element's path  # noqa: E501

        :param path: The path of this ElementStatus.  # noqa: E501
        :type path: list[ElementKey]
        """

        self._path = path

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
        if not isinstance(other, ElementStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElementStatus):
            return True

        return self.to_dict() != other.to_dict()
