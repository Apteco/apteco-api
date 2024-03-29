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


class LastRunDetails(object):
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
        'system_load_date': 'datetime',
        'user_name': 'str',
        'run_date': 'datetime'
    }

    attribute_map = {
        'system_name': 'systemName',
        'system_load_date': 'systemLoadDate',
        'user_name': 'userName',
        'run_date': 'runDate'
    }

    def __init__(self, system_name=None, system_load_date=None, user_name=None, run_date=None, local_vars_configuration=None):  # noqa: E501
        """LastRunDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_name = None
        self._system_load_date = None
        self._user_name = None
        self._run_date = None
        self.discriminator = None

        if system_name is not None:
            self.system_name = system_name
        if system_load_date is not None:
            self.system_load_date = system_load_date
        if user_name is not None:
            self.user_name = user_name
        if run_date is not None:
            self.run_date = run_date

    @property
    def system_name(self):
        """Gets the system_name of this LastRunDetails.  # noqa: E501


        :return: The system_name of this LastRunDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this LastRunDetails.


        :param system_name: The system_name of this LastRunDetails.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def system_load_date(self):
        """Gets the system_load_date of this LastRunDetails.  # noqa: E501


        :return: The system_load_date of this LastRunDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._system_load_date

    @system_load_date.setter
    def system_load_date(self, system_load_date):
        """Sets the system_load_date of this LastRunDetails.


        :param system_load_date: The system_load_date of this LastRunDetails.  # noqa: E501
        :type: datetime
        """

        self._system_load_date = system_load_date

    @property
    def user_name(self):
        """Gets the user_name of this LastRunDetails.  # noqa: E501


        :return: The user_name of this LastRunDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this LastRunDetails.


        :param user_name: The user_name of this LastRunDetails.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def run_date(self):
        """Gets the run_date of this LastRunDetails.  # noqa: E501


        :return: The run_date of this LastRunDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._run_date

    @run_date.setter
    def run_date(self, run_date):
        """Sets the run_date of this LastRunDetails.


        :param run_date: The run_date of this LastRunDetails.  # noqa: E501
        :type: datetime
        """

        self._run_date = run_date

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
        if not isinstance(other, LastRunDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LastRunDetails):
            return True

        return self.to_dict() != other.to_dict()
