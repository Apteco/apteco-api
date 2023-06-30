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
from apteco_api.models.create_update_theme import CreateUpdateTheme  # noqa: E501
from apteco_api.rest import ApiException

class TestCreateUpdateTheme(unittest.TestCase):
    """CreateUpdateTheme unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateUpdateTheme
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.create_update_theme.CreateUpdateTheme()  # noqa: E501
        if include_optional :
            return CreateUpdateTheme(
                name = '0', 
                default = True, 
                published = True, 
                definition = apteco_api.models.theme_definition.ThemeDefinition(
                    visualisation = apteco_api.models.visualisation.Visualisation(
                        title_colour = '0', 
                        title_font = '0', 
                        note_colour = '0', 
                        note_font = '0', 
                        label_colour = '0', 
                        visualisation_colours = [
                            '0'
                            ], 
                        highlight_colours = [
                            '0'
                            ], ), ), 
                logo_id = 56
            )
        else :
            return CreateUpdateTheme(
                name = '0',
                default = True,
                published = True,
                definition = apteco_api.models.theme_definition.ThemeDefinition(
                    visualisation = apteco_api.models.visualisation.Visualisation(
                        title_colour = '0', 
                        title_font = '0', 
                        note_colour = '0', 
                        note_font = '0', 
                        label_colour = '0', 
                        visualisation_colours = [
                            '0'
                            ], 
                        highlight_colours = [
                            '0'
                            ], ), ),
                logo_id = 56,
        )

    def testCreateUpdateTheme(self):
        """Test CreateUpdateTheme"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
