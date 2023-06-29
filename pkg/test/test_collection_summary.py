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
from apteco_api.models.collection_summary import CollectionSummary  # noqa: E501
from apteco_api.rest import ApiException

class TestCollectionSummary(unittest.TestCase):
    """CollectionSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CollectionSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.collection_summary.CollectionSummary()  # noqa: E501
        if include_optional :
            return CollectionSummary(
                id = 56, 
                title = '', 
                description = '', 
                creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                owner = apteco_api.models.user_display_details.UserDisplayDetails(
                    username = '', 
                    firstname = '', 
                    surname = '', 
                    email_address = '', ), 
                deletion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                number_of_parts = 56, 
                number_of_users_shared_with = 56, 
                share_id = 56, 
                number_of_hits = 56, 
                system_name = ''
            )
        else :
            return CollectionSummary(
                id = 56,
                title = '',
                description = '',
                creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                owner = apteco_api.models.user_display_details.UserDisplayDetails(
                    username = '', 
                    firstname = '', 
                    surname = '', 
                    email_address = '', ),
                deletion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                number_of_users_shared_with = 56,
                share_id = 56,
                number_of_hits = 56,
                system_name = '',
        )

    def testCollectionSummary(self):
        """Test CollectionSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
