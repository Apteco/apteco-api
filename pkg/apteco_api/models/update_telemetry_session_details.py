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


class UpdateTelemetrySessionDetails(object):
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
        'session_end': 'datetime'
    }

    attribute_map = {
        'session_end': 'sessionEnd'
    }

    def __init__(self, session_end=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTelemetrySessionDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._session_end = None
        self.discriminator = None

        if session_end is not None:
            self.session_end = session_end

    @property
    def session_end(self):
        """Gets the session_end of this UpdateTelemetrySessionDetails.  # noqa: E501

        The end time for this telemetry session  # noqa: E501

        :return: The session_end of this UpdateTelemetrySessionDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._session_end

    @session_end.setter
    def session_end(self, session_end):
        """Sets the session_end of this UpdateTelemetrySessionDetails.

        The end time for this telemetry session  # noqa: E501

        :param session_end: The session_end of this UpdateTelemetrySessionDetails.  # noqa: E501
        :type session_end: datetime
        """

        self._session_end = session_end

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
        if not isinstance(other, UpdateTelemetrySessionDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTelemetrySessionDetails):
            return True

        return self.to_dict() != other.to_dict()
