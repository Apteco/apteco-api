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
from apteco_api.models.abstract_render_spec import AbstractRenderSpec  # noqa: E501
from apteco_api.rest import ApiException

class TestAbstractRenderSpec(unittest.TestCase):
    """AbstractRenderSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AbstractRenderSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.abstract_render_spec.AbstractRenderSpec()  # noqa: E501
        if include_optional :
            return AbstractRenderSpec(
                type = '0', 
                title = '0', 
                page_width = 56, 
                page_height = 56, 
                visualisation_width = 56, 
                visualisation_height = 56, 
                ran_successfully = True, 
                notes_title = '0', 
                notes = '0', 
                show_notes = True, 
                selection_title = '0', 
                show_selection = True, 
                last_run_details = apteco_api.models.last_run_details.LastRunDetails(
                    system_name = '0', 
                    system_load_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_name = '0', 
                    run_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                query_details = apteco_api.models.query_details.QueryDetails(
                    description = '0', 
                    counts = [
                        apteco_api.models.query_detail_count.QueryDetailCount(
                            table_name = '0', 
                            table_description = '0', 
                            count_value = 56, )
                        ], 
                    properties = [
                        apteco_api.models.property.Property(
                            name = '0', 
                            property_value = '0', 
                            hidden = True, )
                        ], )
            )
        else :
            return AbstractRenderSpec(
        )

    def testAbstractRenderSpec(self):
        """Test AbstractRenderSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()