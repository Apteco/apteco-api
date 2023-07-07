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
from apteco_api.models.collection_hit_detail import CollectionHitDetail  # noqa: E501
from apteco_api.rest import ApiException

class TestCollectionHitDetail(unittest.TestCase):
    """CollectionHitDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CollectionHitDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.collection_hit_detail.CollectionHitDetail()  # noqa: E501
        if include_optional :
            return CollectionHitDetail(
                user_agent_details = '0', 
                id = 56, 
                collection_id = 56, 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', )
            )
        else :
            return CollectionHitDetail(
                id = 56,
                collection_id = 56,
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', ),
        )

    def testCollectionHitDetail(self):
        """Test CollectionHitDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()