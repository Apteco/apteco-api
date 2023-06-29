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
from apteco_api.models.created_share_update_detail import CreatedShareUpdateDetail  # noqa: E501
from apteco_api.rest import ApiException

class TestCreatedShareUpdateDetail(unittest.TestCase):
    """CreatedShareUpdateDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreatedShareUpdateDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.created_share_update_detail.CreatedShareUpdateDetail()  # noqa: E501
        if include_optional :
            return CreatedShareUpdateDetail(
                share_update = apteco_api.models.share_update.ShareUpdate(
                    id = 56, 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', ), 
                    notes = '', 
                    number_of_added_users = 56, 
                    first_added_user = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', ), 
                    number_of_removed_users = 56, 
                    first_removed_user = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', ), ), 
                invalid_users_to_add = [
                    apteco_api.models.invalid_to_share_user_display_details.InvalidToShareUserDisplayDetails(
                        reason = 'ShareableAlreadySharedToUser', 
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', )
                    ], 
                invalid_users_to_remove = [
                    apteco_api.models.invalid_to_share_user_display_details.InvalidToShareUserDisplayDetails(
                        reason = 'ShareableAlreadySharedToUser', 
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', )
                    ]
            )
        else :
            return CreatedShareUpdateDetail(
                share_update = apteco_api.models.share_update.ShareUpdate(
                    id = 56, 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', ), 
                    notes = '', 
                    number_of_added_users = 56, 
                    first_added_user = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', ), 
                    number_of_removed_users = 56, 
                    first_removed_user = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', ), ),
                invalid_users_to_add = [
                    apteco_api.models.invalid_to_share_user_display_details.InvalidToShareUserDisplayDetails(
                        reason = 'ShareableAlreadySharedToUser', 
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', )
                    ],
                invalid_users_to_remove = [
                    apteco_api.models.invalid_to_share_user_display_details.InvalidToShareUserDisplayDetails(
                        reason = 'ShareableAlreadySharedToUser', 
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', )
                    ],
        )

    def testCreatedShareUpdateDetail(self):
        """Test CreatedShareUpdateDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
