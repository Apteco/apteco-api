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

import apteco_api
from apteco_api.api.teams_api import TeamsApi  # noqa: E501
from apteco_api.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.teams_api.TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_teams_create_team(self):
        """Test case for teams_create_team

        Requires OrbitAdmin: Creates a new team.  # noqa: E501
        """
        pass

    def test_teams_delete_team(self):
        """Test case for teams_delete_team

        Requires OrbitAdmin: Deletes the specified team  # noqa: E501
        """
        pass

    def test_teams_get_team(self):
        """Test case for teams_get_team

        Requires OrbitAdmin: Returns the detail for a team.  # noqa: E501
        """
        pass

    def test_teams_get_teams(self):
        """Test case for teams_get_teams

        Returns all teams in the DataView.  # noqa: E501
        """
        pass

    def test_teams_modify_team(self):
        """Test case for teams_modify_team

        Requires OrbitAdmin: Modify the specified team  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
