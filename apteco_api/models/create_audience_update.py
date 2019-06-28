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


class CreateAudienceUpdate(object):
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
        'title': 'str',
        'description': 'str',
        'is_deleted': 'bool',
        'exclude_query': 'Query',
        'include_query': 'Query',
        'body_query': 'Query',
        'selection_modifiers': 'SelectionModifiers',
        'brief_text': 'str'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'is_deleted': 'isDeleted',
        'exclude_query': 'excludeQuery',
        'include_query': 'includeQuery',
        'body_query': 'bodyQuery',
        'selection_modifiers': 'selectionModifiers',
        'brief_text': 'briefText'
    }

    def __init__(self, title=None, description=None, is_deleted=None, exclude_query=None, include_query=None, body_query=None, selection_modifiers=None, brief_text=None):  # noqa: E501
        """CreateAudienceUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._description = None
        self._is_deleted = None
        self._exclude_query = None
        self._include_query = None
        self._body_query = None
        self._selection_modifiers = None
        self._brief_text = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if exclude_query is not None:
            self.exclude_query = exclude_query
        if include_query is not None:
            self.include_query = include_query
        if body_query is not None:
            self.body_query = body_query
        if selection_modifiers is not None:
            self.selection_modifiers = selection_modifiers
        if brief_text is not None:
            self.brief_text = brief_text

    @property
    def title(self):
        """Gets the title of this CreateAudienceUpdate.  # noqa: E501

        The title of the audience  # noqa: E501

        :return: The title of this CreateAudienceUpdate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateAudienceUpdate.

        The title of the audience  # noqa: E501

        :param title: The title of this CreateAudienceUpdate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this CreateAudienceUpdate.  # noqa: E501

        The description of the audience  # noqa: E501

        :return: The description of this CreateAudienceUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAudienceUpdate.

        The description of the audience  # noqa: E501

        :param description: The description of this CreateAudienceUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_deleted(self):
        """Gets the is_deleted of this CreateAudienceUpdate.  # noqa: E501

        Whether this audience should be deleted or not  # noqa: E501

        :return: The is_deleted of this CreateAudienceUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this CreateAudienceUpdate.

        Whether this audience should be deleted or not  # noqa: E501

        :param is_deleted: The is_deleted of this CreateAudienceUpdate.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def exclude_query(self):
        """Gets the exclude_query of this CreateAudienceUpdate.  # noqa: E501


        :return: The exclude_query of this CreateAudienceUpdate.  # noqa: E501
        :rtype: Query
        """
        return self._exclude_query

    @exclude_query.setter
    def exclude_query(self, exclude_query):
        """Sets the exclude_query of this CreateAudienceUpdate.


        :param exclude_query: The exclude_query of this CreateAudienceUpdate.  # noqa: E501
        :type: Query
        """

        self._exclude_query = exclude_query

    @property
    def include_query(self):
        """Gets the include_query of this CreateAudienceUpdate.  # noqa: E501


        :return: The include_query of this CreateAudienceUpdate.  # noqa: E501
        :rtype: Query
        """
        return self._include_query

    @include_query.setter
    def include_query(self, include_query):
        """Sets the include_query of this CreateAudienceUpdate.


        :param include_query: The include_query of this CreateAudienceUpdate.  # noqa: E501
        :type: Query
        """

        self._include_query = include_query

    @property
    def body_query(self):
        """Gets the body_query of this CreateAudienceUpdate.  # noqa: E501


        :return: The body_query of this CreateAudienceUpdate.  # noqa: E501
        :rtype: Query
        """
        return self._body_query

    @body_query.setter
    def body_query(self, body_query):
        """Sets the body_query of this CreateAudienceUpdate.


        :param body_query: The body_query of this CreateAudienceUpdate.  # noqa: E501
        :type: Query
        """

        self._body_query = body_query

    @property
    def selection_modifiers(self):
        """Gets the selection_modifiers of this CreateAudienceUpdate.  # noqa: E501


        :return: The selection_modifiers of this CreateAudienceUpdate.  # noqa: E501
        :rtype: SelectionModifiers
        """
        return self._selection_modifiers

    @selection_modifiers.setter
    def selection_modifiers(self, selection_modifiers):
        """Sets the selection_modifiers of this CreateAudienceUpdate.


        :param selection_modifiers: The selection_modifiers of this CreateAudienceUpdate.  # noqa: E501
        :type: SelectionModifiers
        """

        self._selection_modifiers = selection_modifiers

    @property
    def brief_text(self):
        """Gets the brief_text of this CreateAudienceUpdate.  # noqa: E501

        Notes associated with the audience  # noqa: E501

        :return: The brief_text of this CreateAudienceUpdate.  # noqa: E501
        :rtype: str
        """
        return self._brief_text

    @brief_text.setter
    def brief_text(self, brief_text):
        """Sets the brief_text of this CreateAudienceUpdate.

        Notes associated with the audience  # noqa: E501

        :param brief_text: The brief_text of this CreateAudienceUpdate.  # noqa: E501
        :type: str
        """

        self._brief_text = brief_text

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
        if not isinstance(other, CreateAudienceUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
