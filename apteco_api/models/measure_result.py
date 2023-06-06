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


class MeasureResult(object):
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
        'rows': 'list[str]',
        'cells': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'rows': 'rows',
        'cells': 'cells'
    }

    def __init__(self, id=None, rows=None, cells=None, local_vars_configuration=None):  # noqa: E501
        """MeasureResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._rows = None
        self._cells = None
        self.discriminator = None

        self.id = id
        self.rows = rows
        self.cells = cells

    @property
    def id(self):
        """Gets the id of this MeasureResult.  # noqa: E501

        The id of the measure  # noqa: E501

        :return: The id of this MeasureResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MeasureResult.

        The id of the measure  # noqa: E501

        :param id: The id of this MeasureResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def rows(self):
        """Gets the rows of this MeasureResult.  # noqa: E501

        If the cube is a full cube then a set of rows containing a tab delimeted set of values.  The number of values in each row will be one per category in the first dimension.  If there is a second dimension then there will be one row for each category in the second dimension.  If there are three dimensions then there will be a set of rows (holding the data for all the cells in dimensions 1 and 2) for each category in dimension 3.  # noqa: E501

        :return: The rows of this MeasureResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this MeasureResult.

        If the cube is a full cube then a set of rows containing a tab delimeted set of values.  The number of values in each row will be one per category in the first dimension.  If there is a second dimension then there will be one row for each category in the second dimension.  If there are three dimensions then there will be a set of rows (holding the data for all the cells in dimensions 1 and 2) for each category in dimension 3.  # noqa: E501

        :param rows: The rows of this MeasureResult.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and rows is None:  # noqa: E501
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501

        self._rows = rows

    @property
    def cells(self):
        """Gets the cells of this MeasureResult.  # noqa: E501

        If he cube is a sparse cube then there will be a set of cells, each containing a way of indexing the cell in the cube and then the value of that cell.  # noqa: E501

        :return: The cells of this MeasureResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """Sets the cells of this MeasureResult.

        If he cube is a sparse cube then there will be a set of cells, each containing a way of indexing the cell in the cube and then the value of that cell.  # noqa: E501

        :param cells: The cells of this MeasureResult.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and cells is None:  # noqa: E501
            raise ValueError("Invalid value for `cells`, must not be `None`")  # noqa: E501

        self._cells = cells

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
        if not isinstance(other, MeasureResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeasureResult):
            return True

        return self.to_dict() != other.to_dict()
