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
from apteco_api.models.age_rule import AgeRule  # noqa: E501
from apteco_api.rest import ApiException

class TestAgeRule(unittest.TestCase):
    """AgeRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AgeRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.age_rule.AgeRule()  # noqa: E501
        if include_optional :
            return AgeRule(
                range_low = 56, 
                range_high = 56, 
                units = 'Days', 
                relative_to = 'Actual', 
                reference_type = 'Today', 
                reference_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return AgeRule(
        )

    def testAgeRule(self):
        """Test AgeRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
