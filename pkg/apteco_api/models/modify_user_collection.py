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


class ModifyUserCollection(object):
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
        'collection': 'ModifyUserCollectionDetail',
        'id': 'int',
        'modification_type': 'str'
    }

    attribute_map = {
        'collection': 'collection',
        'id': 'id',
        'modification_type': 'modificationType'
    }

    def __init__(self, collection=None, id=None, modification_type=None, local_vars_configuration=None):  # noqa: E501
        """ModifyUserCollection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._collection = None
        self._id = None
        self._modification_type = None
        self.discriminator = None

        self.collection = collection
        self.id = id
        self.modification_type = modification_type

    @property
    def collection(self):
        """Gets the collection of this ModifyUserCollection.  # noqa: E501


        :return: The collection of this ModifyUserCollection.  # noqa: E501
        :rtype: ModifyUserCollectionDetail
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this ModifyUserCollection.


        :param collection: The collection of this ModifyUserCollection.  # noqa: E501
        :type collection: ModifyUserCollectionDetail
        """
        if self.local_vars_configuration.client_side_validation and collection is None:  # noqa: E501
            raise ValueError("Invalid value for `collection`, must not be `None`")  # noqa: E501

        self._collection = collection

    @property
    def id(self):
        """Gets the id of this ModifyUserCollection.  # noqa: E501

        The id of the item to update  # noqa: E501

        :return: The id of this ModifyUserCollection.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModifyUserCollection.

        The id of the item to update  # noqa: E501

        :param id: The id of this ModifyUserCollection.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def modification_type(self):
        """Gets the modification_type of this ModifyUserCollection.  # noqa: E501

        The type of modification to perform.  If the type is delete or undelete, any other specified item details will be ignored  # noqa: E501

        :return: The modification_type of this ModifyUserCollection.  # noqa: E501
        :rtype: str
        """
        return self._modification_type

    @modification_type.setter
    def modification_type(self, modification_type):
        """Sets the modification_type of this ModifyUserCollection.

        The type of modification to perform.  If the type is delete or undelete, any other specified item details will be ignored  # noqa: E501

        :param modification_type: The modification_type of this ModifyUserCollection.  # noqa: E501
        :type modification_type: str
        """
        if self.local_vars_configuration.client_side_validation and modification_type is None:  # noqa: E501
            raise ValueError("Invalid value for `modification_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Modify", "Delete", "Undelete"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and modification_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `modification_type` ({0}), must be one of {1}"  # noqa: E501
                .format(modification_type, allowed_values)
            )

        self._modification_type = modification_type

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
        if not isinstance(other, ModifyUserCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyUserCollection):
            return True

        return self.to_dict() != other.to_dict()
