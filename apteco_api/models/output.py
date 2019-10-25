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


class Output(object):
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
        'format': 'str',
        'delimiter': 'str',
        'alpha_encloser': 'str',
        'numeric_encloser': 'str',
        'authorisation_code': 'str'
    }

    attribute_map = {
        'format': 'format',
        'delimiter': 'delimiter',
        'alpha_encloser': 'alphaEncloser',
        'numeric_encloser': 'numericEncloser',
        'authorisation_code': 'authorisationCode'
    }

    def __init__(self, format=None, delimiter=None, alpha_encloser=None, numeric_encloser=None, authorisation_code=None):  # noqa: E501
        """Output - a model defined in OpenAPI"""  # noqa: E501

        self._format = None
        self._delimiter = None
        self._alpha_encloser = None
        self._numeric_encloser = None
        self._authorisation_code = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if delimiter is not None:
            self.delimiter = delimiter
        if alpha_encloser is not None:
            self.alpha_encloser = alpha_encloser
        if numeric_encloser is not None:
            self.numeric_encloser = numeric_encloser
        if authorisation_code is not None:
            self.authorisation_code = authorisation_code

    @property
    def format(self):
        """Gets the format of this Output.  # noqa: E501

        The format of the file to generate  # noqa: E501

        :return: The format of this Output.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Output.

        The format of the file to generate  # noqa: E501

        :param format: The format of this Output.  # noqa: E501
        :type: str
        """
        allowed_values = ["CSV", "SDF", "XLSX", "MDB", "DBF", "URN"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def delimiter(self):
        """Gets the delimiter of this Output.  # noqa: E501

        The delimiter character to use when outputting a delimited file.  Specify one character only  # noqa: E501

        :return: The delimiter of this Output.  # noqa: E501
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this Output.

        The delimiter character to use when outputting a delimited file.  Specify one character only  # noqa: E501

        :param delimiter: The delimiter of this Output.  # noqa: E501
        :type: str
        """

        self._delimiter = delimiter

    @property
    def alpha_encloser(self):
        """Gets the alpha_encloser of this Output.  # noqa: E501

        The alpha encloser character to use when outputting a delimited file.  Specify one character only  # noqa: E501

        :return: The alpha_encloser of this Output.  # noqa: E501
        :rtype: str
        """
        return self._alpha_encloser

    @alpha_encloser.setter
    def alpha_encloser(self, alpha_encloser):
        """Sets the alpha_encloser of this Output.

        The alpha encloser character to use when outputting a delimited file.  Specify one character only  # noqa: E501

        :param alpha_encloser: The alpha_encloser of this Output.  # noqa: E501
        :type: str
        """

        self._alpha_encloser = alpha_encloser

    @property
    def numeric_encloser(self):
        """Gets the numeric_encloser of this Output.  # noqa: E501

        The delimiter character to use when outputting a delimited file.  Specify one character only  # noqa: E501

        :return: The numeric_encloser of this Output.  # noqa: E501
        :rtype: str
        """
        return self._numeric_encloser

    @numeric_encloser.setter
    def numeric_encloser(self, numeric_encloser):
        """Sets the numeric_encloser of this Output.

        The delimiter character to use when outputting a delimited file.  Specify one character only  # noqa: E501

        :param numeric_encloser: The numeric_encloser of this Output.  # noqa: E501
        :type: str
        """

        self._numeric_encloser = numeric_encloser

    @property
    def authorisation_code(self):
        """Gets the authorisation_code of this Output.  # noqa: E501

        The velocity authorisation code string  # noqa: E501

        :return: The authorisation_code of this Output.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, authorisation_code):
        """Sets the authorisation_code of this Output.

        The velocity authorisation code string  # noqa: E501

        :param authorisation_code: The authorisation_code of this Output.  # noqa: E501
        :type: str
        """

        self._authorisation_code = authorisation_code

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
        if not isinstance(other, Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
