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


class ModifyUserCollectionDetail(object):
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
        'status': 'str',
        'title': 'str',
        'description': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'status': 'status',
        'title': 'title',
        'description': 'description',
        'file_path': 'filePath'
    }

    def __init__(self, status=None, title=None, description=None, file_path=None, local_vars_configuration=None):  # noqa: E501
        """ModifyUserCollectionDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._title = None
        self._description = None
        self._file_path = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if file_path is not None:
            self.file_path = file_path

    @property
    def status(self):
        """Gets the status of this ModifyUserCollectionDetail.  # noqa: E501

        The status of the collection  # noqa: E501

        :return: The status of this ModifyUserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModifyUserCollectionDetail.

        The status of the collection  # noqa: E501

        :param status: The status of this ModifyUserCollectionDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "Pinned", "Archived"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self):
        """Gets the title of this ModifyUserCollectionDetail.  # noqa: E501

        The title of the collection  # noqa: E501

        :return: The title of this ModifyUserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ModifyUserCollectionDetail.

        The title of the collection  # noqa: E501

        :param title: The title of this ModifyUserCollectionDetail.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this ModifyUserCollectionDetail.  # noqa: E501

        The description of the collection  # noqa: E501

        :return: The description of this ModifyUserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyUserCollectionDetail.

        The description of the collection  # noqa: E501

        :param description: The description of this ModifyUserCollectionDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_path(self):
        """Gets the file_path of this ModifyUserCollectionDetail.  # noqa: E501

        The path to the file that contains the parts of this collection  # noqa: E501

        :return: The file_path of this ModifyUserCollectionDetail.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ModifyUserCollectionDetail.

        The path to the file that contains the parts of this collection  # noqa: E501

        :param file_path: The file_path of this ModifyUserCollectionDetail.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

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
        if not isinstance(other, ModifyUserCollectionDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyUserCollectionDetail):
            return True

        return self.to_dict() != other.to_dict()
