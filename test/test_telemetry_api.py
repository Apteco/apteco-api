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
from apteco_api.api.telemetry_api import TelemetryApi  # noqa: E501
from apteco_api.rest import ApiException


class TestTelemetryApi(unittest.TestCase):
    """TelemetryApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.telemetry_api.TelemetryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_telemetry_create_telemetry_session(self):
        """Test case for telemetry_create_telemetry_session

        Creates a new telemetry session from the given details  # noqa: E501
        """
        pass

    def test_telemetry_create_telemetry_state(self):
        """Test case for telemetry_create_telemetry_state

        Creates a new telemetry state from the given details  # noqa: E501
        """
        pass

    def test_telemetry_get_telemetry_session(self):
        """Test case for telemetry_get_telemetry_session

        Returns the details of a particular telemetry session  # noqa: E501
        """
        pass

    def test_telemetry_get_telemetry_state(self):
        """Test case for telemetry_get_telemetry_state

        Returns the details of a particular telemetry state  # noqa: E501
        """
        pass

    def test_telemetry_get_telemetry_state_for_user(self):
        """Test case for telemetry_get_telemetry_state_for_user

        Returns the details of a given user's telemetry state  # noqa: E501
        """
        pass

    def test_telemetry_update_telemetry_session(self):
        """Test case for telemetry_update_telemetry_session

        Update a particular telemetry session from the given details  # noqa: E501
        """
        pass

    def test_telemetry_update_telemetry_state(self):
        """Test case for telemetry_update_telemetry_state

        Updates a particular telemetry state from the given details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
