# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from apteco_api.configuration import Configuration


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

    def __init__(self, title=None, index=None, visualisation_type=None, visualisation_id=None, local_vars_configuration=None):  # noqa: E501
        """CollectionPartSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

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
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
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
        :type index: int
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
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
        :type visualisation_type: str
        """
        if self.local_vars_configuration.client_side_validation and visualisation_type is None:  # noqa: E501
            raise ValueError("Invalid value for `visualisation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Cube", "Venn", "Chart", "DataGrid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visualisation_type not in allowed_values:  # noqa: E501
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
        :type visualisation_id: str
        """
        if self.local_vars_configuration.client_side_validation and visualisation_id is None:  # noqa: E501
            raise ValueError("Invalid value for `visualisation_id`, must not be `None`")  # noqa: E501

        self._visualisation_id = visualisation_id

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
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
        if not isinstance(other, CollectionPartSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionPartSummary):
            return True

        return self.to_dict() != other.to_dict()
