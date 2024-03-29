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


class Table(object):
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
        'name': 'str',
        'singular_display_name': 'str',
        'plural_display_name': 'str',
        'is_default_table': 'bool',
        'is_people_table': 'bool',
        'total_records': 'int',
        'child_relationship_name': 'str',
        'parent_relationship_name': 'str',
        'has_child_tables': 'bool',
        'parent_table': 'str'
    }

    attribute_map = {
        'name': 'name',
        'singular_display_name': 'singularDisplayName',
        'plural_display_name': 'pluralDisplayName',
        'is_default_table': 'isDefaultTable',
        'is_people_table': 'isPeopleTable',
        'total_records': 'totalRecords',
        'child_relationship_name': 'childRelationshipName',
        'parent_relationship_name': 'parentRelationshipName',
        'has_child_tables': 'hasChildTables',
        'parent_table': 'parentTable'
    }

    def __init__(self, name=None, singular_display_name=None, plural_display_name=None, is_default_table=None, is_people_table=None, total_records=None, child_relationship_name=None, parent_relationship_name=None, has_child_tables=None, parent_table=None, local_vars_configuration=None):  # noqa: E501
        """Table - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._singular_display_name = None
        self._plural_display_name = None
        self._is_default_table = None
        self._is_people_table = None
        self._total_records = None
        self._child_relationship_name = None
        self._parent_relationship_name = None
        self._has_child_tables = None
        self._parent_table = None
        self.discriminator = None

        self.name = name
        self.singular_display_name = singular_display_name
        self.plural_display_name = plural_display_name
        self.is_default_table = is_default_table
        self.is_people_table = is_people_table
        self.total_records = total_records
        self.child_relationship_name = child_relationship_name
        self.parent_relationship_name = parent_relationship_name
        self.has_child_tables = has_child_tables
        self.parent_table = parent_table

    @property
    def name(self):
        """Gets the name of this Table.  # noqa: E501

        The name of the table  # noqa: E501

        :return: The name of this Table.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Table.

        The name of the table  # noqa: E501

        :param name: The name of this Table.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def singular_display_name(self):
        """Gets the singular_display_name of this Table.  # noqa: E501

        A description to use for this table when refering to a single entity (i.e. \"A Person\")  # noqa: E501

        :return: The singular_display_name of this Table.  # noqa: E501
        :rtype: str
        """
        return self._singular_display_name

    @singular_display_name.setter
    def singular_display_name(self, singular_display_name):
        """Sets the singular_display_name of this Table.

        A description to use for this table when refering to a single entity (i.e. \"A Person\")  # noqa: E501

        :param singular_display_name: The singular_display_name of this Table.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and singular_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `singular_display_name`, must not be `None`")  # noqa: E501

        self._singular_display_name = singular_display_name

    @property
    def plural_display_name(self):
        """Gets the plural_display_name of this Table.  # noqa: E501

        A description to use for this table when refering to multiple entities (i.e. \"Many People\")  # noqa: E501

        :return: The plural_display_name of this Table.  # noqa: E501
        :rtype: str
        """
        return self._plural_display_name

    @plural_display_name.setter
    def plural_display_name(self, plural_display_name):
        """Sets the plural_display_name of this Table.

        A description to use for this table when refering to multiple entities (i.e. \"Many People\")  # noqa: E501

        :param plural_display_name: The plural_display_name of this Table.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and plural_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `plural_display_name`, must not be `None`")  # noqa: E501

        self._plural_display_name = plural_display_name

    @property
    def is_default_table(self):
        """Gets the is_default_table of this Table.  # noqa: E501

        Whether this table is the default table in the FastStats system or not - i.e. the table to use when creating a blank query  # noqa: E501

        :return: The is_default_table of this Table.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_table

    @is_default_table.setter
    def is_default_table(self, is_default_table):
        """Sets the is_default_table of this Table.

        Whether this table is the default table in the FastStats system or not - i.e. the table to use when creating a blank query  # noqa: E501

        :param is_default_table: The is_default_table of this Table.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_default_table is None:  # noqa: E501
            raise ValueError("Invalid value for `is_default_table`, must not be `None`")  # noqa: E501

        self._is_default_table = is_default_table

    @property
    def is_people_table(self):
        """Gets the is_people_table of this Table.  # noqa: E501

        Whether this table is the one in the FastStats system used to represent natural people  # noqa: E501

        :return: The is_people_table of this Table.  # noqa: E501
        :rtype: bool
        """
        return self._is_people_table

    @is_people_table.setter
    def is_people_table(self, is_people_table):
        """Sets the is_people_table of this Table.

        Whether this table is the one in the FastStats system used to represent natural people  # noqa: E501

        :param is_people_table: The is_people_table of this Table.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_people_table is None:  # noqa: E501
            raise ValueError("Invalid value for `is_people_table`, must not be `None`")  # noqa: E501

        self._is_people_table = is_people_table

    @property
    def total_records(self):
        """Gets the total_records of this Table.  # noqa: E501

        The total number of records in this table  # noqa: E501

        :return: The total_records of this Table.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this Table.

        The total number of records in this table  # noqa: E501

        :param total_records: The total_records of this Table.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_records is None:  # noqa: E501
            raise ValueError("Invalid value for `total_records`, must not be `None`")  # noqa: E501

        self._total_records = total_records

    @property
    def child_relationship_name(self):
        """Gets the child_relationship_name of this Table.  # noqa: E501

        A descriptive word or phrase to use when relating this table to one of its child tables (i.e. a Households \"is occupied by\" a Customer)  # noqa: E501

        :return: The child_relationship_name of this Table.  # noqa: E501
        :rtype: str
        """
        return self._child_relationship_name

    @child_relationship_name.setter
    def child_relationship_name(self, child_relationship_name):
        """Sets the child_relationship_name of this Table.

        A descriptive word or phrase to use when relating this table to one of its child tables (i.e. a Households \"is occupied by\" a Customer)  # noqa: E501

        :param child_relationship_name: The child_relationship_name of this Table.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and child_relationship_name is None:  # noqa: E501
            raise ValueError("Invalid value for `child_relationship_name`, must not be `None`")  # noqa: E501

        self._child_relationship_name = child_relationship_name

    @property
    def parent_relationship_name(self):
        """Gets the parent_relationship_name of this Table.  # noqa: E501

        A descriptive word or phrase to use when relating this table to one of its parent tables (i.e. a Customer \"lives at\" a Households)  # noqa: E501

        :return: The parent_relationship_name of this Table.  # noqa: E501
        :rtype: str
        """
        return self._parent_relationship_name

    @parent_relationship_name.setter
    def parent_relationship_name(self, parent_relationship_name):
        """Sets the parent_relationship_name of this Table.

        A descriptive word or phrase to use when relating this table to one of its parent tables (i.e. a Customer \"lives at\" a Households)  # noqa: E501

        :param parent_relationship_name: The parent_relationship_name of this Table.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parent_relationship_name is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_relationship_name`, must not be `None`")  # noqa: E501

        self._parent_relationship_name = parent_relationship_name

    @property
    def has_child_tables(self):
        """Gets the has_child_tables of this Table.  # noqa: E501

        Whether this table has any child tables  # noqa: E501

        :return: The has_child_tables of this Table.  # noqa: E501
        :rtype: bool
        """
        return self._has_child_tables

    @has_child_tables.setter
    def has_child_tables(self, has_child_tables):
        """Sets the has_child_tables of this Table.

        Whether this table has any child tables  # noqa: E501

        :param has_child_tables: The has_child_tables of this Table.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and has_child_tables is None:  # noqa: E501
            raise ValueError("Invalid value for `has_child_tables`, must not be `None`")  # noqa: E501

        self._has_child_tables = has_child_tables

    @property
    def parent_table(self):
        """Gets the parent_table of this Table.  # noqa: E501

        The name of the parent table for this table.  The Master table is the only table without a parent  # noqa: E501

        :return: The parent_table of this Table.  # noqa: E501
        :rtype: str
        """
        return self._parent_table

    @parent_table.setter
    def parent_table(self, parent_table):
        """Sets the parent_table of this Table.

        The name of the parent table for this table.  The Master table is the only table without a parent  # noqa: E501

        :param parent_table: The parent_table of this Table.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parent_table is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_table`, must not be `None`")  # noqa: E501

        self._parent_table = parent_table

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
        if not isinstance(other, Table):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Table):
            return True

        return self.to_dict() != other.to_dict()
