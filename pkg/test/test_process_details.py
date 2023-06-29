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
from apteco_api.models.process_details import ProcessDetails  # noqa: E501
from apteco_api.rest import ApiException

class TestProcessDetails(unittest.TestCase):
    """ProcessDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProcessDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.process_details.ProcessDetails()  # noqa: E501
        if include_optional :
            return ProcessDetails(
                process_id = 56, 
                private_memory_in_bytes = 56, 
                working_set_in_bytes = 56, 
                heap_size_in_bytes = 56, 
                is_server_garbage_collection_enabled = True
            )
        else :
            return ProcessDetails(
                process_id = 56,
                private_memory_in_bytes = 56,
                working_set_in_bytes = 56,
                heap_size_in_bytes = 56,
                is_server_garbage_collection_enabled = True,
        )

    def testProcessDetails(self):
        """Test ProcessDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
