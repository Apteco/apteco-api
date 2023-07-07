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
from apteco_api.models.paged_results_team_summary import PagedResultsTeamSummary  # noqa: E501
from apteco_api.rest import ApiException

class TestPagedResultsTeamSummary(unittest.TestCase):
    """PagedResultsTeamSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResultsTeamSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.paged_results_team_summary.PagedResultsTeamSummary()  # noqa: E501
        if include_optional :
            return PagedResultsTeamSummary(
                offset = 56, 
                count = 56, 
                total_count = 56, 
                list = [
                    apteco_api.models.team_summary.TeamSummary(
                        id = 56, 
                        name = '0', )
                    ]
            )
        else :
            return PagedResultsTeamSummary(
                offset = 56,
                count = 56,
                total_count = 56,
                list = [
                    apteco_api.models.team_summary.TeamSummary(
                        id = 56, 
                        name = '0', )
                    ],
        )

    def testPagedResultsTeamSummary(self):
        """Test PagedResultsTeamSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()