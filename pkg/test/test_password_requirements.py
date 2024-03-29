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
from apteco_api.models.password_requirements import PasswordRequirements  # noqa: E501
from apteco_api.rest import ApiException

class TestPasswordRequirements(unittest.TestCase):
    """PasswordRequirements unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PasswordRequirements
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.password_requirements.PasswordRequirements()  # noqa: E501
        if include_optional :
            return PasswordRequirements(
                minimum_password_length = 56, 
                minimum_number_of_digits_in_password = 56, 
                minimum_number_of_letters_in_password = 56, 
                minimum_number_of_lowercase_letters_in_password = 56, 
                minimum_number_of_uppercase_letters_in_password = 56, 
                minimum_number_of_symbols_in_password = 56
            )
        else :
            return PasswordRequirements(
                minimum_password_length = 56,
                minimum_number_of_digits_in_password = 56,
                minimum_number_of_letters_in_password = 56,
                minimum_number_of_lowercase_letters_in_password = 56,
                minimum_number_of_uppercase_letters_in_password = 56,
                minimum_number_of_symbols_in_password = 56,
        )

    def testPasswordRequirements(self):
        """Test PasswordRequirements"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
