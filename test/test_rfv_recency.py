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
from apteco_api.models.rfv_recency import RFVRecency  # noqa: E501
from apteco_api.rest import ApiException

class TestRFVRecency(unittest.TestCase):
    """RFVRecency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RFVRecency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.rfv_recency.RFVRecency()  # noqa: E501
        if include_optional :
            return RFVRecency(
                variable_name = '0', 
                sequence = '0', 
                direction = 'Any', 
                value = 56, 
                distinct = True
            )
        else :
            return RFVRecency(
        )

    def testRFVRecency(self):
        """Test RFVRecency"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
