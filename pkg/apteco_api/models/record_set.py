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


class RecordSet(object):
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
        'type': 'str',
        'key_variable_name': 'str',
        'by_reference': 'bool',
        'path': 'str',
        'transient': 'bool',
        'values': 'str',
        'min_occurs': 'int'
    }

    attribute_map = {
        'type': 'type',
        'key_variable_name': 'keyVariableName',
        'by_reference': 'byReference',
        'path': 'path',
        'transient': 'transient',
        'values': 'values',
        'min_occurs': 'minOccurs'
    }

    def __init__(self, type=None, key_variable_name=None, by_reference=None, path=None, transient=None, values=None, min_occurs=None, local_vars_configuration=None):  # noqa: E501
        """RecordSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._key_variable_name = None
        self._by_reference = None
        self._path = None
        self._transient = None
        self._values = None
        self._min_occurs = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if key_variable_name is not None:
            self.key_variable_name = key_variable_name
        if by_reference is not None:
            self.by_reference = by_reference
        if path is not None:
            self.path = path
        if transient is not None:
            self.transient = transient
        if values is not None:
            self.values = values
        if min_occurs is not None:
            self.min_occurs = min_occurs

    @property
    def type(self):
        """Gets the type of this RecordSet.  # noqa: E501


        :return: The type of this RecordSet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecordSet.


        :param type: The type of this RecordSet.  # noqa: E501
        :type type: str
        """
        allowed_values = ["URN", "SBM", "FSRN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def key_variable_name(self):
        """Gets the key_variable_name of this RecordSet.  # noqa: E501


        :return: The key_variable_name of this RecordSet.  # noqa: E501
        :rtype: str
        """
        return self._key_variable_name

    @key_variable_name.setter
    def key_variable_name(self, key_variable_name):
        """Sets the key_variable_name of this RecordSet.


        :param key_variable_name: The key_variable_name of this RecordSet.  # noqa: E501
        :type key_variable_name: str
        """

        self._key_variable_name = key_variable_name

    @property
    def by_reference(self):
        """Gets the by_reference of this RecordSet.  # noqa: E501


        :return: The by_reference of this RecordSet.  # noqa: E501
        :rtype: bool
        """
        return self._by_reference

    @by_reference.setter
    def by_reference(self, by_reference):
        """Sets the by_reference of this RecordSet.


        :param by_reference: The by_reference of this RecordSet.  # noqa: E501
        :type by_reference: bool
        """

        self._by_reference = by_reference

    @property
    def path(self):
        """Gets the path of this RecordSet.  # noqa: E501


        :return: The path of this RecordSet.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RecordSet.


        :param path: The path of this RecordSet.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def transient(self):
        """Gets the transient of this RecordSet.  # noqa: E501


        :return: The transient of this RecordSet.  # noqa: E501
        :rtype: bool
        """
        return self._transient

    @transient.setter
    def transient(self, transient):
        """Sets the transient of this RecordSet.


        :param transient: The transient of this RecordSet.  # noqa: E501
        :type transient: bool
        """

        self._transient = transient

    @property
    def values(self):
        """Gets the values of this RecordSet.  # noqa: E501


        :return: The values of this RecordSet.  # noqa: E501
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this RecordSet.


        :param values: The values of this RecordSet.  # noqa: E501
        :type values: str
        """

        self._values = values

    @property
    def min_occurs(self):
        """Gets the min_occurs of this RecordSet.  # noqa: E501


        :return: The min_occurs of this RecordSet.  # noqa: E501
        :rtype: int
        """
        return self._min_occurs

    @min_occurs.setter
    def min_occurs(self, min_occurs):
        """Sets the min_occurs of this RecordSet.


        :param min_occurs: The min_occurs of this RecordSet.  # noqa: E501
        :type min_occurs: int
        """

        self._min_occurs = min_occurs

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
        if not isinstance(other, RecordSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordSet):
            return True

        return self.to_dict() != other.to_dict()
