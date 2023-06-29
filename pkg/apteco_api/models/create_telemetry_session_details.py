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


class CreateTelemetrySessionDetails(object):
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
        'client_type': 'str',
        'client_version': 'str',
        'user_agent_details': 'str'
    }

    attribute_map = {
        'client_type': 'clientType',
        'client_version': 'clientVersion',
        'user_agent_details': 'userAgentDetails'
    }

    def __init__(self, client_type=None, client_version=None, user_agent_details=None, local_vars_configuration=None):  # noqa: E501
        """CreateTelemetrySessionDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._client_type = None
        self._client_version = None
        self._user_agent_details = None
        self.discriminator = None

        self.client_type = client_type
        if client_version is not None:
            self.client_version = client_version
        if user_agent_details is not None:
            self.user_agent_details = user_agent_details

    @property
    def client_type(self):
        """Gets the client_type of this CreateTelemetrySessionDetails.  # noqa: E501

        The client type for this telemetry session  # noqa: E501

        :return: The client_type of this CreateTelemetrySessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this CreateTelemetrySessionDetails.

        The client type for this telemetry session  # noqa: E501

        :param client_type: The client_type of this CreateTelemetrySessionDetails.  # noqa: E501
        :type client_type: str
        """
        if self.local_vars_configuration.client_side_validation and client_type is None:  # noqa: E501
            raise ValueError("Invalid value for `client_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Orbit"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and client_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `client_type` ({0}), must be one of {1}"  # noqa: E501
                .format(client_type, allowed_values)
            )

        self._client_type = client_type

    @property
    def client_version(self):
        """Gets the client_version of this CreateTelemetrySessionDetails.  # noqa: E501

        The client version for this telemetry session  # noqa: E501

        :return: The client_version of this CreateTelemetrySessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this CreateTelemetrySessionDetails.

        The client version for this telemetry session  # noqa: E501

        :param client_version: The client_version of this CreateTelemetrySessionDetails.  # noqa: E501
        :type client_version: str
        """

        self._client_version = client_version

    @property
    def user_agent_details(self):
        """Gets the user_agent_details of this CreateTelemetrySessionDetails.  # noqa: E501

        The user agent details for this telemetry session  # noqa: E501

        :return: The user_agent_details of this CreateTelemetrySessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_agent_details

    @user_agent_details.setter
    def user_agent_details(self, user_agent_details):
        """Sets the user_agent_details of this CreateTelemetrySessionDetails.

        The user agent details for this telemetry session  # noqa: E501

        :param user_agent_details: The user_agent_details of this CreateTelemetrySessionDetails.  # noqa: E501
        :type user_agent_details: str
        """

        self._user_agent_details = user_agent_details

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
        if not isinstance(other, CreateTelemetrySessionDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTelemetrySessionDetails):
            return True

        return self.to_dict() != other.to_dict()
