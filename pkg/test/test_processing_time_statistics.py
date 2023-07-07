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
from apteco_api.models.processing_time_statistics import ProcessingTimeStatistics  # noqa: E501
from apteco_api.rest import ApiException

class TestProcessingTimeStatistics(unittest.TestCase):
    """ProcessingTimeStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProcessingTimeStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.processing_time_statistics.ProcessingTimeStatistics()  # noqa: E501
        if include_optional :
            return ProcessingTimeStatistics(
                categories = [
                    '0'
                    ], 
                frequencies = [
                    56
                    ], 
                minimum_durations_in_seconds = [
                    1.337
                    ], 
                maximum_durations_in_seconds = [
                    1.337
                    ], 
                mean_durations_in_seconds = [
                    1.337
                    ], 
                standard_deviation_of_durations_in_seconds = [
                    1.337
                    ], 
                median_durations_in_seconds = [
                    1.337
                    ], 
                percent75_durations_in_seconds = [
                    1.337
                    ], 
                percent90_durations_in_seconds = [
                    1.337
                    ], 
                percent95_durations_in_seconds = [
                    1.337
                    ], 
                percent99_durations_in_seconds = [
                    1.337
                    ]
            )
        else :
            return ProcessingTimeStatistics(
                categories = [
                    '0'
                    ],
                frequencies = [
                    56
                    ],
                minimum_durations_in_seconds = [
                    1.337
                    ],
                maximum_durations_in_seconds = [
                    1.337
                    ],
                mean_durations_in_seconds = [
                    1.337
                    ],
                standard_deviation_of_durations_in_seconds = [
                    1.337
                    ],
                median_durations_in_seconds = [
                    1.337
                    ],
                percent75_durations_in_seconds = [
                    1.337
                    ],
                percent90_durations_in_seconds = [
                    1.337
                    ],
                percent95_durations_in_seconds = [
                    1.337
                    ],
                percent99_durations_in_seconds = [
                    1.337
                    ],
        )

    def testProcessingTimeStatistics(self):
        """Test ProcessingTimeStatistics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()