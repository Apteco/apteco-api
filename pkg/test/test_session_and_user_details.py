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
from apteco_api.models.session_and_user_details import SessionAndUserDetails  # noqa: E501
from apteco_api.rest import ApiException

class TestSessionAndUserDetails(unittest.TestCase):
    """SessionAndUserDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SessionAndUserDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.session_and_user_details.SessionAndUserDetails()  # noqa: E501
        if include_optional :
            return SessionAndUserDetails(
                user = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', ), 
                session_id = '0'
            )
        else :
            return SessionAndUserDetails(
                user = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', ),
                session_id = '0',
        )

    def testSessionAndUserDetails(self):
        """Test SessionAndUserDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
