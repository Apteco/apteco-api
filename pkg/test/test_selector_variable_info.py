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
from apteco_api.models.selector_variable_info import SelectorVariableInfo  # noqa: E501
from apteco_api.rest import ApiException

class TestSelectorVariableInfo(unittest.TestCase):
    """SelectorVariableInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SelectorVariableInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.selector_variable_info.SelectorVariableInfo()  # noqa: E501
        if include_optional :
            return SelectorVariableInfo(
                selector_type = 'SingleValue', 
                sub_type = 'Categorical', 
                var_code_order = 'Nominal', 
                number_of_codes = 56, 
                code_length = 56, 
                minimum_var_code_count = 56, 
                maximum_var_code_count = 56, 
                minimum_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                maximum_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                combined_from_variable_name = ''
            )
        else :
            return SelectorVariableInfo(
        )

    def testSelectorVariableInfo(self):
        """Test SelectorVariableInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
