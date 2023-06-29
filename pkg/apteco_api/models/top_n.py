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


class TopN(object):
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
        'variable_name': 'str',
        'order_expression': 'Expression',
        'expression': 'str',
        'direction': 'str',
        'value': 'int',
        'percent': 'float',
        'min_value': 'float',
        'max_value': 'float',
        'sequence': 'str',
        'grouping_variable_name': 'str',
        'grouping_sequence_variable_name': 'str',
        'grouping_ascending': 'bool',
        'grouping_sequence': 'str',
        'group_max': 'int'
    }

    attribute_map = {
        'variable_name': 'variableName',
        'order_expression': 'orderExpression',
        'expression': 'expression',
        'direction': 'direction',
        'value': 'value',
        'percent': 'percent',
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'sequence': 'sequence',
        'grouping_variable_name': 'groupingVariableName',
        'grouping_sequence_variable_name': 'groupingSequenceVariableName',
        'grouping_ascending': 'groupingAscending',
        'grouping_sequence': 'groupingSequence',
        'group_max': 'groupMax'
    }

    def __init__(self, variable_name=None, order_expression=None, expression=None, direction=None, value=None, percent=None, min_value=None, max_value=None, sequence=None, grouping_variable_name=None, grouping_sequence_variable_name=None, grouping_ascending=None, grouping_sequence=None, group_max=None, local_vars_configuration=None):  # noqa: E501
        """TopN - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._variable_name = None
        self._order_expression = None
        self._expression = None
        self._direction = None
        self._value = None
        self._percent = None
        self._min_value = None
        self._max_value = None
        self._sequence = None
        self._grouping_variable_name = None
        self._grouping_sequence_variable_name = None
        self._grouping_ascending = None
        self._grouping_sequence = None
        self._group_max = None
        self.discriminator = None

        if variable_name is not None:
            self.variable_name = variable_name
        if order_expression is not None:
            self.order_expression = order_expression
        if expression is not None:
            self.expression = expression
        if direction is not None:
            self.direction = direction
        if value is not None:
            self.value = value
        if percent is not None:
            self.percent = percent
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if sequence is not None:
            self.sequence = sequence
        if grouping_variable_name is not None:
            self.grouping_variable_name = grouping_variable_name
        if grouping_sequence_variable_name is not None:
            self.grouping_sequence_variable_name = grouping_sequence_variable_name
        if grouping_ascending is not None:
            self.grouping_ascending = grouping_ascending
        if grouping_sequence is not None:
            self.grouping_sequence = grouping_sequence
        if group_max is not None:
            self.group_max = group_max

    @property
    def variable_name(self):
        """Gets the variable_name of this TopN.  # noqa: E501


        :return: The variable_name of this TopN.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this TopN.


        :param variable_name: The variable_name of this TopN.  # noqa: E501
        :type variable_name: str
        """

        self._variable_name = variable_name

    @property
    def order_expression(self):
        """Gets the order_expression of this TopN.  # noqa: E501


        :return: The order_expression of this TopN.  # noqa: E501
        :rtype: Expression
        """
        return self._order_expression

    @order_expression.setter
    def order_expression(self, order_expression):
        """Sets the order_expression of this TopN.


        :param order_expression: The order_expression of this TopN.  # noqa: E501
        :type order_expression: Expression
        """

        self._order_expression = order_expression

    @property
    def expression(self):
        """Gets the expression of this TopN.  # noqa: E501


        :return: The expression of this TopN.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this TopN.


        :param expression: The expression of this TopN.  # noqa: E501
        :type expression: str
        """

        self._expression = expression

    @property
    def direction(self):
        """Gets the direction of this TopN.  # noqa: E501


        :return: The direction of this TopN.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TopN.


        :param direction: The direction of this TopN.  # noqa: E501
        :type direction: str
        """
        allowed_values = ["Top", "Bottom", "RangeTopDown", "RangeBottomUp", "PercentRangeTopDown", "PercentRangeBottomUp"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and direction not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def value(self):
        """Gets the value of this TopN.  # noqa: E501


        :return: The value of this TopN.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TopN.


        :param value: The value of this TopN.  # noqa: E501
        :type value: int
        """

        self._value = value

    @property
    def percent(self):
        """Gets the percent of this TopN.  # noqa: E501


        :return: The percent of this TopN.  # noqa: E501
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this TopN.


        :param percent: The percent of this TopN.  # noqa: E501
        :type percent: float
        """

        self._percent = percent

    @property
    def min_value(self):
        """Gets the min_value of this TopN.  # noqa: E501


        :return: The min_value of this TopN.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this TopN.


        :param min_value: The min_value of this TopN.  # noqa: E501
        :type min_value: float
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this TopN.  # noqa: E501


        :return: The max_value of this TopN.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this TopN.


        :param max_value: The max_value of this TopN.  # noqa: E501
        :type max_value: float
        """

        self._max_value = max_value

    @property
    def sequence(self):
        """Gets the sequence of this TopN.  # noqa: E501


        :return: The sequence of this TopN.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this TopN.


        :param sequence: The sequence of this TopN.  # noqa: E501
        :type sequence: str
        """

        self._sequence = sequence

    @property
    def grouping_variable_name(self):
        """Gets the grouping_variable_name of this TopN.  # noqa: E501


        :return: The grouping_variable_name of this TopN.  # noqa: E501
        :rtype: str
        """
        return self._grouping_variable_name

    @grouping_variable_name.setter
    def grouping_variable_name(self, grouping_variable_name):
        """Sets the grouping_variable_name of this TopN.


        :param grouping_variable_name: The grouping_variable_name of this TopN.  # noqa: E501
        :type grouping_variable_name: str
        """

        self._grouping_variable_name = grouping_variable_name

    @property
    def grouping_sequence_variable_name(self):
        """Gets the grouping_sequence_variable_name of this TopN.  # noqa: E501


        :return: The grouping_sequence_variable_name of this TopN.  # noqa: E501
        :rtype: str
        """
        return self._grouping_sequence_variable_name

    @grouping_sequence_variable_name.setter
    def grouping_sequence_variable_name(self, grouping_sequence_variable_name):
        """Sets the grouping_sequence_variable_name of this TopN.


        :param grouping_sequence_variable_name: The grouping_sequence_variable_name of this TopN.  # noqa: E501
        :type grouping_sequence_variable_name: str
        """

        self._grouping_sequence_variable_name = grouping_sequence_variable_name

    @property
    def grouping_ascending(self):
        """Gets the grouping_ascending of this TopN.  # noqa: E501


        :return: The grouping_ascending of this TopN.  # noqa: E501
        :rtype: bool
        """
        return self._grouping_ascending

    @grouping_ascending.setter
    def grouping_ascending(self, grouping_ascending):
        """Sets the grouping_ascending of this TopN.


        :param grouping_ascending: The grouping_ascending of this TopN.  # noqa: E501
        :type grouping_ascending: bool
        """

        self._grouping_ascending = grouping_ascending

    @property
    def grouping_sequence(self):
        """Gets the grouping_sequence of this TopN.  # noqa: E501


        :return: The grouping_sequence of this TopN.  # noqa: E501
        :rtype: str
        """
        return self._grouping_sequence

    @grouping_sequence.setter
    def grouping_sequence(self, grouping_sequence):
        """Sets the grouping_sequence of this TopN.


        :param grouping_sequence: The grouping_sequence of this TopN.  # noqa: E501
        :type grouping_sequence: str
        """

        self._grouping_sequence = grouping_sequence

    @property
    def group_max(self):
        """Gets the group_max of this TopN.  # noqa: E501


        :return: The group_max of this TopN.  # noqa: E501
        :rtype: int
        """
        return self._group_max

    @group_max.setter
    def group_max(self, group_max):
        """Sets the group_max of this TopN.


        :param group_max: The group_max of this TopN.  # noqa: E501
        :type group_max: int
        """

        self._group_max = group_max

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
        if not isinstance(other, TopN):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopN):
            return True

        return self.to_dict() != other.to_dict()
