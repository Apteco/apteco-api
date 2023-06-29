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


class Export(object):
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
        'base_query': 'Query',
        'resolve_table_name': 'str',
        'maximum_number_of_rows_to_browse': 'int',
        'return_browse_rows': 'bool',
        'path_to_export_to': 'str',
        'output': 'Output',
        'columns': 'list[Column]',
        'limits': 'Limits'
    }

    attribute_map = {
        'base_query': 'baseQuery',
        'resolve_table_name': 'resolveTableName',
        'maximum_number_of_rows_to_browse': 'maximumNumberOfRowsToBrowse',
        'return_browse_rows': 'returnBrowseRows',
        'path_to_export_to': 'pathToExportTo',
        'output': 'output',
        'columns': 'columns',
        'limits': 'limits'
    }

    def __init__(self, base_query=None, resolve_table_name=None, maximum_number_of_rows_to_browse=None, return_browse_rows=None, path_to_export_to=None, output=None, columns=None, limits=None, local_vars_configuration=None):  # noqa: E501
        """Export - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_query = None
        self._resolve_table_name = None
        self._maximum_number_of_rows_to_browse = None
        self._return_browse_rows = None
        self._path_to_export_to = None
        self._output = None
        self._columns = None
        self._limits = None
        self.discriminator = None

        self.base_query = base_query
        self.resolve_table_name = resolve_table_name
        self.maximum_number_of_rows_to_browse = maximum_number_of_rows_to_browse
        self.return_browse_rows = return_browse_rows
        if path_to_export_to is not None:
            self.path_to_export_to = path_to_export_to
        if output is not None:
            self.output = output
        self.columns = columns
        if limits is not None:
            self.limits = limits

    @property
    def base_query(self):
        """Gets the base_query of this Export.  # noqa: E501


        :return: The base_query of this Export.  # noqa: E501
        :rtype: Query
        """
        return self._base_query

    @base_query.setter
    def base_query(self, base_query):
        """Sets the base_query of this Export.


        :param base_query: The base_query of this Export.  # noqa: E501
        :type base_query: Query
        """
        if self.local_vars_configuration.client_side_validation and base_query is None:  # noqa: E501
            raise ValueError("Invalid value for `base_query`, must not be `None`")  # noqa: E501

        self._base_query = base_query

    @property
    def resolve_table_name(self):
        """Gets the resolve_table_name of this Export.  # noqa: E501

        The name of the table to resolve this export to.  I.e. each row will correspond to one record from this table  # noqa: E501

        :return: The resolve_table_name of this Export.  # noqa: E501
        :rtype: str
        """
        return self._resolve_table_name

    @resolve_table_name.setter
    def resolve_table_name(self, resolve_table_name):
        """Sets the resolve_table_name of this Export.

        The name of the table to resolve this export to.  I.e. each row will correspond to one record from this table  # noqa: E501

        :param resolve_table_name: The resolve_table_name of this Export.  # noqa: E501
        :type resolve_table_name: str
        """
        if self.local_vars_configuration.client_side_validation and resolve_table_name is None:  # noqa: E501
            raise ValueError("Invalid value for `resolve_table_name`, must not be `None`")  # noqa: E501

        self._resolve_table_name = resolve_table_name

    @property
    def maximum_number_of_rows_to_browse(self):
        """Gets the maximum_number_of_rows_to_browse of this Export.  # noqa: E501

        The maximum number of rows to return in the browse results  # noqa: E501

        :return: The maximum_number_of_rows_to_browse of this Export.  # noqa: E501
        :rtype: int
        """
        return self._maximum_number_of_rows_to_browse

    @maximum_number_of_rows_to_browse.setter
    def maximum_number_of_rows_to_browse(self, maximum_number_of_rows_to_browse):
        """Sets the maximum_number_of_rows_to_browse of this Export.

        The maximum number of rows to return in the browse results  # noqa: E501

        :param maximum_number_of_rows_to_browse: The maximum_number_of_rows_to_browse of this Export.  # noqa: E501
        :type maximum_number_of_rows_to_browse: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_number_of_rows_to_browse is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_number_of_rows_to_browse`, must not be `None`")  # noqa: E501

        self._maximum_number_of_rows_to_browse = maximum_number_of_rows_to_browse

    @property
    def return_browse_rows(self):
        """Gets the return_browse_rows of this Export.  # noqa: E501

        Whether to output browse rows as well as generating a file  # noqa: E501

        :return: The return_browse_rows of this Export.  # noqa: E501
        :rtype: bool
        """
        return self._return_browse_rows

    @return_browse_rows.setter
    def return_browse_rows(self, return_browse_rows):
        """Sets the return_browse_rows of this Export.

        Whether to output browse rows as well as generating a file  # noqa: E501

        :param return_browse_rows: The return_browse_rows of this Export.  # noqa: E501
        :type return_browse_rows: bool
        """
        if self.local_vars_configuration.client_side_validation and return_browse_rows is None:  # noqa: E501
            raise ValueError("Invalid value for `return_browse_rows`, must not be `None`")  # noqa: E501

        self._return_browse_rows = return_browse_rows

    @property
    def path_to_export_to(self):
        """Gets the path_to_export_to of this Export.  # noqa: E501

        The path of the file to export results to  # noqa: E501

        :return: The path_to_export_to of this Export.  # noqa: E501
        :rtype: str
        """
        return self._path_to_export_to

    @path_to_export_to.setter
    def path_to_export_to(self, path_to_export_to):
        """Sets the path_to_export_to of this Export.

        The path of the file to export results to  # noqa: E501

        :param path_to_export_to: The path_to_export_to of this Export.  # noqa: E501
        :type path_to_export_to: str
        """

        self._path_to_export_to = path_to_export_to

    @property
    def output(self):
        """Gets the output of this Export.  # noqa: E501


        :return: The output of this Export.  # noqa: E501
        :rtype: Output
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this Export.


        :param output: The output of this Export.  # noqa: E501
        :type output: Output
        """

        self._output = output

    @property
    def columns(self):
        """Gets the columns of this Export.  # noqa: E501

        The name of the table to resolve this export to.  I.e. each row will correspond to one record from this table  # noqa: E501

        :return: The columns of this Export.  # noqa: E501
        :rtype: list[Column]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Export.

        The name of the table to resolve this export to.  I.e. each row will correspond to one record from this table  # noqa: E501

        :param columns: The columns of this Export.  # noqa: E501
        :type columns: list[Column]
        """
        if self.local_vars_configuration.client_side_validation and columns is None:  # noqa: E501
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def limits(self):
        """Gets the limits of this Export.  # noqa: E501


        :return: The limits of this Export.  # noqa: E501
        :rtype: Limits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Export.


        :param limits: The limits of this Export.  # noqa: E501
        :type limits: Limits
        """

        self._limits = limits

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
        if not isinstance(other, Export):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Export):
            return True

        return self.to_dict() != other.to_dict()
