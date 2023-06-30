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
from apteco_api.api.cubes_api import CubesApi  # noqa: E501
from apteco_api.rest import ApiException


class TestCubesApi(unittest.TestCase):
    """CubesApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.cubes_api.CubesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cubes_calculate_cube_synchronously(self):
        """Test case for cubes_calculate_cube_synchronously

        Calcaultes a cube using the given definition and returns the results.  The data to build the cube from is defined by the base query provided.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
