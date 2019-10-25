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


class Selection(object):
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
        'ancestor_counts': 'bool',
        'record_set': 'RecordSet',
        'rule': 'Rule',
        'rfv': 'RFV',
        'n_per': 'NPer',
        'top_n': 'TopN',
        'limits': 'Limits',
        'table_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'ancestor_counts': 'ancestorCounts',
        'record_set': 'recordSet',
        'rule': 'rule',
        'rfv': 'rfv',
        'n_per': 'nPer',
        'top_n': 'topN',
        'limits': 'limits',
        'table_name': 'tableName',
        'name': 'name'
    }

    def __init__(self, ancestor_counts=None, record_set=None, rule=None, rfv=None, n_per=None, top_n=None, limits=None, table_name=None, name=None):  # noqa: E501
        """Selection - a model defined in OpenAPI"""  # noqa: E501

        self._ancestor_counts = None
        self._record_set = None
        self._rule = None
        self._rfv = None
        self._n_per = None
        self._top_n = None
        self._limits = None
        self._table_name = None
        self._name = None
        self.discriminator = None

        if ancestor_counts is not None:
            self.ancestor_counts = ancestor_counts
        if record_set is not None:
            self.record_set = record_set
        if rule is not None:
            self.rule = rule
        if rfv is not None:
            self.rfv = rfv
        if n_per is not None:
            self.n_per = n_per
        if top_n is not None:
            self.top_n = top_n
        if limits is not None:
            self.limits = limits
        self.table_name = table_name
        if name is not None:
            self.name = name

    @property
    def ancestor_counts(self):
        """Gets the ancestor_counts of this Selection.  # noqa: E501


        :return: The ancestor_counts of this Selection.  # noqa: E501
        :rtype: bool
        """
        return self._ancestor_counts

    @ancestor_counts.setter
    def ancestor_counts(self, ancestor_counts):
        """Sets the ancestor_counts of this Selection.


        :param ancestor_counts: The ancestor_counts of this Selection.  # noqa: E501
        :type: bool
        """

        self._ancestor_counts = ancestor_counts

    @property
    def record_set(self):
        """Gets the record_set of this Selection.  # noqa: E501


        :return: The record_set of this Selection.  # noqa: E501
        :rtype: RecordSet
        """
        return self._record_set

    @record_set.setter
    def record_set(self, record_set):
        """Sets the record_set of this Selection.


        :param record_set: The record_set of this Selection.  # noqa: E501
        :type: RecordSet
        """

        self._record_set = record_set

    @property
    def rule(self):
        """Gets the rule of this Selection.  # noqa: E501


        :return: The rule of this Selection.  # noqa: E501
        :rtype: Rule
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this Selection.


        :param rule: The rule of this Selection.  # noqa: E501
        :type: Rule
        """

        self._rule = rule

    @property
    def rfv(self):
        """Gets the rfv of this Selection.  # noqa: E501


        :return: The rfv of this Selection.  # noqa: E501
        :rtype: RFV
        """
        return self._rfv

    @rfv.setter
    def rfv(self, rfv):
        """Sets the rfv of this Selection.


        :param rfv: The rfv of this Selection.  # noqa: E501
        :type: RFV
        """

        self._rfv = rfv

    @property
    def n_per(self):
        """Gets the n_per of this Selection.  # noqa: E501


        :return: The n_per of this Selection.  # noqa: E501
        :rtype: NPer
        """
        return self._n_per

    @n_per.setter
    def n_per(self, n_per):
        """Sets the n_per of this Selection.


        :param n_per: The n_per of this Selection.  # noqa: E501
        :type: NPer
        """

        self._n_per = n_per

    @property
    def top_n(self):
        """Gets the top_n of this Selection.  # noqa: E501


        :return: The top_n of this Selection.  # noqa: E501
        :rtype: TopN
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this Selection.


        :param top_n: The top_n of this Selection.  # noqa: E501
        :type: TopN
        """

        self._top_n = top_n

    @property
    def limits(self):
        """Gets the limits of this Selection.  # noqa: E501


        :return: The limits of this Selection.  # noqa: E501
        :rtype: Limits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Selection.


        :param limits: The limits of this Selection.  # noqa: E501
        :type: Limits
        """

        self._limits = limits

    @property
    def table_name(self):
        """Gets the table_name of this Selection.  # noqa: E501


        :return: The table_name of this Selection.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this Selection.


        :param table_name: The table_name of this Selection.  # noqa: E501
        :type: str
        """
        if table_name is None:
            raise ValueError("Invalid value for `table_name`, must not be `None`")  # noqa: E501

        self._table_name = table_name

    @property
    def name(self):
        """Gets the name of this Selection.  # noqa: E501


        :return: The name of this Selection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Selection.


        :param name: The name of this Selection.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Selection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
