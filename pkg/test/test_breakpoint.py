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
from apteco_api.models.breakpoint import Breakpoint  # noqa: E501
from apteco_api.rest import ApiException

class TestBreakpoint(unittest.TestCase):
    """Breakpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Breakpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.breakpoint.Breakpoint()  # noqa: E501
        if include_optional :
            return Breakpoint(
                breakpoint = 'xs', 
                x = 56, 
                y = 56, 
                size = apteco_api.models.size.Size(
                    width = 1.337, 
                    height = 1.337, ), 
                notes_alignment = apteco_api.models.notes_alignment.NotesAlignment(
                    notes_position = 'Top', 
                    notes_content_vertical_alignment = 'Top', 
                    notes_content_horizontal_alignment = 'Left', )
            )
        else :
            return Breakpoint(
                breakpoint = 'xs',
                x = 56,
                y = 56,
                size = apteco_api.models.size.Size(
                    width = 1.337, 
                    height = 1.337, ),
                notes_alignment = apteco_api.models.notes_alignment.NotesAlignment(
                    notes_position = 'Top', 
                    notes_content_vertical_alignment = 'Top', 
                    notes_content_horizontal_alignment = 'Left', ),
        )

    def testBreakpoint(self):
        """Test Breakpoint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()