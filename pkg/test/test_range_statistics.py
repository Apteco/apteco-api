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
from apteco_api.models.range_statistics import RangeStatistics  # noqa: E501
from apteco_api.rest import ApiException

class TestRangeStatistics(unittest.TestCase):
    """RangeStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RangeStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.range_statistics.RangeStatistics()  # noqa: E501
        if include_optional :
            return RangeStatistics(
                id = '0', 
                communications_count = 56, 
                deliveries_count = 56, 
                messages_count = 56, 
                campaigns_count = 56, 
                first_ran = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_ran = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                statistics_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return RangeStatistics(
                id = '0',
        )

    def testRangeStatistics(self):
        """Test RangeStatistics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()