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


class DataPurchaseDetail(object):
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
        'query_id': 'str',
        'licensing_set': 'str',
        'filename': 'str',
        'grand_total_cost': 'float',
        'purchase_order_number': 'str',
        'password': 'str',
        'authorisation_code': 'str'
    }

    attribute_map = {
        'query_id': 'queryId',
        'licensing_set': 'licensingSet',
        'filename': 'filename',
        'grand_total_cost': 'grandTotalCost',
        'purchase_order_number': 'purchaseOrderNumber',
        'password': 'password',
        'authorisation_code': 'authorisationCode'
    }

    def __init__(self, query_id=None, licensing_set=None, filename=None, grand_total_cost=None, purchase_order_number=None, password=None, authorisation_code=None, local_vars_configuration=None):  # noqa: E501
        """DataPurchaseDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query_id = None
        self._licensing_set = None
        self._filename = None
        self._grand_total_cost = None
        self._purchase_order_number = None
        self._password = None
        self._authorisation_code = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if licensing_set is not None:
            self.licensing_set = licensing_set
        if filename is not None:
            self.filename = filename
        if grand_total_cost is not None:
            self.grand_total_cost = grand_total_cost
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if password is not None:
            self.password = password
        if authorisation_code is not None:
            self.authorisation_code = authorisation_code

    @property
    def query_id(self):
        """Gets the query_id of this DataPurchaseDetail.  # noqa: E501

        The unique id of the data licensing query to purchase records for  # noqa: E501

        :return: The query_id of this DataPurchaseDetail.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this DataPurchaseDetail.

        The unique id of the data licensing query to purchase records for  # noqa: E501

        :param query_id: The query_id of this DataPurchaseDetail.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def licensing_set(self):
        """Gets the licensing_set of this DataPurchaseDetail.  # noqa: E501

        The name of the licensing set to purchase records for  # noqa: E501

        :return: The licensing_set of this DataPurchaseDetail.  # noqa: E501
        :rtype: str
        """
        return self._licensing_set

    @licensing_set.setter
    def licensing_set(self, licensing_set):
        """Sets the licensing_set of this DataPurchaseDetail.

        The name of the licensing set to purchase records for  # noqa: E501

        :param licensing_set: The licensing_set of this DataPurchaseDetail.  # noqa: E501
        :type: str
        """

        self._licensing_set = licensing_set

    @property
    def filename(self):
        """Gets the filename of this DataPurchaseDetail.  # noqa: E501

        The name of the file saved to the user's private directory  # noqa: E501

        :return: The filename of this DataPurchaseDetail.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this DataPurchaseDetail.

        The name of the file saved to the user's private directory  # noqa: E501

        :param filename: The filename of this DataPurchaseDetail.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def grand_total_cost(self):
        """Gets the grand_total_cost of this DataPurchaseDetail.  # noqa: E501

        The total cost to license the records  # noqa: E501

        :return: The grand_total_cost of this DataPurchaseDetail.  # noqa: E501
        :rtype: float
        """
        return self._grand_total_cost

    @grand_total_cost.setter
    def grand_total_cost(self, grand_total_cost):
        """Sets the grand_total_cost of this DataPurchaseDetail.

        The total cost to license the records  # noqa: E501

        :param grand_total_cost: The grand_total_cost of this DataPurchaseDetail.  # noqa: E501
        :type: float
        """

        self._grand_total_cost = grand_total_cost

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this DataPurchaseDetail.  # noqa: E501

        The order number for this purchase of records  # noqa: E501

        :return: The purchase_order_number of this DataPurchaseDetail.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this DataPurchaseDetail.

        The order number for this purchase of records  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this DataPurchaseDetail.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def password(self):
        """Gets the password of this DataPurchaseDetail.  # noqa: E501

        String of characters to authorise purchase  # noqa: E501

        :return: The password of this DataPurchaseDetail.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DataPurchaseDetail.

        String of characters to authorise purchase  # noqa: E501

        :param password: The password of this DataPurchaseDetail.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def authorisation_code(self):
        """Gets the authorisation_code of this DataPurchaseDetail.  # noqa: E501

        Authorisation code to purchase records over velocity limit  # noqa: E501

        :return: The authorisation_code of this DataPurchaseDetail.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, authorisation_code):
        """Sets the authorisation_code of this DataPurchaseDetail.

        Authorisation code to purchase records over velocity limit  # noqa: E501

        :param authorisation_code: The authorisation_code of this DataPurchaseDetail.  # noqa: E501
        :type: str
        """

        self._authorisation_code = authorisation_code

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
        if not isinstance(other, DataPurchaseDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataPurchaseDetail):
            return True

        return self.to_dict() != other.to_dict()
