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
from apteco_api.api.users_api import UsersApi  # noqa: E501
from apteco_api.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_change_user_password(self):
        """Test case for users_change_user_password

        Change the password for the user with the given username  # noqa: E501
        """
        pass

    def test_users_create_user(self):
        """Test case for users_create_user

        Requires OrbitAdmin: Creates a new user.  # noqa: E501
        """
        pass

    def test_users_delete_user(self):
        """Test case for users_delete_user

        Requires OrbitAdmin: Deletes the specified user  # noqa: E501
        """
        pass

    def test_users_get_previous_login_history(self):
        """Test case for users_get_previous_login_history

        Gets a list of users last login history  # noqa: E501
        """
        pass

    def test_users_get_user_audience(self):
        """Test case for users_get_user_audience

        Returns the details of a particular audience  # noqa: E501
        """
        pass

    def test_users_get_user_audience_composition(self):
        """Test case for users_get_user_audience_composition

        Returns the details of a particular composition  # noqa: E501
        """
        pass

    def test_users_get_user_audience_compositions(self):
        """Test case for users_get_user_audience_compositions

        Returns the list of audience compositions associated with the given user  # noqa: E501
        """
        pass

    def test_users_get_user_audiences(self):
        """Test case for users_get_user_audiences

        Returns the list of audiences associated with the given user  # noqa: E501
        """
        pass

    def test_users_get_user_collection(self):
        """Test case for users_get_user_collection

        Returns the details of a particular collection  # noqa: E501
        """
        pass

    def test_users_get_user_collections(self):
        """Test case for users_get_user_collections

        Returns the list of collections associated with the given user  # noqa: E501
        """
        pass

    def test_users_get_user_configuration(self):
        """Test case for users_get_user_configuration

        Gets the user configuration  # noqa: E501
        """
        pass

    def test_users_get_user_dashboard(self):
        """Test case for users_get_user_dashboard

        Gets a dashboard in the DataView.  # noqa: E501
        """
        pass

    def test_users_get_user_dashboards(self):
        """Test case for users_get_user_dashboards

        Gets a dashboard in the DataView.  # noqa: E501
        """
        pass

    def test_users_get_user_details(self):
        """Test case for users_get_user_details

        Returns details for the given username  # noqa: E501
        """
        pass

    def test_users_get_user_details_list(self):
        """Test case for users_get_user_details_list

        Returns all users in the system.  # noqa: E501
        """
        pass

    def test_users_modify_user_audiences(self):
        """Test case for users_modify_user_audiences

        Updates one or more audiences  # noqa: E501
        """
        pass

    def test_users_modify_user_collections(self):
        """Test case for users_modify_user_collections

        Updates one or more collections  # noqa: E501
        """
        pass

    def test_users_modify_user_dashboards(self):
        """Test case for users_modify_user_dashboards

        Updates one or more dashboards  # noqa: E501
        """
        pass

    def test_users_update_user_details(self):
        """Test case for users_update_user_details

        Updates user details for the given username  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
