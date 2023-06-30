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
from apteco_api.models.paged_results_folder_structure_node import PagedResultsFolderStructureNode  # noqa: E501
from apteco_api.rest import ApiException

class TestPagedResultsFolderStructureNode(unittest.TestCase):
    """PagedResultsFolderStructureNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResultsFolderStructureNode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.paged_results_folder_structure_node.PagedResultsFolderStructureNode()  # noqa: E501
        if include_optional :
            return PagedResultsFolderStructureNode(
                offset = 56, 
                count = 56, 
                total_count = 56, 
                list = [
                    apteco_api.models.folder_structure_node.FolderStructureNode(
                        folder = apteco_api.models.folder.Folder(
                            name = '0', 
                            description = '0', ), 
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
                            reference_info = apteco_api.models.reference_variable_info.ReferenceVariableInfo(), ), )
                    ]
            )
        else :
            return PagedResultsFolderStructureNode(
                offset = 56,
                count = 56,
                total_count = 56,
                list = [
                    apteco_api.models.folder_structure_node.FolderStructureNode(
                        folder = apteco_api.models.folder.Folder(
                            name = '0', 
                            description = '0', ), 
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
                            reference_info = apteco_api.models.reference_variable_info.ReferenceVariableInfo(), ), )
                    ],
        )

    def testPagedResultsFolderStructureNode(self):
        """Test PagedResultsFolderStructureNode"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
