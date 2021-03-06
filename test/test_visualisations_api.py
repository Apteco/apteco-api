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
from apteco_api.api.visualisations_api import VisualisationsApi  # noqa: E501
from apteco_api.rest import ApiException


class TestVisualisationsApi(unittest.TestCase):
    """VisualisationsApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.visualisations_api.VisualisationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_visualisations_cancel_visualisation_render_data_refresh_job(self):
        """Test case for visualisations_cancel_visualisation_render_data_refresh_job

        Cancel a job refreshing the render data for a particular visualisation  # noqa: E501
        """
        pass

    def test_visualisations_create_visualisation_render_data_refresh_job(self):
        """Test case for visualisations_create_visualisation_render_data_refresh_job

        Creates a job to refresh the render data for a particular visualisation  # noqa: E501
        """
        pass

    def test_visualisations_get_visualisation(self):
        """Test case for visualisations_get_visualisation

        Returns the details of a particular visualisation  # noqa: E501
        """
        pass

    def test_visualisations_get_visualisation_render_data(self):
        """Test case for visualisations_get_visualisation_render_data

        Returns the render data for a particular visualisation  # noqa: E501
        """
        pass

    def test_visualisations_get_visualisation_render_data_refresh_job(self):
        """Test case for visualisations_get_visualisation_render_data_refresh_job

        Returns the details of a job to refresh the render data for a particular visualisation  # noqa: E501
        """
        pass

    def test_visualisations_perform_visualisation_render_data_refresh_synchronously(self):
        """Test case for visualisations_perform_visualisation_render_data_refresh_synchronously

        Performs a synchronous refresh of the render data for a particular visualisation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
