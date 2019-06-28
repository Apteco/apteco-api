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


class PeopleStageSystemDetail(object):
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
        'metadata': 'DiagramMetadata',
        'last_requested_data_at': 'datetime',
        'system_name': 'str',
        'diagram_id': 'str',
        'programme_id': 'str',
        'programme_description': 'str',
        'is_able_to_provide_statistics': 'bool'
    }

    attribute_map = {
        'metadata': 'metadata',
        'last_requested_data_at': 'lastRequestedDataAt',
        'system_name': 'systemName',
        'diagram_id': 'diagramId',
        'programme_id': 'programmeId',
        'programme_description': 'programmeDescription',
        'is_able_to_provide_statistics': 'isAbleToProvideStatistics'
    }

    def __init__(self, metadata=None, last_requested_data_at=None, system_name=None, diagram_id=None, programme_id=None, programme_description=None, is_able_to_provide_statistics=None):  # noqa: E501
        """PeopleStageSystemDetail - a model defined in OpenAPI"""  # noqa: E501

        self._metadata = None
        self._last_requested_data_at = None
        self._system_name = None
        self._diagram_id = None
        self._programme_id = None
        self._programme_description = None
        self._is_able_to_provide_statistics = None
        self.discriminator = None

        self.metadata = metadata
        if last_requested_data_at is not None:
            self.last_requested_data_at = last_requested_data_at
        self.system_name = system_name
        self.diagram_id = diagram_id
        self.programme_id = programme_id
        self.programme_description = programme_description
        self.is_able_to_provide_statistics = is_able_to_provide_statistics

    @property
    def metadata(self):
        """Gets the metadata of this PeopleStageSystemDetail.  # noqa: E501


        :return: The metadata of this PeopleStageSystemDetail.  # noqa: E501
        :rtype: DiagramMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PeopleStageSystemDetail.


        :param metadata: The metadata of this PeopleStageSystemDetail.  # noqa: E501
        :type: DiagramMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def last_requested_data_at(self):
        """Gets the last_requested_data_at of this PeopleStageSystemDetail.  # noqa: E501

        The date and time that the API last polled for PeopleStage data  # noqa: E501

        :return: The last_requested_data_at of this PeopleStageSystemDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_requested_data_at

    @last_requested_data_at.setter
    def last_requested_data_at(self, last_requested_data_at):
        """Sets the last_requested_data_at of this PeopleStageSystemDetail.

        The date and time that the API last polled for PeopleStage data  # noqa: E501

        :param last_requested_data_at: The last_requested_data_at of this PeopleStageSystemDetail.  # noqa: E501
        :type: datetime
        """

        self._last_requested_data_at = last_requested_data_at

    @property
    def system_name(self):
        """Gets the system_name of this PeopleStageSystemDetail.  # noqa: E501

        The name of the system that has PeopleStage configured  # noqa: E501

        :return: The system_name of this PeopleStageSystemDetail.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this PeopleStageSystemDetail.

        The name of the system that has PeopleStage configured  # noqa: E501

        :param system_name: The system_name of this PeopleStageSystemDetail.  # noqa: E501
        :type: str
        """
        if system_name is None:
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501

        self._system_name = system_name

    @property
    def diagram_id(self):
        """Gets the diagram_id of this PeopleStageSystemDetail.  # noqa: E501

        The top-level diagram id for this PeopleStage system  # noqa: E501

        :return: The diagram_id of this PeopleStageSystemDetail.  # noqa: E501
        :rtype: str
        """
        return self._diagram_id

    @diagram_id.setter
    def diagram_id(self, diagram_id):
        """Sets the diagram_id of this PeopleStageSystemDetail.

        The top-level diagram id for this PeopleStage system  # noqa: E501

        :param diagram_id: The diagram_id of this PeopleStageSystemDetail.  # noqa: E501
        :type: str
        """
        if diagram_id is None:
            raise ValueError("Invalid value for `diagram_id`, must not be `None`")  # noqa: E501

        self._diagram_id = diagram_id

    @property
    def programme_id(self):
        """Gets the programme_id of this PeopleStageSystemDetail.  # noqa: E501

        The id of the first programme configured within the PeopleStage diagram  # noqa: E501

        :return: The programme_id of this PeopleStageSystemDetail.  # noqa: E501
        :rtype: str
        """
        return self._programme_id

    @programme_id.setter
    def programme_id(self, programme_id):
        """Sets the programme_id of this PeopleStageSystemDetail.

        The id of the first programme configured within the PeopleStage diagram  # noqa: E501

        :param programme_id: The programme_id of this PeopleStageSystemDetail.  # noqa: E501
        :type: str
        """
        if programme_id is None:
            raise ValueError("Invalid value for `programme_id`, must not be `None`")  # noqa: E501

        self._programme_id = programme_id

    @property
    def programme_description(self):
        """Gets the programme_description of this PeopleStageSystemDetail.  # noqa: E501

        The description of the first programme configured within the PeopleStage diagram  # noqa: E501

        :return: The programme_description of this PeopleStageSystemDetail.  # noqa: E501
        :rtype: str
        """
        return self._programme_description

    @programme_description.setter
    def programme_description(self, programme_description):
        """Sets the programme_description of this PeopleStageSystemDetail.

        The description of the first programme configured within the PeopleStage diagram  # noqa: E501

        :param programme_description: The programme_description of this PeopleStageSystemDetail.  # noqa: E501
        :type: str
        """
        if programme_description is None:
            raise ValueError("Invalid value for `programme_description`, must not be `None`")  # noqa: E501

        self._programme_description = programme_description

    @property
    def is_able_to_provide_statistics(self):
        """Gets the is_able_to_provide_statistics of this PeopleStageSystemDetail.  # noqa: E501

        Whether statistics information can be gathered for this PeopleStage system  # noqa: E501

        :return: The is_able_to_provide_statistics of this PeopleStageSystemDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_able_to_provide_statistics

    @is_able_to_provide_statistics.setter
    def is_able_to_provide_statistics(self, is_able_to_provide_statistics):
        """Sets the is_able_to_provide_statistics of this PeopleStageSystemDetail.

        Whether statistics information can be gathered for this PeopleStage system  # noqa: E501

        :param is_able_to_provide_statistics: The is_able_to_provide_statistics of this PeopleStageSystemDetail.  # noqa: E501
        :type: bool
        """
        if is_able_to_provide_statistics is None:
            raise ValueError("Invalid value for `is_able_to_provide_statistics`, must not be `None`")  # noqa: E501

        self._is_able_to_provide_statistics = is_able_to_provide_statistics

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
        if not isinstance(other, PeopleStageSystemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
