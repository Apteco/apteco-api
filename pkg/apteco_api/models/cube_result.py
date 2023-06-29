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


class CubeResult(object):
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
        'dimension_results': 'list[DimensionResult]',
        'measure_results': 'list[MeasureResult]',
        'cube': 'Cube',
        'counts': 'list[Count]'
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
        'dimension_results': 'dimensionResults',
        'measure_results': 'measureResults',
        'cube': 'cube',
        'counts': 'counts'
    }

    def __init__(self, title=None, notes=None, ran_successfully=None, system_name=None, system_load_date=None, user_name=None, run_date=None, query_description=None, dimension_results=None, measure_results=None, cube=None, counts=None, local_vars_configuration=None):  # noqa: E501
        """CubeResult - a model defined in OpenAPI"""  # noqa: E501
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
        self._dimension_results = None
        self._measure_results = None
        self._cube = None
        self._counts = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if notes is not None:
            self.notes = notes
        if ran_successfully is not None:
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
        if dimension_results is not None:
            self.dimension_results = dimension_results
        if measure_results is not None:
            self.measure_results = measure_results
        if cube is not None:
            self.cube = cube
        if counts is not None:
            self.counts = counts

    @property
    def title(self):
        """Gets the title of this CubeResult.  # noqa: E501

        The title of the cube that has been calculated  # noqa: E501

        :return: The title of this CubeResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CubeResult.

        The title of the cube that has been calculated  # noqa: E501

        :param title: The title of this CubeResult.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def notes(self):
        """Gets the notes of this CubeResult.  # noqa: E501

        Any notes associated with the query that has been counted  # noqa: E501

        :return: The notes of this CubeResult.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CubeResult.

        Any notes associated with the query that has been counted  # noqa: E501

        :param notes: The notes of this CubeResult.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def ran_successfully(self):
        """Gets the ran_successfully of this CubeResult.  # noqa: E501

        Whether the query was counted successfully or not  # noqa: E501

        :return: The ran_successfully of this CubeResult.  # noqa: E501
        :rtype: bool
        """
        return self._ran_successfully

    @ran_successfully.setter
    def ran_successfully(self, ran_successfully):
        """Sets the ran_successfully of this CubeResult.

        Whether the query was counted successfully or not  # noqa: E501

        :param ran_successfully: The ran_successfully of this CubeResult.  # noqa: E501
        :type ran_successfully: bool
        """

        self._ran_successfully = ran_successfully

    @property
    def system_name(self):
        """Gets the system_name of this CubeResult.  # noqa: E501

        The name of the FastStats system that this count has been produced by  # noqa: E501

        :return: The system_name of this CubeResult.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this CubeResult.

        The name of the FastStats system that this count has been produced by  # noqa: E501

        :param system_name: The system_name of this CubeResult.  # noqa: E501
        :type system_name: str
        """

        self._system_name = system_name

    @property
    def system_load_date(self):
        """Gets the system_load_date of this CubeResult.  # noqa: E501

        The date and time that the FastStats system from which this count has come was last built  # noqa: E501

        :return: The system_load_date of this CubeResult.  # noqa: E501
        :rtype: datetime
        """
        return self._system_load_date

    @system_load_date.setter
    def system_load_date(self, system_load_date):
        """Sets the system_load_date of this CubeResult.

        The date and time that the FastStats system from which this count has come was last built  # noqa: E501

        :param system_load_date: The system_load_date of this CubeResult.  # noqa: E501
        :type system_load_date: datetime
        """

        self._system_load_date = system_load_date

    @property
    def user_name(self):
        """Gets the user_name of this CubeResult.  # noqa: E501

        The name of the user that requested this count  # noqa: E501

        :return: The user_name of this CubeResult.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CubeResult.

        The name of the user that requested this count  # noqa: E501

        :param user_name: The user_name of this CubeResult.  # noqa: E501
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def run_date(self):
        """Gets the run_date of this CubeResult.  # noqa: E501

        The date and time that this count was run on  # noqa: E501

        :return: The run_date of this CubeResult.  # noqa: E501
        :rtype: datetime
        """
        return self._run_date

    @run_date.setter
    def run_date(self, run_date):
        """Sets the run_date of this CubeResult.

        The date and time that this count was run on  # noqa: E501

        :param run_date: The run_date of this CubeResult.  # noqa: E501
        :type run_date: datetime
        """

        self._run_date = run_date

    @property
    def query_description(self):
        """Gets the query_description of this CubeResult.  # noqa: E501

        A textual description of the query that was counted  # noqa: E501

        :return: The query_description of this CubeResult.  # noqa: E501
        :rtype: str
        """
        return self._query_description

    @query_description.setter
    def query_description(self, query_description):
        """Sets the query_description of this CubeResult.

        A textual description of the query that was counted  # noqa: E501

        :param query_description: The query_description of this CubeResult.  # noqa: E501
        :type query_description: str
        """

        self._query_description = query_description

    @property
    def dimension_results(self):
        """Gets the dimension_results of this CubeResult.  # noqa: E501

        The set of dimension results for this cube, containing the category codes and descriptions for each dimension in the cube  # noqa: E501

        :return: The dimension_results of this CubeResult.  # noqa: E501
        :rtype: list[DimensionResult]
        """
        return self._dimension_results

    @dimension_results.setter
    def dimension_results(self, dimension_results):
        """Sets the dimension_results of this CubeResult.

        The set of dimension results for this cube, containing the category codes and descriptions for each dimension in the cube  # noqa: E501

        :param dimension_results: The dimension_results of this CubeResult.  # noqa: E501
        :type dimension_results: list[DimensionResult]
        """

        self._dimension_results = dimension_results

    @property
    def measure_results(self):
        """Gets the measure_results of this CubeResult.  # noqa: E501

        The set of measure results for this cube, containing the values for each measure in the cube  # noqa: E501

        :return: The measure_results of this CubeResult.  # noqa: E501
        :rtype: list[MeasureResult]
        """
        return self._measure_results

    @measure_results.setter
    def measure_results(self, measure_results):
        """Sets the measure_results of this CubeResult.

        The set of measure results for this cube, containing the values for each measure in the cube  # noqa: E501

        :param measure_results: The measure_results of this CubeResult.  # noqa: E501
        :type measure_results: list[MeasureResult]
        """

        self._measure_results = measure_results

    @property
    def cube(self):
        """Gets the cube of this CubeResult.  # noqa: E501


        :return: The cube of this CubeResult.  # noqa: E501
        :rtype: Cube
        """
        return self._cube

    @cube.setter
    def cube(self, cube):
        """Sets the cube of this CubeResult.


        :param cube: The cube of this CubeResult.  # noqa: E501
        :type cube: Cube
        """

        self._cube = cube

    @property
    def counts(self):
        """Gets the counts of this CubeResult.  # noqa: E501

        A list of counts for each affected table in the FastStats system.  The first count in the list is the main one.  # noqa: E501

        :return: The counts of this CubeResult.  # noqa: E501
        :rtype: list[Count]
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this CubeResult.

        A list of counts for each affected table in the FastStats system.  The first count in the list is the main one.  # noqa: E501

        :param counts: The counts of this CubeResult.  # noqa: E501
        :type counts: list[Count]
        """

        self._counts = counts

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
        if not isinstance(other, CubeResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CubeResult):
            return True

        return self.to_dict() != other.to_dict()
