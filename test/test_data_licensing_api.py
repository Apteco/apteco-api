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
from apteco_api.api.data_licensing_api import DataLicensingApi  # noqa: E501
from apteco_api.rest import ApiException


class TestDataLicensingApi(unittest.TestCase):
    """DataLicensingApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.data_licensing_api.DataLicensingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_data_licensing_cancel_data_purchase_job(self):
        """Test case for data_licensing_cancel_data_purchase_job

        Cancel a running data purchasing job  # noqa: E501
        """
        pass

    def test_data_licensing_create_purchase_data_licensing_job(self):
        """Test case for data_licensing_create_purchase_data_licensing_job

        Create a new job to purchase data licensing information  # noqa: E501
        """
        pass

    def test_data_licensing_get_data_purchase_job(self):
        """Test case for data_licensing_get_data_purchase_job

        Get the status of a running purchase job  # noqa: E501
        """
        pass

    def test_data_licensing_purchase_data_licensing_sync(self):
        """Test case for data_licensing_purchase_data_licensing_sync

        Purchase data licensing information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
