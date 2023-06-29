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


class AudienceResultDetail(object):
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
        'exclude_results': 'AudienceQueryResult',
        'include_results': 'AudienceQueryResult',
        'body_results': 'AudienceQueryResult',
        'id': 'int',
        'audience_update_id': 'int',
        'timestamp': 'datetime',
        'fast_stats_build_date': 'datetime',
        'user': 'UserDisplayDetails',
        'nett_results': 'AudienceQueryResult',
        'urn_file_path': 'str'
    }

    attribute_map = {
        'exclude_results': 'excludeResults',
        'include_results': 'includeResults',
        'body_results': 'bodyResults',
        'id': 'id',
        'audience_update_id': 'audienceUpdateId',
        'timestamp': 'timestamp',
        'fast_stats_build_date': 'fastStatsBuildDate',
        'user': 'user',
        'nett_results': 'nettResults',
        'urn_file_path': 'urnFilePath'
    }

    def __init__(self, exclude_results=None, include_results=None, body_results=None, id=None, audience_update_id=None, timestamp=None, fast_stats_build_date=None, user=None, nett_results=None, urn_file_path=None, local_vars_configuration=None):  # noqa: E501
        """AudienceResultDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._exclude_results = None
        self._include_results = None
        self._body_results = None
        self._id = None
        self._audience_update_id = None
        self._timestamp = None
        self._fast_stats_build_date = None
        self._user = None
        self._nett_results = None
        self._urn_file_path = None
        self.discriminator = None

        if exclude_results is not None:
            self.exclude_results = exclude_results
        if include_results is not None:
            self.include_results = include_results
        self.body_results = body_results
        self.id = id
        self.audience_update_id = audience_update_id
        self.timestamp = timestamp
        self.fast_stats_build_date = fast_stats_build_date
        self.user = user
        self.nett_results = nett_results
        self.urn_file_path = urn_file_path

    @property
    def exclude_results(self):
        """Gets the exclude_results of this AudienceResultDetail.  # noqa: E501


        :return: The exclude_results of this AudienceResultDetail.  # noqa: E501
        :rtype: AudienceQueryResult
        """
        return self._exclude_results

    @exclude_results.setter
    def exclude_results(self, exclude_results):
        """Sets the exclude_results of this AudienceResultDetail.


        :param exclude_results: The exclude_results of this AudienceResultDetail.  # noqa: E501
        :type exclude_results: AudienceQueryResult
        """

        self._exclude_results = exclude_results

    @property
    def include_results(self):
        """Gets the include_results of this AudienceResultDetail.  # noqa: E501


        :return: The include_results of this AudienceResultDetail.  # noqa: E501
        :rtype: AudienceQueryResult
        """
        return self._include_results

    @include_results.setter
    def include_results(self, include_results):
        """Sets the include_results of this AudienceResultDetail.


        :param include_results: The include_results of this AudienceResultDetail.  # noqa: E501
        :type include_results: AudienceQueryResult
        """

        self._include_results = include_results

    @property
    def body_results(self):
        """Gets the body_results of this AudienceResultDetail.  # noqa: E501


        :return: The body_results of this AudienceResultDetail.  # noqa: E501
        :rtype: AudienceQueryResult
        """
        return self._body_results

    @body_results.setter
    def body_results(self, body_results):
        """Sets the body_results of this AudienceResultDetail.


        :param body_results: The body_results of this AudienceResultDetail.  # noqa: E501
        :type body_results: AudienceQueryResult
        """
        if self.local_vars_configuration.client_side_validation and body_results is None:  # noqa: E501
            raise ValueError("Invalid value for `body_results`, must not be `None`")  # noqa: E501

        self._body_results = body_results

    @property
    def id(self):
        """Gets the id of this AudienceResultDetail.  # noqa: E501

        The id for this audience result  # noqa: E501

        :return: The id of this AudienceResultDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AudienceResultDetail.

        The id for this audience result  # noqa: E501

        :param id: The id of this AudienceResultDetail.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def audience_update_id(self):
        """Gets the audience_update_id of this AudienceResultDetail.  # noqa: E501

        The id of the update (audience version) that this audience result was calculated with  # noqa: E501

        :return: The audience_update_id of this AudienceResultDetail.  # noqa: E501
        :rtype: int
        """
        return self._audience_update_id

    @audience_update_id.setter
    def audience_update_id(self, audience_update_id):
        """Sets the audience_update_id of this AudienceResultDetail.

        The id of the update (audience version) that this audience result was calculated with  # noqa: E501

        :param audience_update_id: The audience_update_id of this AudienceResultDetail.  # noqa: E501
        :type audience_update_id: int
        """
        if self.local_vars_configuration.client_side_validation and audience_update_id is None:  # noqa: E501
            raise ValueError("Invalid value for `audience_update_id`, must not be `None`")  # noqa: E501

        self._audience_update_id = audience_update_id

    @property
    def timestamp(self):
        """Gets the timestamp of this AudienceResultDetail.  # noqa: E501

        The date and time that this audience result was calculated  # noqa: E501

        :return: The timestamp of this AudienceResultDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AudienceResultDetail.

        The date and time that this audience result was calculated  # noqa: E501

        :param timestamp: The timestamp of this AudienceResultDetail.  # noqa: E501
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def fast_stats_build_date(self):
        """Gets the fast_stats_build_date of this AudienceResultDetail.  # noqa: E501

        The date and time that the FastStats system used to calculate this audience result was built  # noqa: E501

        :return: The fast_stats_build_date of this AudienceResultDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._fast_stats_build_date

    @fast_stats_build_date.setter
    def fast_stats_build_date(self, fast_stats_build_date):
        """Sets the fast_stats_build_date of this AudienceResultDetail.

        The date and time that the FastStats system used to calculate this audience result was built  # noqa: E501

        :param fast_stats_build_date: The fast_stats_build_date of this AudienceResultDetail.  # noqa: E501
        :type fast_stats_build_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and fast_stats_build_date is None:  # noqa: E501
            raise ValueError("Invalid value for `fast_stats_build_date`, must not be `None`")  # noqa: E501

        self._fast_stats_build_date = fast_stats_build_date

    @property
    def user(self):
        """Gets the user of this AudienceResultDetail.  # noqa: E501


        :return: The user of this AudienceResultDetail.  # noqa: E501
        :rtype: UserDisplayDetails
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AudienceResultDetail.


        :param user: The user of this AudienceResultDetail.  # noqa: E501
        :type user: UserDisplayDetails
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def nett_results(self):
        """Gets the nett_results of this AudienceResultDetail.  # noqa: E501


        :return: The nett_results of this AudienceResultDetail.  # noqa: E501
        :rtype: AudienceQueryResult
        """
        return self._nett_results

    @nett_results.setter
    def nett_results(self, nett_results):
        """Sets the nett_results of this AudienceResultDetail.


        :param nett_results: The nett_results of this AudienceResultDetail.  # noqa: E501
        :type nett_results: AudienceQueryResult
        """
        if self.local_vars_configuration.client_side_validation and nett_results is None:  # noqa: E501
            raise ValueError("Invalid value for `nett_results`, must not be `None`")  # noqa: E501

        self._nett_results = nett_results

    @property
    def urn_file_path(self):
        """Gets the urn_file_path of this AudienceResultDetail.  # noqa: E501

        If a URN file was generated as part of this audience result then this will be its path within the FastStats system  # noqa: E501

        :return: The urn_file_path of this AudienceResultDetail.  # noqa: E501
        :rtype: str
        """
        return self._urn_file_path

    @urn_file_path.setter
    def urn_file_path(self, urn_file_path):
        """Sets the urn_file_path of this AudienceResultDetail.

        If a URN file was generated as part of this audience result then this will be its path within the FastStats system  # noqa: E501

        :param urn_file_path: The urn_file_path of this AudienceResultDetail.  # noqa: E501
        :type urn_file_path: str
        """
        if self.local_vars_configuration.client_side_validation and urn_file_path is None:  # noqa: E501
            raise ValueError("Invalid value for `urn_file_path`, must not be `None`")  # noqa: E501

        self._urn_file_path = urn_file_path

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
        if not isinstance(other, AudienceResultDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AudienceResultDetail):
            return True

        return self.to_dict() != other.to_dict()
