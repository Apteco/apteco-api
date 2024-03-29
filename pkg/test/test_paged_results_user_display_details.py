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
from apteco_api.models.paged_results_user_display_details import PagedResultsUserDisplayDetails  # noqa: E501
from apteco_api.rest import ApiException

class TestPagedResultsUserDisplayDetails(unittest.TestCase):
    """PagedResultsUserDisplayDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResultsUserDisplayDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.paged_results_user_display_details.PagedResultsUserDisplayDetails()  # noqa: E501
        if include_optional :
            return PagedResultsUserDisplayDetails(
                offset = 56, 
                count = 56, 
                total_count = 56, 
                list = [
                    apteco_api.models.user_display_details.UserDisplayDetails(
                        id = 56, 
                        username = '0', 
                        firstname = '0', 
                        surname = '0', 
                        email_address = '0', )
                    ]
            )
        else :
            return PagedResultsUserDisplayDetails(
                offset = 56,
                count = 56,
                total_count = 56,
                list = [
                    apteco_api.models.user_display_details.UserDisplayDetails(
                        id = 56, 
                        username = '0', 
                        firstname = '0', 
                        surname = '0', 
                        email_address = '0', )
                    ],
        )

    def testPagedResultsUserDisplayDetails(self):
        """Test PagedResultsUserDisplayDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
