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


class ElementDetail(object):
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
        'description': 'str',
        'type': 'str',
        'schema_id': 'int',
        'schema_id_type': 'str',
        'parent_id': 'str',
        'parent_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'type': 'type',
        'schema_id': 'schemaId',
        'schema_id_type': 'schemaIdType',
        'parent_id': 'parentId',
        'parent_type': 'parentType'
    }

    def __init__(self, id=None, description=None, type=None, schema_id=None, schema_id_type=None, parent_id=None, parent_type=None):  # noqa: E501
        """ElementDetail - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._description = None
        self._type = None
        self._schema_id = None
        self._schema_id_type = None
        self._parent_id = None
        self._parent_type = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.type = type
        if schema_id is not None:
            self.schema_id = schema_id
        if schema_id_type is not None:
            self.schema_id_type = schema_id_type
        self.parent_id = parent_id
        self.parent_type = parent_type

    @property
    def id(self):
        """Gets the id of this ElementDetail.  # noqa: E501

        The element's id  # noqa: E501

        :return: The id of this ElementDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElementDetail.

        The element's id  # noqa: E501

        :param id: The id of this ElementDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this ElementDetail.  # noqa: E501

        The element's description  # noqa: E501

        :return: The description of this ElementDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ElementDetail.

        The element's description  # noqa: E501

        :param description: The description of this ElementDetail.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this ElementDetail.  # noqa: E501

        The element's type  # noqa: E501

        :return: The type of this ElementDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElementDetail.

        The element's type  # noqa: E501

        :param type: The type of this ElementDetail.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "Diagram", "Programme", "Area", "Campaign", "Message", "Group", "Audience", "Content", "Delivery", "Pool", "Responses", "Transition", "PauseAction"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def schema_id(self):
        """Gets the schema_id of this ElementDetail.  # noqa: E501

        The element's schema id - if it has one.  This is the key field into the PeopleStage schema tables such as ProcessDefinition.  Published elements should have a schema id.  # noqa: E501

        :return: The schema_id of this ElementDetail.  # noqa: E501
        :rtype: int
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this ElementDetail.

        The element's schema id - if it has one.  This is the key field into the PeopleStage schema tables such as ProcessDefinition.  Published elements should have a schema id.  # noqa: E501

        :param schema_id: The schema_id of this ElementDetail.  # noqa: E501
        :type: int
        """

        self._schema_id = schema_id

    @property
    def schema_id_type(self):
        """Gets the schema_id_type of this ElementDetail.  # noqa: E501

        The type of the element's schema id - if it has a schema id.  Published elements should have a schema id and type.  # noqa: E501

        :return: The schema_id_type of this ElementDetail.  # noqa: E501
        :rtype: str
        """
        return self._schema_id_type

    @schema_id_type.setter
    def schema_id_type(self, schema_id_type):
        """Sets the schema_id_type of this ElementDetail.

        The type of the element's schema id - if it has a schema id.  Published elements should have a schema id and type.  # noqa: E501

        :param schema_id_type: The schema_id_type of this ElementDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "ProcessId"]  # noqa: E501
        if schema_id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schema_id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(schema_id_type, allowed_values)
            )

        self._schema_id_type = schema_id_type

    @property
    def parent_id(self):
        """Gets the parent_id of this ElementDetail.  # noqa: E501

        The parent of this element's id  # noqa: E501

        :return: The parent_id of this ElementDetail.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ElementDetail.

        The parent of this element's id  # noqa: E501

        :param parent_id: The parent_id of this ElementDetail.  # noqa: E501
        :type: str
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def parent_type(self):
        """Gets the parent_type of this ElementDetail.  # noqa: E501

        The parent of this element's type  # noqa: E501

        :return: The parent_type of this ElementDetail.  # noqa: E501
        :rtype: str
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        """Sets the parent_type of this ElementDetail.

        The parent of this element's type  # noqa: E501

        :param parent_type: The parent_type of this ElementDetail.  # noqa: E501
        :type: str
        """
        if parent_type is None:
            raise ValueError("Invalid value for `parent_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "Diagram", "Programme", "Area", "Campaign", "Message", "Group", "Audience", "Content", "Delivery", "Pool", "Responses", "Transition", "PauseAction"]  # noqa: E501
        if parent_type not in allowed_values:
            raise ValueError(
                "Invalid value for `parent_type` ({0}), must be one of {1}"  # noqa: E501
                .format(parent_type, allowed_values)
            )

        self._parent_type = parent_type

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
        if not isinstance(other, ElementDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
