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
from apteco_api.models.update_team_details import UpdateTeamDetails  # noqa: E501
from apteco_api.rest import ApiException

class TestUpdateTeamDetails(unittest.TestCase):
    """UpdateTeamDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateTeamDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.update_team_details.UpdateTeamDetails()  # noqa: E501
        if include_optional :
            return UpdateTeamDetails(
                name = '0'
            )
        else :
            return UpdateTeamDetails(
        )

    def testUpdateTeamDetails(self):
        """Test UpdateTeamDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
