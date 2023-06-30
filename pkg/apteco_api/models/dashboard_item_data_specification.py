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


class DashboardItemDataSpecification(object):
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
        'cube_specification': 'CubeSpecification',
        'pareto_specification': 'ParetoSpecification'
    }

    attribute_map = {
        'cube_specification': 'cubeSpecification',
        'pareto_specification': 'paretoSpecification'
    }

    def __init__(self, cube_specification=None, pareto_specification=None, local_vars_configuration=None):  # noqa: E501
        """DashboardItemDataSpecification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cube_specification = None
        self._pareto_specification = None
        self.discriminator = None

        if cube_specification is not None:
            self.cube_specification = cube_specification
        if pareto_specification is not None:
            self.pareto_specification = pareto_specification

    @property
    def cube_specification(self):
        """Gets the cube_specification of this DashboardItemDataSpecification.  # noqa: E501


        :return: The cube_specification of this DashboardItemDataSpecification.  # noqa: E501
        :rtype: CubeSpecification
        """
        return self._cube_specification

    @cube_specification.setter
    def cube_specification(self, cube_specification):
        """Sets the cube_specification of this DashboardItemDataSpecification.


        :param cube_specification: The cube_specification of this DashboardItemDataSpecification.  # noqa: E501
        :type: CubeSpecification
        """

        self._cube_specification = cube_specification

    @property
    def pareto_specification(self):
        """Gets the pareto_specification of this DashboardItemDataSpecification.  # noqa: E501


        :return: The pareto_specification of this DashboardItemDataSpecification.  # noqa: E501
        :rtype: ParetoSpecification
        """
        return self._pareto_specification

    @pareto_specification.setter
    def pareto_specification(self, pareto_specification):
        """Sets the pareto_specification of this DashboardItemDataSpecification.


        :param pareto_specification: The pareto_specification of this DashboardItemDataSpecification.  # noqa: E501
        :type: ParetoSpecification
        """

        self._pareto_specification = pareto_specification

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
        if not isinstance(other, DashboardItemDataSpecification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardItemDataSpecification):
            return True

        return self.to_dict() != other.to_dict()
