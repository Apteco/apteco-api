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


class UpdateTelemetryStateDetails(object):
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
        'opt_state': 'str'
    }

    attribute_map = {
        'opt_state': 'optState'
    }

    def __init__(self, opt_state=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTelemetryStateDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opt_state = None
        self.discriminator = None

        self.opt_state = opt_state

    @property
    def opt_state(self):
        """Gets the opt_state of this UpdateTelemetryStateDetails.  # noqa: E501

        The optState for this telemetry state  # noqa: E501

        :return: The opt_state of this UpdateTelemetryStateDetails.  # noqa: E501
        :rtype: str
        """
        return self._opt_state

    @opt_state.setter
    def opt_state(self, opt_state):
        """Sets the opt_state of this UpdateTelemetryStateDetails.

        The optState for this telemetry state  # noqa: E501

        :param opt_state: The opt_state of this UpdateTelemetryStateDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and opt_state is None:  # noqa: E501
            raise ValueError("Invalid value for `opt_state`, must not be `None`")  # noqa: E501
        allowed_values = ["NotOpted", "OptedOut", "OptedIn", "ForcedOut", "ForcedIn"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and opt_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `opt_state` ({0}), must be one of {1}"  # noqa: E501
                .format(opt_state, allowed_values)
            )

        self._opt_state = opt_state

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
        if not isinstance(other, UpdateTelemetryStateDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTelemetryStateDetails):
            return True

        return self.to_dict() != other.to_dict()
