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
from apteco_api.models.user_audience_composition_detail import UserAudienceCompositionDetail  # noqa: E501
from apteco_api.rest import ApiException

class TestUserAudienceCompositionDetail(unittest.TestCase):
    """UserAudienceCompositionDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserAudienceCompositionDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.user_audience_composition_detail.UserAudienceCompositionDetail()  # noqa: E501
        if include_optional :
            return UserAudienceCompositionDetail(
                viewing_username = '0', 
                shared_to_me = True, 
                shared_by_me = True, 
                check_composition_definition = apteco_api.models.check_composition_definition.CheckCompositionDefinition(
                    dashboard_items = [
                        apteco_api.models.dashboard_item.DashboardItem(
                            variable_name = '0', 
                            size = apteco_api.models.size.Size(
                                width = 1.337, 
                                height = 1.337, ), 
                            chart_type = 'Bar', 
                            omit_zeros = True, 
                            sort_order = 'Natural', 
                            description = '0', )
                        ], 
                    grid_items = [
                        apteco_api.models.grid_item.GridItem(
                            variable_name = '0', 
                            detail = 'Code', 
                            unclassified_format = 'FromDesign', 
                            description = '0', )
                        ], ), 
                export_composition_definition = apteco_api.models.export_composition_definition.ExportCompositionDefinition(
                    output = apteco_api.models.output.Output(
                        format = 'CSV', 
                        delimiter = '0', 
                        alpha_encloser = '0', 
                        numeric_encloser = '0', 
                        authorisation_code = '0', 
                        export_extra_name = '0', ), 
                    grid_items = [
                        apteco_api.models.grid_item.GridItem(
                            variable_name = '0', 
                            detail = 'Code', 
                            unclassified_format = 'FromDesign', 
                            description = '0', )
                        ], ), 
                compositions_lookup = apteco_api.models.system_lookup.SystemLookup(
                    variables_lookup = [
                        apteco_api.models.variable_lookup.VariableLookup(
                            variable = apteco_api.models.variable.Variable(
                                name = '0', 
                                description = '0', 
                                type = 'Selector', 
                                folder_name = '0', 
                                table_name = '0', 
                                is_selectable = True, 
                                is_browsable = True, 
                                is_exportable = True, 
                                is_virtual = True, 
                                selector_info = apteco_api.models.selector_variable_info.SelectorVariableInfo(
                                    selector_type = 'SingleValue', 
                                    sub_type = 'Categorical', 
                                    var_code_order = 'Nominal', 
                                    number_of_codes = 56, 
                                    code_length = 56, 
                                    minimum_var_code_count = 56, 
                                    maximum_var_code_count = 56, 
                                    minimum_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    maximum_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    combined_from_variable_name = '0', ), 
                                numeric_info = apteco_api.models.numeric_variable_info.NumericVariableInfo(
                                    minimum = 1.337, 
                                    maximum = 1.337, 
                                    is_currency = True, 
                                    currency_locale = '0', 
                                    currency_symbol = '0', ), 
                                text_info = apteco_api.models.text_variable_info.TextVariableInfo(
                                    maximum_text_length = 56, ), 
                                reference_info = apteco_api.models.reference_variable_info.ReferenceVariableInfo(), ), 
                            var_codes_lookup = [
                                apteco_api.models.var_code.VarCode(
                                    code = '0', 
                                    description = '0', 
                                    count = 56, )
                                ], )
                        ], 
                    folders_lookup = [
                        apteco_api.models.folder.Folder(
                            name = '0', 
                            description = '0', )
                        ], ), 
                id = 56, 
                description = '0', 
                type = 'Check', 
                system_name = '0', 
                owner = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', ), 
                number_of_users_shared_with = 56, 
                shared_to_all = True, 
                share_id = 56
            )
        else :
            return UserAudienceCompositionDetail(
                viewing_username = '0',
                shared_to_me = True,
                shared_by_me = True,
                id = 56,
                description = '0',
                type = 'Check',
                system_name = '0',
                owner = apteco_api.models.user_display_details.UserDisplayDetails(
                    id = 56, 
                    username = '0', 
                    firstname = '0', 
                    surname = '0', 
                    email_address = '0', ),
                number_of_users_shared_with = 56,
                shared_to_all = True,
        )

    def testUserAudienceCompositionDetail(self):
        """Test UserAudienceCompositionDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
