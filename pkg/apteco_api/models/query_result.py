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


class QueryResult(object):
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
        'notes': 'str',
        'ran_successfully': 'bool',
        'system_name': 'str',
        'system_load_date': 'datetime',
        'user_name': 'str',
        'run_date': 'datetime',
        'query_description': 'str',
        'counts': 'list[Count]',
        'messages': 'list[ServerMessage]',
        'query': 'Query'
    }

    attribute_map = {
        'title': 'title',
        'notes': 'notes',
        'ran_successfully': 'ranSuccessfully',
        'system_name': 'systemName',
        'system_load_date': 'systemLoadDate',
        'user_name': 'userName',
        'run_date': 'runDate',
        'query_description': 'queryDescription',
        'counts': 'counts',
        'messages': 'messages',
        'query': 'query'
    }

    def __init__(self, title=None, notes=None, ran_successfully=None, system_name=None, system_load_date=None, user_name=None, run_date=None, query_description=None, counts=None, messages=None, query=None, local_vars_configuration=None):  # noqa: E501
        """QueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._notes = None
        self._ran_successfully = None
        self._system_name = None
        self._system_load_date = None
        self._user_name = None
        self._run_date = None
        self._query_description = None
        self._counts = None
        self._messages = None
        self._query = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if notes is not None:
            self.notes = notes
        self.ran_successfully = ran_successfully
        if system_name is not None:
            self.system_name = system_name
        if system_load_date is not None:
            self.system_load_date = system_load_date
        if user_name is not None:
            self.user_name = user_name
        if run_date is not None:
            self.run_date = run_date
        if query_description is not None:
            self.query_description = query_description
        if counts is not None:
            self.counts = counts
        if messages is not None:
            self.messages = messages
        if query is not None:
            self.query = query

    @property
    def title(self):
        """Gets the title of this QueryResult.  # noqa: E501

        The title of the query that has been counted  # noqa: E501

        :return: The title of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this QueryResult.

        The title of the query that has been counted  # noqa: E501

        :param title: The title of this QueryResult.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def notes(self):
        """Gets the notes of this QueryResult.  # noqa: E501

        Any notes associated with the query that has been counted  # noqa: E501

        :return: The notes of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this QueryResult.

        Any notes associated with the query that has been counted  # noqa: E501

        :param notes: The notes of this QueryResult.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def ran_successfully(self):
        """Gets the ran_successfully of this QueryResult.  # noqa: E501

        Whether the query was counted successfully or not  # noqa: E501

        :return: The ran_successfully of this QueryResult.  # noqa: E501
        :rtype: bool
        """
        return self._ran_successfully

    @ran_successfully.setter
    def ran_successfully(self, ran_successfully):
        """Sets the ran_successfully of this QueryResult.

        Whether the query was counted successfully or not  # noqa: E501

        :param ran_successfully: The ran_successfully of this QueryResult.  # noqa: E501
        :type ran_successfully: bool
        """
        if self.local_vars_configuration.client_side_validation and ran_successfully is None:  # noqa: E501
            raise ValueError("Invalid value for `ran_successfully`, must not be `None`")  # noqa: E501

        self._ran_successfully = ran_successfully

    @property
    def system_name(self):
        """Gets the system_name of this QueryResult.  # noqa: E501

        The name of the FastStats system that this count has been produced by  # noqa: E501

        :return: The system_name of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this QueryResult.

        The name of the FastStats system that this count has been produced by  # noqa: E501

        :param system_name: The system_name of this QueryResult.  # noqa: E501
        :type system_name: str
        """

        self._system_name = system_name

    @property
    def system_load_date(self):
        """Gets the system_load_date of this QueryResult.  # noqa: E501

        The date and time that the FastStats system from which this count has come was last built  # noqa: E501

        :return: The system_load_date of this QueryResult.  # noqa: E501
        :rtype: datetime
        """
        return self._system_load_date

    @system_load_date.setter
    def system_load_date(self, system_load_date):
        """Sets the system_load_date of this QueryResult.

        The date and time that the FastStats system from which this count has come was last built  # noqa: E501

        :param system_load_date: The system_load_date of this QueryResult.  # noqa: E501
        :type system_load_date: datetime
        """

        self._system_load_date = system_load_date

    @property
    def user_name(self):
        """Gets the user_name of this QueryResult.  # noqa: E501

        The name of the user that requested this count  # noqa: E501

        :return: The user_name of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this QueryResult.

        The name of the user that requested this count  # noqa: E501

        :param user_name: The user_name of this QueryResult.  # noqa: E501
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def run_date(self):
        """Gets the run_date of this QueryResult.  # noqa: E501

        The date and time that this count was run on  # noqa: E501

        :return: The run_date of this QueryResult.  # noqa: E501
        :rtype: datetime
        """
        return self._run_date

    @run_date.setter
    def run_date(self, run_date):
        """Sets the run_date of this QueryResult.

        The date and time that this count was run on  # noqa: E501

        :param run_date: The run_date of this QueryResult.  # noqa: E501
        :type run_date: datetime
        """

        self._run_date = run_date

    @property
    def query_description(self):
        """Gets the query_description of this QueryResult.  # noqa: E501

        A textual description of the query that was counted  # noqa: E501

        :return: The query_description of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._query_description

    @query_description.setter
    def query_description(self, query_description):
        """Sets the query_description of this QueryResult.

        A textual description of the query that was counted  # noqa: E501

        :param query_description: The query_description of this QueryResult.  # noqa: E501
        :type query_description: str
        """

        self._query_description = query_description

    @property
    def counts(self):
        """Gets the counts of this QueryResult.  # noqa: E501

        A list of counts for each affected table in the FastStats system.  The first count in the list is the main one.  # noqa: E501

        :return: The counts of this QueryResult.  # noqa: E501
        :rtype: list[Count]
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this QueryResult.

        A list of counts for each affected table in the FastStats system.  The first count in the list is the main one.  # noqa: E501

        :param counts: The counts of this QueryResult.  # noqa: E501
        :type counts: list[Count]
        """

        self._counts = counts

    @property
    def messages(self):
        """Gets the messages of this QueryResult.  # noqa: E501

        A list of messages associated with this result  # noqa: E501

        :return: The messages of this QueryResult.  # noqa: E501
        :rtype: list[ServerMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this QueryResult.

        A list of messages associated with this result  # noqa: E501

        :param messages: The messages of this QueryResult.  # noqa: E501
        :type messages: list[ServerMessage]
        """

        self._messages = messages

    @property
    def query(self):
        """Gets the query of this QueryResult.  # noqa: E501


        :return: The query of this QueryResult.  # noqa: E501
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryResult.


        :param query: The query of this QueryResult.  # noqa: E501
        :type query: Query
        """

        self._query = query

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
        if not isinstance(other, QueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryResult):
            return True

        return self.to_dict() != other.to_dict()
