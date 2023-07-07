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


class CheckDimensionResult(object):
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
        'codes': 'str',
        'descriptions': 'str',
        'base_counts': 'str',
        'audience_counts': 'str'
    }

    attribute_map = {
        'id': 'id',
        'codes': 'codes',
        'descriptions': 'descriptions',
        'base_counts': 'baseCounts',
        'audience_counts': 'audienceCounts'
    }

    def __init__(self, id=None, codes=None, descriptions=None, base_counts=None, audience_counts=None, local_vars_configuration=None):  # noqa: E501
        """CheckDimensionResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._codes = None
        self._descriptions = None
        self._base_counts = None
        self._audience_counts = None
        self.discriminator = None

        self.id = id
        self.codes = codes
        self.descriptions = descriptions
        self.base_counts = base_counts
        self.audience_counts = audience_counts

    @property
    def id(self):
        """Gets the id of this CheckDimensionResult.  # noqa: E501

        The id of the dimension  # noqa: E501

        :return: The id of this CheckDimensionResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckDimensionResult.

        The id of the dimension  # noqa: E501

        :param id: The id of this CheckDimensionResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def codes(self):
        """Gets the codes of this CheckDimensionResult.  # noqa: E501

        A set of tab-delimited codes, one for each category in the dimension  # noqa: E501

        :return: The codes of this CheckDimensionResult.  # noqa: E501
        :rtype: str
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this CheckDimensionResult.

        A set of tab-delimited codes, one for each category in the dimension  # noqa: E501

        :param codes: The codes of this CheckDimensionResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and codes is None:  # noqa: E501
            raise ValueError("Invalid value for `codes`, must not be `None`")  # noqa: E501

        self._codes = codes

    @property
    def descriptions(self):
        """Gets the descriptions of this CheckDimensionResult.  # noqa: E501

        A set of tab-delimited descriptions, one for each category in the dimension  # noqa: E501

        :return: The descriptions of this CheckDimensionResult.  # noqa: E501
        :rtype: str
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """Sets the descriptions of this CheckDimensionResult.

        A set of tab-delimited descriptions, one for each category in the dimension  # noqa: E501

        :param descriptions: The descriptions of this CheckDimensionResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and descriptions is None:  # noqa: E501
            raise ValueError("Invalid value for `descriptions`, must not be `None`")  # noqa: E501

        self._descriptions = descriptions

    @property
    def base_counts(self):
        """Gets the base_counts of this CheckDimensionResult.  # noqa: E501

        A set of tab-delimited counts for the universe, one for each category in the dimension  # noqa: E501

        :return: The base_counts of this CheckDimensionResult.  # noqa: E501
        :rtype: str
        """
        return self._base_counts

    @base_counts.setter
    def base_counts(self, base_counts):
        """Sets the base_counts of this CheckDimensionResult.

        A set of tab-delimited counts for the universe, one for each category in the dimension  # noqa: E501

        :param base_counts: The base_counts of this CheckDimensionResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base_counts is None:  # noqa: E501
            raise ValueError("Invalid value for `base_counts`, must not be `None`")  # noqa: E501

        self._base_counts = base_counts

    @property
    def audience_counts(self):
        """Gets the audience_counts of this CheckDimensionResult.  # noqa: E501

        A set of tab-delimited counts for the audience, one for each category in the dimension  # noqa: E501

        :return: The audience_counts of this CheckDimensionResult.  # noqa: E501
        :rtype: str
        """
        return self._audience_counts

    @audience_counts.setter
    def audience_counts(self, audience_counts):
        """Sets the audience_counts of this CheckDimensionResult.

        A set of tab-delimited counts for the audience, one for each category in the dimension  # noqa: E501

        :param audience_counts: The audience_counts of this CheckDimensionResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and audience_counts is None:  # noqa: E501
            raise ValueError("Invalid value for `audience_counts`, must not be `None`")  # noqa: E501

        self._audience_counts = audience_counts

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
        if not isinstance(other, CheckDimensionResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckDimensionResult):
            return True

        return self.to_dict() != other.to_dict()