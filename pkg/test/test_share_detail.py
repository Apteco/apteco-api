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
from apteco_api.models.share_detail import ShareDetail  # noqa: E501
from apteco_api.rest import ApiException

class TestShareDetail(unittest.TestCase):
    """ShareDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ShareDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.share_detail.ShareDetail()  # noqa: E501
        if include_optional :
            return ShareDetail(
                id = 56, 
                shareable_type = 'Unknown', 
                shareable_id = 56, 
                shareable_title = '0', 
                number_of_users_shared_with = 56, 
                shared_to_all = True, 
                view_shareable_url = '0'
            )
        else :
            return ShareDetail(
                id = 56,
                shareable_type = 'Unknown',
                shareable_id = 56,
                shareable_title = '0',
                number_of_users_shared_with = 56,
                shared_to_all = True,
                view_shareable_url = '0',
        )

    def testShareDetail(self):
        """Test ShareDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
