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


class CalculateAudienceDetails(object):
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
        'generate_urn_file': 'bool'
    }

    attribute_map = {
        'generate_urn_file': 'generateUrnFile'
    }

    def __init__(self, generate_urn_file=None, local_vars_configuration=None):  # noqa: E501
        """CalculateAudienceDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._generate_urn_file = None
        self.discriminator = None

        self.generate_urn_file = generate_urn_file

    @property
    def generate_urn_file(self):
        """Gets the generate_urn_file of this CalculateAudienceDetails.  # noqa: E501

        Whether to generate a URN file with this count or not  # noqa: E501

        :return: The generate_urn_file of this CalculateAudienceDetails.  # noqa: E501
        :rtype: bool
        """
        return self._generate_urn_file

    @generate_urn_file.setter
    def generate_urn_file(self, generate_urn_file):
        """Sets the generate_urn_file of this CalculateAudienceDetails.

        Whether to generate a URN file with this count or not  # noqa: E501

        :param generate_urn_file: The generate_urn_file of this CalculateAudienceDetails.  # noqa: E501
        :type generate_urn_file: bool
        """
        if self.local_vars_configuration.client_side_validation and generate_urn_file is None:  # noqa: E501
            raise ValueError("Invalid value for `generate_urn_file`, must not be `None`")  # noqa: E501

        self._generate_urn_file = generate_urn_file

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
        if not isinstance(other, CalculateAudienceDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalculateAudienceDetails):
            return True

        return self.to_dict() != other.to_dict()
