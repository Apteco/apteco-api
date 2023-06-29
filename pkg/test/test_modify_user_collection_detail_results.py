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
from apteco_api.models.modify_user_collection_detail_results import ModifyUserCollectionDetailResults  # noqa: E501
from apteco_api.rest import ApiException

class TestModifyUserCollectionDetailResults(unittest.TestCase):
    """ModifyUserCollectionDetailResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModifyUserCollectionDetailResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.modify_user_collection_detail_results.ModifyUserCollectionDetailResults()  # noqa: E501
        if include_optional :
            return ModifyUserCollectionDetailResults(
                collection = apteco_api.models.user_collection_detail.UserCollectionDetail(
                    viewing_username = '', 
                    status = 'Default', 
                    shared_to_me = True, 
                    shared_by_me = True, 
                    id = 56, 
                    owner = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '', 
                        firstname = '', 
                        surname = '', 
                        email_address = '', ), 
                    number_of_parts = 56, 
                    number_of_users_shared_with = 56, 
                    share_id = 56, 
                    number_of_hits = 56, 
                    system_name = '', 
                    title = '', 
                    description = '', 
                    creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    file_path = '', 
                    deletion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                id = 56, 
                succeeded = True, 
                status = '', 
                status_code = 56
            )
        else :
            return ModifyUserCollectionDetailResults(
                id = 56,
                succeeded = True,
                status = '',
                status_code = 56,
        )

    def testModifyUserCollectionDetailResults(self):
        """Test ModifyUserCollectionDetailResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
