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
from apteco_api.models.user_audience_composition_summary import UserAudienceCompositionSummary  # noqa: E501
from apteco_api.rest import ApiException

class TestUserAudienceCompositionSummary(unittest.TestCase):
    """UserAudienceCompositionSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserAudienceCompositionSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.user_audience_composition_summary.UserAudienceCompositionSummary()  # noqa: E501
        if include_optional :
            return UserAudienceCompositionSummary(
                viewing_username = '0', 
                shared_to_me = True, 
                shared_by_me = True, 
                id = 56, 
                description = '0', 
                type = 'Check', 
                system_name = '0', 
                owner = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', ), 
                number_of_users_shared_with = 56, 
                shared_to_all = True, 
                share_id = 56
            )
        else :
            return UserAudienceCompositionSummary(
                viewing_username = '0',
                shared_to_me = True,
                shared_by_me = True,
                id = 56,
                description = '0',
                type = 'Check',
                system_name = '0',
                owner = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', ),
                number_of_users_shared_with = 56,
                shared_to_all = True,
        )

    def testUserAudienceCompositionSummary(self):
        """Test UserAudienceCompositionSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()