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


class NumericVariableInfo(object):
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
        'minimum': 'float',
        'maximum': 'float',
        'is_currency': 'bool',
        'currency_locale': 'str',
        'currency_symbol': 'str'
    }

    attribute_map = {
        'minimum': 'minimum',
        'maximum': 'maximum',
        'is_currency': 'isCurrency',
        'currency_locale': 'currencyLocale',
        'currency_symbol': 'currencySymbol'
    }

    def __init__(self, minimum=None, maximum=None, is_currency=None, currency_locale=None, currency_symbol=None, local_vars_configuration=None):  # noqa: E501
        """NumericVariableInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._minimum = None
        self._maximum = None
        self._is_currency = None
        self._currency_locale = None
        self._currency_symbol = None
        self.discriminator = None

        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum
        if is_currency is not None:
            self.is_currency = is_currency
        if currency_locale is not None:
            self.currency_locale = currency_locale
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol

    @property
    def minimum(self):
        """Gets the minimum of this NumericVariableInfo.  # noqa: E501

        The minimum value that this numeric value has  # noqa: E501

        :return: The minimum of this NumericVariableInfo.  # noqa: E501
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this NumericVariableInfo.

        The minimum value that this numeric value has  # noqa: E501

        :param minimum: The minimum of this NumericVariableInfo.  # noqa: E501
        :type minimum: float
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this NumericVariableInfo.  # noqa: E501

        The maximum value that this numeric value has  # noqa: E501

        :return: The maximum of this NumericVariableInfo.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this NumericVariableInfo.

        The maximum value that this numeric value has  # noqa: E501

        :param maximum: The maximum of this NumericVariableInfo.  # noqa: E501
        :type maximum: float
        """

        self._maximum = maximum

    @property
    def is_currency(self):
        """Gets the is_currency of this NumericVariableInfo.  # noqa: E501

        Whether this variable represents a currency value  # noqa: E501

        :return: The is_currency of this NumericVariableInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_currency

    @is_currency.setter
    def is_currency(self, is_currency):
        """Sets the is_currency of this NumericVariableInfo.

        Whether this variable represents a currency value  # noqa: E501

        :param is_currency: The is_currency of this NumericVariableInfo.  # noqa: E501
        :type is_currency: bool
        """

        self._is_currency = is_currency

    @property
    def currency_locale(self):
        """Gets the currency_locale of this NumericVariableInfo.  # noqa: E501

        If this variable is a currency variable, then the locale name for the specific currency (i.e. \"en-GB\" for the UK pound sterling, \"en-US\" for the US dollar)  # noqa: E501

        :return: The currency_locale of this NumericVariableInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency_locale

    @currency_locale.setter
    def currency_locale(self, currency_locale):
        """Sets the currency_locale of this NumericVariableInfo.

        If this variable is a currency variable, then the locale name for the specific currency (i.e. \"en-GB\" for the UK pound sterling, \"en-US\" for the US dollar)  # noqa: E501

        :param currency_locale: The currency_locale of this NumericVariableInfo.  # noqa: E501
        :type currency_locale: str
        """

        self._currency_locale = currency_locale

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this NumericVariableInfo.  # noqa: E501

        If this variable is a currency variable, then the currency symbolfor the specific currency (i.e. \"£\" for the UK pound sterling, \"$\" for the US dollar)  # noqa: E501

        :return: The currency_symbol of this NumericVariableInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this NumericVariableInfo.

        If this variable is a currency variable, then the currency symbolfor the specific currency (i.e. \"£\" for the UK pound sterling, \"$\" for the US dollar)  # noqa: E501

        :param currency_symbol: The currency_symbol of this NumericVariableInfo.  # noqa: E501
        :type currency_symbol: str
        """

        self._currency_symbol = currency_symbol

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
        if not isinstance(other, NumericVariableInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NumericVariableInfo):
            return True

        return self.to_dict() != other.to_dict()
