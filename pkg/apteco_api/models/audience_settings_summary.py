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


class AudienceSettingsSummary(object):
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
        'system_name': 'str',
        'allow_audience_browser_download_delivery_entry': 'bool',
        'allow_audience_ftp_delivery_entry': 'bool'
    }

    attribute_map = {
        'system_name': 'systemName',
        'allow_audience_browser_download_delivery_entry': 'allowAudienceBrowserDownloadDeliveryEntry',
        'allow_audience_ftp_delivery_entry': 'allowAudienceFtpDeliveryEntry'
    }

    def __init__(self, system_name=None, allow_audience_browser_download_delivery_entry=None, allow_audience_ftp_delivery_entry=None, local_vars_configuration=None):  # noqa: E501
        """AudienceSettingsSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_name = None
        self._allow_audience_browser_download_delivery_entry = None
        self._allow_audience_ftp_delivery_entry = None
        self.discriminator = None

        self.system_name = system_name
        self.allow_audience_browser_download_delivery_entry = allow_audience_browser_download_delivery_entry
        self.allow_audience_ftp_delivery_entry = allow_audience_ftp_delivery_entry

    @property
    def system_name(self):
        """Gets the system_name of this AudienceSettingsSummary.  # noqa: E501

        The name of the system that the settings apply to  # noqa: E501

        :return: The system_name of this AudienceSettingsSummary.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this AudienceSettingsSummary.

        The name of the system that the settings apply to  # noqa: E501

        :param system_name: The system_name of this AudienceSettingsSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_name is None:  # noqa: E501
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501

        self._system_name = system_name

    @property
    def allow_audience_browser_download_delivery_entry(self):
        """Gets the allow_audience_browser_download_delivery_entry of this AudienceSettingsSummary.  # noqa: E501

        Whether an audience is allowed to have exported data delivered directly to the browser for download  # noqa: E501

        :return: The allow_audience_browser_download_delivery_entry of this AudienceSettingsSummary.  # noqa: E501
        :rtype: bool
        """
        return self._allow_audience_browser_download_delivery_entry

    @allow_audience_browser_download_delivery_entry.setter
    def allow_audience_browser_download_delivery_entry(self, allow_audience_browser_download_delivery_entry):
        """Sets the allow_audience_browser_download_delivery_entry of this AudienceSettingsSummary.

        Whether an audience is allowed to have exported data delivered directly to the browser for download  # noqa: E501

        :param allow_audience_browser_download_delivery_entry: The allow_audience_browser_download_delivery_entry of this AudienceSettingsSummary.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_audience_browser_download_delivery_entry is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_audience_browser_download_delivery_entry`, must not be `None`")  # noqa: E501

        self._allow_audience_browser_download_delivery_entry = allow_audience_browser_download_delivery_entry

    @property
    def allow_audience_ftp_delivery_entry(self):
        """Gets the allow_audience_ftp_delivery_entry of this AudienceSettingsSummary.  # noqa: E501

        Whether an audience is allowed to have exported data delivered to an FTP site  # noqa: E501

        :return: The allow_audience_ftp_delivery_entry of this AudienceSettingsSummary.  # noqa: E501
        :rtype: bool
        """
        return self._allow_audience_ftp_delivery_entry

    @allow_audience_ftp_delivery_entry.setter
    def allow_audience_ftp_delivery_entry(self, allow_audience_ftp_delivery_entry):
        """Sets the allow_audience_ftp_delivery_entry of this AudienceSettingsSummary.

        Whether an audience is allowed to have exported data delivered to an FTP site  # noqa: E501

        :param allow_audience_ftp_delivery_entry: The allow_audience_ftp_delivery_entry of this AudienceSettingsSummary.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_audience_ftp_delivery_entry is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_audience_ftp_delivery_entry`, must not be `None`")  # noqa: E501

        self._allow_audience_ftp_delivery_entry = allow_audience_ftp_delivery_entry

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
        if not isinstance(other, AudienceSettingsSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AudienceSettingsSummary):
            return True

        return self.to_dict() != other.to_dict()
