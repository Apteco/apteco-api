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


class Limits(object):
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
        'sampling': 'str',
        'stop_at_limit': 'bool',
        'total': 'int',
        'type': 'str',
        'start_at': 'int',
        'percent': 'float',
        'fraction': 'Fraction'
    }

    attribute_map = {
        'sampling': 'sampling',
        'stop_at_limit': 'stopAtLimit',
        'total': 'total',
        'type': 'type',
        'start_at': 'startAt',
        'percent': 'percent',
        'fraction': 'fraction'
    }

    def __init__(self, sampling=None, stop_at_limit=None, total=None, type=None, start_at=None, percent=None, fraction=None, local_vars_configuration=None):  # noqa: E501
        """Limits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._sampling = None
        self._stop_at_limit = None
        self._total = None
        self._type = None
        self._start_at = None
        self._percent = None
        self._fraction = None
        self.discriminator = None

        if sampling is not None:
            self.sampling = sampling
        if stop_at_limit is not None:
            self.stop_at_limit = stop_at_limit
        if total is not None:
            self.total = total
        if type is not None:
            self.type = type
        if start_at is not None:
            self.start_at = start_at
        if percent is not None:
            self.percent = percent
        if fraction is not None:
            self.fraction = fraction

    @property
    def sampling(self):
        """Gets the sampling of this Limits.  # noqa: E501


        :return: The sampling of this Limits.  # noqa: E501
        :rtype: str
        """
        return self._sampling

    @sampling.setter
    def sampling(self, sampling):
        """Sets the sampling of this Limits.


        :param sampling: The sampling of this Limits.  # noqa: E501
        :type sampling: str
        """
        allowed_values = ["All", "First", "Stratified", "Random"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sampling not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sampling` ({0}), must be one of {1}"  # noqa: E501
                .format(sampling, allowed_values)
            )

        self._sampling = sampling

    @property
    def stop_at_limit(self):
        """Gets the stop_at_limit of this Limits.  # noqa: E501


        :return: The stop_at_limit of this Limits.  # noqa: E501
        :rtype: bool
        """
        return self._stop_at_limit

    @stop_at_limit.setter
    def stop_at_limit(self, stop_at_limit):
        """Sets the stop_at_limit of this Limits.


        :param stop_at_limit: The stop_at_limit of this Limits.  # noqa: E501
        :type stop_at_limit: bool
        """

        self._stop_at_limit = stop_at_limit

    @property
    def total(self):
        """Gets the total of this Limits.  # noqa: E501


        :return: The total of this Limits.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Limits.


        :param total: The total of this Limits.  # noqa: E501
        :type total: int
        """

        self._total = total

    @property
    def type(self):
        """Gets the type of this Limits.  # noqa: E501


        :return: The type of this Limits.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Limits.


        :param type: The type of this Limits.  # noqa: E501
        :type type: str
        """
        allowed_values = ["None", "Total", "Fraction", "Percent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def start_at(self):
        """Gets the start_at of this Limits.  # noqa: E501


        :return: The start_at of this Limits.  # noqa: E501
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this Limits.


        :param start_at: The start_at of this Limits.  # noqa: E501
        :type start_at: int
        """

        self._start_at = start_at

    @property
    def percent(self):
        """Gets the percent of this Limits.  # noqa: E501


        :return: The percent of this Limits.  # noqa: E501
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this Limits.


        :param percent: The percent of this Limits.  # noqa: E501
        :type percent: float
        """

        self._percent = percent

    @property
    def fraction(self):
        """Gets the fraction of this Limits.  # noqa: E501


        :return: The fraction of this Limits.  # noqa: E501
        :rtype: Fraction
        """
        return self._fraction

    @fraction.setter
    def fraction(self, fraction):
        """Sets the fraction of this Limits.


        :param fraction: The fraction of this Limits.  # noqa: E501
        :type fraction: Fraction
        """

        self._fraction = fraction

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
        if not isinstance(other, Limits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Limits):
            return True

        return self.to_dict() != other.to_dict()
