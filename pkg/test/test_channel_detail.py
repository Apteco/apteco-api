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
from apteco_api.models.channel_detail import ChannelDetail  # noqa: E501
from apteco_api.rest import ApiException

class TestChannelDetail(unittest.TestCase):
    """ChannelDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChannelDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.channel_detail.ChannelDetail()  # noqa: E501
        if include_optional :
            return ChannelDetail(
                id = '0', 
                schema_id = 56, 
                description = '0', 
                type = 'Unknown', 
                parent_id = '0'
            )
        else :
            return ChannelDetail(
                id = '0',
                description = '0',
                type = 'Unknown',
        )

    def testChannelDetail(self):
        """Test ChannelDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
