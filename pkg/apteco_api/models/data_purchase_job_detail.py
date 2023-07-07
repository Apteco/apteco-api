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


class DataPurchaseJobDetail(object):
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
        'purchase_info': 'PurchaseInfo',
        'id': 'int',
        'is_complete': 'bool',
        'queue_position': 'int',
        'progress': 'int'
    }

    attribute_map = {
        'purchase_info': 'purchaseInfo',
        'id': 'id',
        'is_complete': 'isComplete',
        'queue_position': 'queuePosition',
        'progress': 'progress'
    }

    def __init__(self, purchase_info=None, id=None, is_complete=None, queue_position=None, progress=None, local_vars_configuration=None):  # noqa: E501
        """DataPurchaseJobDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._purchase_info = None
        self._id = None
        self._is_complete = None
        self._queue_position = None
        self._progress = None
        self.discriminator = None

        if purchase_info is not None:
            self.purchase_info = purchase_info
        self.id = id
        self.is_complete = is_complete
        if queue_position is not None:
            self.queue_position = queue_position
        if progress is not None:
            self.progress = progress

    @property
    def purchase_info(self):
        """Gets the purchase_info of this DataPurchaseJobDetail.  # noqa: E501


        :return: The purchase_info of this DataPurchaseJobDetail.  # noqa: E501
        :rtype: PurchaseInfo
        """
        return self._purchase_info

    @purchase_info.setter
    def purchase_info(self, purchase_info):
        """Sets the purchase_info of this DataPurchaseJobDetail.


        :param purchase_info: The purchase_info of this DataPurchaseJobDetail.  # noqa: E501
        :type: PurchaseInfo
        """

        self._purchase_info = purchase_info

    @property
    def id(self):
        """Gets the id of this DataPurchaseJobDetail.  # noqa: E501

        The job's id  # noqa: E501

        :return: The id of this DataPurchaseJobDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataPurchaseJobDetail.

        The job's id  # noqa: E501

        :param id: The id of this DataPurchaseJobDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_complete(self):
        """Gets the is_complete of this DataPurchaseJobDetail.  # noqa: E501

        Whether the job is complete or not  # noqa: E501

        :return: The is_complete of this DataPurchaseJobDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this DataPurchaseJobDetail.

        Whether the job is complete or not  # noqa: E501

        :param is_complete: The is_complete of this DataPurchaseJobDetail.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_complete is None:  # noqa: E501
            raise ValueError("Invalid value for `is_complete`, must not be `None`")  # noqa: E501

        self._is_complete = is_complete

    @property
    def queue_position(self):
        """Gets the queue_position of this DataPurchaseJobDetail.  # noqa: E501

        If present, the position that the job is in the job queue.  Jobs only start being actively processed once they reach the head of the queue  # noqa: E501

        :return: The queue_position of this DataPurchaseJobDetail.  # noqa: E501
        :rtype: int
        """
        return self._queue_position

    @queue_position.setter
    def queue_position(self, queue_position):
        """Sets the queue_position of this DataPurchaseJobDetail.

        If present, the position that the job is in the job queue.  Jobs only start being actively processed once they reach the head of the queue  # noqa: E501

        :param queue_position: The queue_position of this DataPurchaseJobDetail.  # noqa: E501
        :type: int
        """

        self._queue_position = queue_position

    @property
    def progress(self):
        """Gets the progress of this DataPurchaseJobDetail.  # noqa: E501

        If present, an estimate of how far through its processing this job is  # noqa: E501

        :return: The progress of this DataPurchaseJobDetail.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DataPurchaseJobDetail.

        If present, an estimate of how far through its processing this job is  # noqa: E501

        :param progress: The progress of this DataPurchaseJobDetail.  # noqa: E501
        :type: int
        """

        self._progress = progress

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
        if not isinstance(other, DataPurchaseJobDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataPurchaseJobDetail):
            return True

        return self.to_dict() != other.to_dict()