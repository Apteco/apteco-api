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


class RangeStatistics(object):
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
        'communications_count': 'int',
        'deliveries_count': 'int',
        'messages_count': 'int',
        'campaigns_count': 'int',
        'first_ran': 'datetime',
        'last_ran': 'datetime',
        'statistics_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'communications_count': 'communicationsCount',
        'deliveries_count': 'deliveriesCount',
        'messages_count': 'messagesCount',
        'campaigns_count': 'campaignsCount',
        'first_ran': 'firstRan',
        'last_ran': 'lastRan',
        'statistics_timestamp': 'statisticsTimestamp'
    }

    def __init__(self, id=None, communications_count=None, deliveries_count=None, messages_count=None, campaigns_count=None, first_ran=None, last_ran=None, statistics_timestamp=None, local_vars_configuration=None):  # noqa: E501
        """RangeStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._communications_count = None
        self._deliveries_count = None
        self._messages_count = None
        self._campaigns_count = None
        self._first_ran = None
        self._last_ran = None
        self._statistics_timestamp = None
        self.discriminator = None

        self.id = id
        if communications_count is not None:
            self.communications_count = communications_count
        if deliveries_count is not None:
            self.deliveries_count = deliveries_count
        if messages_count is not None:
            self.messages_count = messages_count
        if campaigns_count is not None:
            self.campaigns_count = campaigns_count
        if first_ran is not None:
            self.first_ran = first_ran
        if last_ran is not None:
            self.last_ran = last_ran
        if statistics_timestamp is not None:
            self.statistics_timestamp = statistics_timestamp

    @property
    def id(self):
        """Gets the id of this RangeStatistics.  # noqa: E501

        The element's id  # noqa: E501

        :return: The id of this RangeStatistics.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RangeStatistics.

        The element's id  # noqa: E501

        :param id: The id of this RangeStatistics.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def communications_count(self):
        """Gets the communications_count of this RangeStatistics.  # noqa: E501

        The number of communications sent within this element during the specified date range  # noqa: E501

        :return: The communications_count of this RangeStatistics.  # noqa: E501
        :rtype: int
        """
        return self._communications_count

    @communications_count.setter
    def communications_count(self, communications_count):
        """Sets the communications_count of this RangeStatistics.

        The number of communications sent within this element during the specified date range  # noqa: E501

        :param communications_count: The communications_count of this RangeStatistics.  # noqa: E501
        :type communications_count: int
        """

        self._communications_count = communications_count

    @property
    def deliveries_count(self):
        """Gets the deliveries_count of this RangeStatistics.  # noqa: E501

        The number of deliveries that have run within this element during the specified date range  # noqa: E501

        :return: The deliveries_count of this RangeStatistics.  # noqa: E501
        :rtype: int
        """
        return self._deliveries_count

    @deliveries_count.setter
    def deliveries_count(self, deliveries_count):
        """Sets the deliveries_count of this RangeStatistics.

        The number of deliveries that have run within this element during the specified date range  # noqa: E501

        :param deliveries_count: The deliveries_count of this RangeStatistics.  # noqa: E501
        :type deliveries_count: int
        """

        self._deliveries_count = deliveries_count

    @property
    def messages_count(self):
        """Gets the messages_count of this RangeStatistics.  # noqa: E501

        The number of messages that have had at least one delivery run within this element during the specified date range  # noqa: E501

        :return: The messages_count of this RangeStatistics.  # noqa: E501
        :rtype: int
        """
        return self._messages_count

    @messages_count.setter
    def messages_count(self, messages_count):
        """Sets the messages_count of this RangeStatistics.

        The number of messages that have had at least one delivery run within this element during the specified date range  # noqa: E501

        :param messages_count: The messages_count of this RangeStatistics.  # noqa: E501
        :type messages_count: int
        """

        self._messages_count = messages_count

    @property
    def campaigns_count(self):
        """Gets the campaigns_count of this RangeStatistics.  # noqa: E501

        The number of campaigns that have had at least one delivery run within this element during the specified date range  # noqa: E501

        :return: The campaigns_count of this RangeStatistics.  # noqa: E501
        :rtype: int
        """
        return self._campaigns_count

    @campaigns_count.setter
    def campaigns_count(self, campaigns_count):
        """Sets the campaigns_count of this RangeStatistics.

        The number of campaigns that have had at least one delivery run within this element during the specified date range  # noqa: E501

        :param campaigns_count: The campaigns_count of this RangeStatistics.  # noqa: E501
        :type campaigns_count: int
        """

        self._campaigns_count = campaigns_count

    @property
    def first_ran(self):
        """Gets the first_ran of this RangeStatistics.  # noqa: E501

        The first time that any deliveries ran within this element during the specified date range  # noqa: E501

        :return: The first_ran of this RangeStatistics.  # noqa: E501
        :rtype: datetime
        """
        return self._first_ran

    @first_ran.setter
    def first_ran(self, first_ran):
        """Sets the first_ran of this RangeStatistics.

        The first time that any deliveries ran within this element during the specified date range  # noqa: E501

        :param first_ran: The first_ran of this RangeStatistics.  # noqa: E501
        :type first_ran: datetime
        """

        self._first_ran = first_ran

    @property
    def last_ran(self):
        """Gets the last_ran of this RangeStatistics.  # noqa: E501

        The last time that any deliveries ran within this element during the specified date range  # noqa: E501

        :return: The last_ran of this RangeStatistics.  # noqa: E501
        :rtype: datetime
        """
        return self._last_ran

    @last_ran.setter
    def last_ran(self, last_ran):
        """Sets the last_ran of this RangeStatistics.

        The last time that any deliveries ran within this element during the specified date range  # noqa: E501

        :param last_ran: The last_ran of this RangeStatistics.  # noqa: E501
        :type last_ran: datetime
        """

        self._last_ran = last_ran

    @property
    def statistics_timestamp(self):
        """Gets the statistics_timestamp of this RangeStatistics.  # noqa: E501

        The date and time that the campaign statistics were calculated  # noqa: E501

        :return: The statistics_timestamp of this RangeStatistics.  # noqa: E501
        :rtype: datetime
        """
        return self._statistics_timestamp

    @statistics_timestamp.setter
    def statistics_timestamp(self, statistics_timestamp):
        """Sets the statistics_timestamp of this RangeStatistics.

        The date and time that the campaign statistics were calculated  # noqa: E501

        :param statistics_timestamp: The statistics_timestamp of this RangeStatistics.  # noqa: E501
        :type statistics_timestamp: datetime
        """

        self._statistics_timestamp = statistics_timestamp

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
        if not isinstance(other, RangeStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RangeStatistics):
            return True

        return self.to_dict() != other.to_dict()
