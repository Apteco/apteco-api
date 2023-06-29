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


class EmailRequirements(object):
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
        'allow_unrestricted_email_domains': 'bool',
        'restricted_email_domains': 'list[str]'
    }

    attribute_map = {
        'allow_unrestricted_email_domains': 'allowUnrestrictedEmailDomains',
        'restricted_email_domains': 'restrictedEmailDomains'
    }

    def __init__(self, allow_unrestricted_email_domains=None, restricted_email_domains=None, local_vars_configuration=None):  # noqa: E501
        """EmailRequirements - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allow_unrestricted_email_domains = None
        self._restricted_email_domains = None
        self.discriminator = None

        self.allow_unrestricted_email_domains = allow_unrestricted_email_domains
        self.restricted_email_domains = restricted_email_domains

    @property
    def allow_unrestricted_email_domains(self):
        """Gets the allow_unrestricted_email_domains of this EmailRequirements.  # noqa: E501

        Whether the domains of email addresses used to create users or share to users will  be checked against the list of RestrictedEmailDomains  # noqa: E501

        :return: The allow_unrestricted_email_domains of this EmailRequirements.  # noqa: E501
        :rtype: bool
        """
        return self._allow_unrestricted_email_domains

    @allow_unrestricted_email_domains.setter
    def allow_unrestricted_email_domains(self, allow_unrestricted_email_domains):
        """Sets the allow_unrestricted_email_domains of this EmailRequirements.

        Whether the domains of email addresses used to create users or share to users will  be checked against the list of RestrictedEmailDomains  # noqa: E501

        :param allow_unrestricted_email_domains: The allow_unrestricted_email_domains of this EmailRequirements.  # noqa: E501
        :type allow_unrestricted_email_domains: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_unrestricted_email_domains is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_unrestricted_email_domains`, must not be `None`")  # noqa: E501

        self._allow_unrestricted_email_domains = allow_unrestricted_email_domains

    @property
    def restricted_email_domains(self):
        """Gets the restricted_email_domains of this EmailRequirements.  # noqa: E501

        The list of valid email domains available for creating user or sharing with users  If AllowUnrestrictedEmailDomains is false and an attempt is made to create a user  or share to a user with an email address that has a domain not in the list then an  error will be returned.  # noqa: E501

        :return: The restricted_email_domains of this EmailRequirements.  # noqa: E501
        :rtype: list[str]
        """
        return self._restricted_email_domains

    @restricted_email_domains.setter
    def restricted_email_domains(self, restricted_email_domains):
        """Sets the restricted_email_domains of this EmailRequirements.

        The list of valid email domains available for creating user or sharing with users  If AllowUnrestrictedEmailDomains is false and an attempt is made to create a user  or share to a user with an email address that has a domain not in the list then an  error will be returned.  # noqa: E501

        :param restricted_email_domains: The restricted_email_domains of this EmailRequirements.  # noqa: E501
        :type restricted_email_domains: list[str]
        """
        if self.local_vars_configuration.client_side_validation and restricted_email_domains is None:  # noqa: E501
            raise ValueError("Invalid value for `restricted_email_domains`, must not be `None`")  # noqa: E501

        self._restricted_email_domains = restricted_email_domains

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
        if not isinstance(other, EmailRequirements):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailRequirements):
            return True

        return self.to_dict() != other.to_dict()
