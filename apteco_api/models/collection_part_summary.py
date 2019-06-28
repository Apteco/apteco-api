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


class CollectionPartSummary(object):
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
        'index': 'int',
        'visualisation_type': 'str',
        'visualisation_id': 'str'
    }

    attribute_map = {
        'title': 'title',
        'index': 'index',
        'visualisation_type': 'visualisationType',
        'visualisation_id': 'visualisationId'
    }

    def __init__(self, title=None, index=None, visualisation_type=None, visualisation_id=None):  # noqa: E501
        """CollectionPartSummary - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._index = None
        self._visualisation_type = None
        self._visualisation_id = None
        self.discriminator = None

        self.title = title
        self.index = index
        self.visualisation_type = visualisation_type
        self.visualisation_id = visualisation_id

    @property
    def title(self):
        """Gets the title of this CollectionPartSummary.  # noqa: E501

        The collection part's title  # noqa: E501

        :return: The title of this CollectionPartSummary.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CollectionPartSummary.

        The collection part's title  # noqa: E501

        :param title: The title of this CollectionPartSummary.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def index(self):
        """Gets the index of this CollectionPartSummary.  # noqa: E501

        The part's index within the collection  # noqa: E501

        :return: The index of this CollectionPartSummary.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this CollectionPartSummary.

        The part's index within the collection  # noqa: E501

        :param index: The index of this CollectionPartSummary.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def visualisation_type(self):
        """Gets the visualisation_type of this CollectionPartSummary.  # noqa: E501

        The collection part's visualisation type  # noqa: E501

        :return: The visualisation_type of this CollectionPartSummary.  # noqa: E501
        :rtype: str
        """
        return self._visualisation_type

    @visualisation_type.setter
    def visualisation_type(self, visualisation_type):
        """Sets the visualisation_type of this CollectionPartSummary.

        The collection part's visualisation type  # noqa: E501

        :param visualisation_type: The visualisation_type of this CollectionPartSummary.  # noqa: E501
        :type: str
        """
        if visualisation_type is None:
            raise ValueError("Invalid value for `visualisation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Cube", "Venn", "Chart", "DataGrid"]  # noqa: E501
        if visualisation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `visualisation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(visualisation_type, allowed_values)
            )

        self._visualisation_type = visualisation_type

    @property
    def visualisation_id(self):
        """Gets the visualisation_id of this CollectionPartSummary.  # noqa: E501

        The id of the visualisation for this part  # noqa: E501

        :return: The visualisation_id of this CollectionPartSummary.  # noqa: E501
        :rtype: str
        """
        return self._visualisation_id

    @visualisation_id.setter
    def visualisation_id(self, visualisation_id):
        """Sets the visualisation_id of this CollectionPartSummary.

        The id of the visualisation for this part  # noqa: E501

        :param visualisation_id: The visualisation_id of this CollectionPartSummary.  # noqa: E501
        :type: str
        """
        if visualisation_id is None:
            raise ValueError("Invalid value for `visualisation_id`, must not be `None`")  # noqa: E501

        self._visualisation_id = visualisation_id

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
        if not isinstance(other, CollectionPartSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
