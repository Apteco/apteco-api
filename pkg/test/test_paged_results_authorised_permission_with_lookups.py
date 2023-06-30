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
from apteco_api.models.paged_results_authorised_permission_with_lookups import PagedResultsAuthorisedPermissionWithLookups  # noqa: E501
from apteco_api.rest import ApiException

class TestPagedResultsAuthorisedPermissionWithLookups(unittest.TestCase):
    """PagedResultsAuthorisedPermissionWithLookups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResultsAuthorisedPermissionWithLookups
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.paged_results_authorised_permission_with_lookups.PagedResultsAuthorisedPermissionWithLookups()  # noqa: E501
        if include_optional :
            return PagedResultsAuthorisedPermissionWithLookups(
                offset = 56, 
                count = 56, 
                total_count = 56, 
                list = [
                    apteco_api.models.authorised_permission_with_lookups.AuthorisedPermissionWithLookups(
                        authorised_permission = apteco_api.models.authorised_permission.AuthorisedPermission(
                            id = 56, 
                            permission = apteco_api.models.permission.permission(), 
                            permission_type = 'Unknown', 
                            resource = '0', 
                            resource_type = 'Unknown', 
                            grant = True, 
                            deny = True, 
                            inherit = True, 
                            permission_set = apteco_api.models.permission_set.PermissionSet(
                                id = 56, 
                                name = '0', 
                                system_name = '0', 
                                system_permission_set = True, ), 
                            authority = apteco_api.models.authority.Authority(
                                authority_id = 56, 
                                id = apteco_api.models.id.Id(
                                    id_type = 'None', 
                                    id_value = 56, ), ), 
                            team = apteco_api.models.team_summary.TeamSummary(
                                id = 56, 
                                name = '0', ), ), 
                        lookups = apteco_api.models.lookups.Lookups(
                            system_lookup = apteco_api.models.system_lookup.SystemLookup(
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
                            people_stage_lookup = apteco_api.models.people_stage_lookup.PeopleStageLookup(
                                people_stage_elements_lookup = [
                                    apteco_api.models.element_summary.ElementSummary(
                                        id = '0', 
                                        description = '0', 
                                        type = 'Unknown', 
                                        schema_id = 56, 
                                        schema_id_type = 'Unknown', 
                                        parent_id = '0', 
                                        parent_type = 'Unknown', 
                                        path = [
                                            apteco_api.models.element_key.ElementKey(
                                                id = '0', 
                                                description = '0', )
                                            ], )
                                    ], ), 
                            users_lookup = apteco_api.models.users_lookup.UsersLookup(
                                user_lookup = [
                                    apteco_api.models.user_summary.UserSummary(
                                        id = 56, 
                                        username = '0', 
                                        group_id = 56, 
                                        teams = [
                                            apteco_api.models.team_summary.TeamSummary(
                                                id = 56, 
                                                name = '0', )
                                            ], 
                                        firstname = '0', 
                                        surname = '0', 
                                        email_address = '0', 
                                        user_disabled_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                group_lookup = [
                                    apteco_api.models.group_summary.GroupSummary(
                                        id = 56, 
                                        name = '0', )
                                    ], 
                                team_lookup = [
                                    apteco_api.models.team_summary.TeamSummary(
                                        id = 56, 
                                        name = '0', )
                                    ], ), ), )
                    ]
            )
        else :
            return PagedResultsAuthorisedPermissionWithLookups(
                offset = 56,
                count = 56,
                total_count = 56,
                list = [
                    apteco_api.models.authorised_permission_with_lookups.AuthorisedPermissionWithLookups(
                        authorised_permission = apteco_api.models.authorised_permission.AuthorisedPermission(
                            id = 56, 
                            permission = apteco_api.models.permission.permission(), 
                            permission_type = 'Unknown', 
                            resource = '0', 
                            resource_type = 'Unknown', 
                            grant = True, 
                            deny = True, 
                            inherit = True, 
                            permission_set = apteco_api.models.permission_set.PermissionSet(
                                id = 56, 
                                name = '0', 
                                system_name = '0', 
                                system_permission_set = True, ), 
                            authority = apteco_api.models.authority.Authority(
                                authority_id = 56, 
                                id = apteco_api.models.id.Id(
                                    id_type = 'None', 
                                    id_value = 56, ), ), 
                            team = apteco_api.models.team_summary.TeamSummary(
                                id = 56, 
                                name = '0', ), ), 
                        lookups = apteco_api.models.lookups.Lookups(
                            system_lookup = apteco_api.models.system_lookup.SystemLookup(
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
                            people_stage_lookup = apteco_api.models.people_stage_lookup.PeopleStageLookup(
                                people_stage_elements_lookup = [
                                    apteco_api.models.element_summary.ElementSummary(
                                        id = '0', 
                                        description = '0', 
                                        type = 'Unknown', 
                                        schema_id = 56, 
                                        schema_id_type = 'Unknown', 
                                        parent_id = '0', 
                                        parent_type = 'Unknown', 
                                        path = [
                                            apteco_api.models.element_key.ElementKey(
                                                id = '0', 
                                                description = '0', )
                                            ], )
                                    ], ), 
                            users_lookup = apteco_api.models.users_lookup.UsersLookup(
                                user_lookup = [
                                    apteco_api.models.user_summary.UserSummary(
                                        id = 56, 
                                        username = '0', 
                                        group_id = 56, 
                                        teams = [
                                            apteco_api.models.team_summary.TeamSummary(
                                                id = 56, 
                                                name = '0', )
                                            ], 
                                        firstname = '0', 
                                        surname = '0', 
                                        email_address = '0', 
                                        user_disabled_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                group_lookup = [
                                    apteco_api.models.group_summary.GroupSummary(
                                        id = 56, 
                                        name = '0', )
                                    ], 
                                team_lookup = [
                                    apteco_api.models.team_summary.TeamSummary(
                                        id = 56, 
                                        name = '0', )
                                    ], ), ), )
                    ],
        )

    def testPagedResultsAuthorisedPermissionWithLookups(self):
        """Test PagedResultsAuthorisedPermissionWithLookups"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
