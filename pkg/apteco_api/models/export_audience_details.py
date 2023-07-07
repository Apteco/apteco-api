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


class ExportAudienceDetails(object):
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
        'maximum_number_of_rows_to_browse': 'int',
        'return_browse_rows': 'bool',
        'filename': 'str',
        'output': 'Output',
        'columns': 'list[Column]',
        'generate_urn_file': 'bool'
    }

    attribute_map = {
        'maximum_number_of_rows_to_browse': 'maximumNumberOfRowsToBrowse',
        'return_browse_rows': 'returnBrowseRows',
        'filename': 'filename',
        'output': 'output',
        'columns': 'columns',
        'generate_urn_file': 'generateUrnFile'
    }

    def __init__(self, maximum_number_of_rows_to_browse=None, return_browse_rows=None, filename=None, output=None, columns=None, generate_urn_file=None, local_vars_configuration=None):  # noqa: E501
        """ExportAudienceDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._maximum_number_of_rows_to_browse = None
        self._return_browse_rows = None
        self._filename = None
        self._output = None
        self._columns = None
        self._generate_urn_file = None
        self.discriminator = None

        self.maximum_number_of_rows_to_browse = maximum_number_of_rows_to_browse
        self.return_browse_rows = return_browse_rows
        if filename is not None:
            self.filename = filename
        if output is not None:
            self.output = output
        self.columns = columns
        self.generate_urn_file = generate_urn_file

    @property
    def maximum_number_of_rows_to_browse(self):
        """Gets the maximum_number_of_rows_to_browse of this ExportAudienceDetails.  # noqa: E501

        The maximum number of rows to return when browsing the data  # noqa: E501

        :return: The maximum_number_of_rows_to_browse of this ExportAudienceDetails.  # noqa: E501
        :rtype: int
        """
        return self._maximum_number_of_rows_to_browse

    @maximum_number_of_rows_to_browse.setter
    def maximum_number_of_rows_to_browse(self, maximum_number_of_rows_to_browse):
        """Sets the maximum_number_of_rows_to_browse of this ExportAudienceDetails.

        The maximum number of rows to return when browsing the data  # noqa: E501

        :param maximum_number_of_rows_to_browse: The maximum_number_of_rows_to_browse of this ExportAudienceDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_number_of_rows_to_browse is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_number_of_rows_to_browse`, must not be `None`")  # noqa: E501

        self._maximum_number_of_rows_to_browse = maximum_number_of_rows_to_browse

    @property
    def return_browse_rows(self):
        """Gets the return_browse_rows of this ExportAudienceDetails.  # noqa: E501

        Whether to return data rows in the response or just export data to a file  # noqa: E501

        :return: The return_browse_rows of this ExportAudienceDetails.  # noqa: E501
        :rtype: bool
        """
        return self._return_browse_rows

    @return_browse_rows.setter
    def return_browse_rows(self, return_browse_rows):
        """Sets the return_browse_rows of this ExportAudienceDetails.

        Whether to return data rows in the response or just export data to a file  # noqa: E501

        :param return_browse_rows: The return_browse_rows of this ExportAudienceDetails.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and return_browse_rows is None:  # noqa: E501
            raise ValueError("Invalid value for `return_browse_rows`, must not be `None`")  # noqa: E501

        self._return_browse_rows = return_browse_rows

    @property
    def filename(self):
        """Gets the filename of this ExportAudienceDetails.  # noqa: E501

        If specified, the filename of a file to create, containing the full export data.  The file will be created in the directory for the associated audience, as configured in the API  # noqa: E501

        :return: The filename of this ExportAudienceDetails.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ExportAudienceDetails.

        If specified, the filename of a file to create, containing the full export data.  The file will be created in the directory for the associated audience, as configured in the API  # noqa: E501

        :param filename: The filename of this ExportAudienceDetails.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def output(self):
        """Gets the output of this ExportAudienceDetails.  # noqa: E501


        :return: The output of this ExportAudienceDetails.  # noqa: E501
        :rtype: Output
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ExportAudienceDetails.


        :param output: The output of this ExportAudienceDetails.  # noqa: E501
        :type: Output
        """

        self._output = output

    @property
    def columns(self):
        """Gets the columns of this ExportAudienceDetails.  # noqa: E501

        The list of columns to include in this export  # noqa: E501

        :return: The columns of this ExportAudienceDetails.  # noqa: E501
        :rtype: list[Column]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ExportAudienceDetails.

        The list of columns to include in this export  # noqa: E501

        :param columns: The columns of this ExportAudienceDetails.  # noqa: E501
        :type: list[Column]
        """
        if self.local_vars_configuration.client_side_validation and columns is None:  # noqa: E501
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def generate_urn_file(self):
        """Gets the generate_urn_file of this ExportAudienceDetails.  # noqa: E501

        Whether to generate a URN file with this export or not  # noqa: E501

        :return: The generate_urn_file of this ExportAudienceDetails.  # noqa: E501
        :rtype: bool
        """
        return self._generate_urn_file

    @generate_urn_file.setter
    def generate_urn_file(self, generate_urn_file):
        """Sets the generate_urn_file of this ExportAudienceDetails.

        Whether to generate a URN file with this export or not  # noqa: E501

        :param generate_urn_file: The generate_urn_file of this ExportAudienceDetails.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and generate_urn_file is None:  # noqa: E501
            raise ValueError("Invalid value for `generate_urn_file`, must not be `None`")  # noqa: E501

        self._generate_urn_file = generate_urn_file

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
        if not isinstance(other, ExportAudienceDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportAudienceDetails):
            return True

        return self.to_dict() != other.to_dict()