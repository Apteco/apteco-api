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
from apteco_api.api.audience_hits_api import AudienceHitsApi  # noqa: E501
from apteco_api.rest import ApiException


class TestAudienceHitsApi(unittest.TestCase):
    """AudienceHitsApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.audience_hits_api.AudienceHitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_audience_hits_get_audience_hit(self):
        """Test case for audience_hits_get_audience_hit

        Requires OrbitAdmin: Returns details for a given audience hit  # noqa: E501
        """
        pass

    def test_audience_hits_get_audience_hits(self):
        """Test case for audience_hits_get_audience_hits

        Requires OrbitAdmin: Returns all the hit information for all audiences.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
