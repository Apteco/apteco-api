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
from apteco_api.models.create_share_detail import CreateShareDetail  # noqa: E501
from apteco_api.rest import ApiException

class TestCreateShareDetail(unittest.TestCase):
    """CreateShareDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateShareDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.create_share_detail.CreateShareDetail()  # noqa: E501
        if include_optional :
            return CreateShareDetail(
                shareable_type = 'Collection', 
                shareable_id = 56, 
                email_addresses_to_add = [
                    '0'
                    ], 
                user_ids_to_add = [
                    56
                    ], 
                group_ids_to_add = [
                    56
                    ], 
                share_to_all = True, 
                notify_added_recipients = True, 
                added_recipient_notification_message = '0', 
                notes = '0', 
                view_shareable_url = '0'
            )
        else :
            return CreateShareDetail(
                shareable_type = 'Collection',
                shareable_id = 56,
                email_addresses_to_add = [
                    '0'
                    ],
                user_ids_to_add = [
                    56
                    ],
                group_ids_to_add = [
                    56
                    ],
                notify_added_recipients = True,
        )

    def testCreateShareDetail(self):
        """Test CreateShareDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()