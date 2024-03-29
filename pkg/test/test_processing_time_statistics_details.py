# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import apteco_api
from apteco_api.models.processing_time_statistics_details import ProcessingTimeStatisticsDetails  # noqa: E501
from apteco_api.rest import ApiException

class TestProcessingTimeStatisticsDetails(unittest.TestCase):
    """ProcessingTimeStatisticsDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProcessingTimeStatisticsDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.processing_time_statistics_details.ProcessingTimeStatisticsDetails()  # noqa: E501
        if include_optional :
            return ProcessingTimeStatisticsDetails(
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                measure = 'ProcessingTime', 
                dimension = 'Years', 
                job_property_selection_type = 'AllJobs', 
                job_property_selections = [
                    '0'
                    ]
            )
        else :
            return ProcessingTimeStatisticsDetails(
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                measure = 'ProcessingTime',
                dimension = 'Years',
                job_property_selection_type = 'AllJobs',
                job_property_selections = [
                    '0'
                    ],
        )

    def testProcessingTimeStatisticsDetails(self):
        """Test ProcessingTimeStatisticsDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
