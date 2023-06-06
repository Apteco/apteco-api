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
from apteco_api.models.modify_user_audience_detail_results import ModifyUserAudienceDetailResults  # noqa: E501
from apteco_api.rest import ApiException

class TestModifyUserAudienceDetailResults(unittest.TestCase):
    """ModifyUserAudienceDetailResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModifyUserAudienceDetailResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.modify_user_audience_detail_results.ModifyUserAudienceDetailResults()  # noqa: E501
        if include_optional :
            return ModifyUserAudienceDetailResults(
                audience = apteco_api.models.user_audience_detail.UserAudienceDetail(
                    viewing_username = '0', 
                    status = 'Default', 
                    shared_to_me = True, 
                    shared_by_me = True, 
                    brief_text = '0', 
                    exclude_query = apteco_api.models.query.Query(
                        selection = apteco_api.models.selection.Selection(
                            ancestor_counts = True, 
                            record_set = apteco_api.models.record_set.RecordSet(
                                type = 'URN', 
                                key_variable_name = '0', 
                                by_reference = True, 
                                path = '0', 
                                transient = True, 
                                values = '0', 
                                min_occurs = 56, ), 
                            rule = apteco_api.models.rule.Rule(
                                clause = apteco_api.models.clause.Clause(
                                    logic = apteco_api.models.logic.Logic(
                                        operation = 'INCLUDE', 
                                        operands = [
                                            apteco_api.models.clause.Clause(
                                                criteria = apteco_api.models.criteria.Criteria(
                                                    variable_name = '0', 
                                                    path = '0', 
                                                    include = True, 
                                                    ignore_case = True, 
                                                    text_match_type = 'Ranges', 
                                                    value_rules = [
                                                        apteco_api.models.value_rule.ValueRule(
                                                            age_rule = apteco_api.models.age_rule.AgeRule(
                                                                range_low = 56, 
                                                                range_high = 56, 
                                                                units = 'Days', 
                                                                relative_to = 'Actual', 
                                                                reference_type = 'Today', 
                                                                reference_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                                            date_rule = apteco_api.models.date_rule.DateRule(
                                                                pattern_frequency = 'Daily', 
                                                                pattern_interval = 56, 
                                                                pattern_type = 'CalculatedDay', 
                                                                pattern_days_of_week = [
                                                                    'None'
                                                                    ], 
                                                                pattern_day_of_month = 56, 
                                                                pattern_month_of_year = 56, 
                                                                pattern_occurrence_of_day_in_month = 'None', 
                                                                start_range_limit = 'Earliest', 
                                                                range_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                start_range_relative = 'Today', 
                                                                start_range_offset_direction = 'Forward', 
                                                                start_range_offset = 56, 
                                                                start_range_offset_units = 'Days', 
                                                                end_range_limit = 'Earliest', 
                                                                range_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                end_range_relative = 'Today', 
                                                                end_range_offset_direction = 'Forward', 
                                                                end_range_offset = 56, 
                                                                end_range_offset_units = 'Days', 
                                                                range_max_occurrences = 56, ), 
                                                            list_rule = apteco_api.models.list_rule.ListRule(
                                                                banding_type = 'None', 
                                                                list = '0', 
                                                                variable_name = '0', ), 
                                                            time_rule = apteco_api.models.time_rule.TimeRule(
                                                                range_low = '0', 
                                                                range_high = '0', ), 
                                                            predefined_rule = 'DateRange', 
                                                            name = '0', )
                                                        ], 
                                                    expression_rule = apteco_api.models.expression.Expression(
                                                        table_name = '0', 
                                                        queries = [
                                                            apteco_api.models.query.Query(
                                                                today_at = '0', )
                                                            ], 
                                                        desc = '0', 
                                                        display_text = '0', 
                                                        server_text = '0', 
                                                        query_descriptions = [
                                                            '0'
                                                            ], 
                                                        output_type = 'Double', 
                                                        string_size = 56, ), 
                                                    today_at = '0', 
                                                    table_name = '0', 
                                                    name = '0', ), 
                                                sub_selection = apteco_api.models.sub_selection.SubSelection(
                                                    by_reference = True, 
                                                    path = '0', ), )
                                            ], 
                                        table_name = '0', 
                                        name = '0', ), 
                                    criteria = apteco_api.models.criteria.Criteria(
                                        variable_name = '0', 
                                        path = '0', 
                                        include = True, 
                                        ignore_case = True, 
                                        text_match_type = 'Ranges', 
                                        today_at = '0', 
                                        table_name = '0', 
                                        name = '0', ), 
                                    sub_selection = apteco_api.models.sub_selection.SubSelection(
                                        by_reference = True, 
                                        path = '0', ), ), ), 
                            rfv = apteco_api.models.rfv.RFV(
                                frequency = apteco_api.models.rfv_frequency.RFVFrequency(
                                    values = '0', ), 
                                recency = apteco_api.models.rfv_recency.RFVRecency(
                                    variable_name = '0', 
                                    sequence = '0', 
                                    direction = 'Any', 
                                    value = 56, 
                                    distinct = True, ), 
                                value = apteco_api.models.rfv_value.RFVValue(
                                    variable_name = '0', 
                                    action = 'Sum', 
                                    values = '0', ), 
                                grouping_table = '0', 
                                transactional_table = '0', ), 
                            n_per = apteco_api.models.n_per.NPer(
                                grouping_table_name = '0', 
                                transactional_table_name = '0', ), 
                            top_n = apteco_api.models.top_n.TopN(
                                variable_name = '0', 
                                order_expression = apteco_api.models.expression.Expression(
                                    table_name = '0', 
                                    desc = '0', 
                                    display_text = '0', 
                                    server_text = '0', 
                                    output_type = 'Double', 
                                    string_size = 56, ), 
                                expression = '0', 
                                direction = 'Top', 
                                percent = 1.337, 
                                min_value = 1.337, 
                                max_value = 1.337, 
                                sequence = '0', 
                                grouping_variable_name = '0', 
                                grouping_sequence_variable_name = '0', 
                                grouping_ascending = True, 
                                grouping_sequence = '0', 
                                group_max = 56, ), 
                            limits = apteco_api.models.limits.Limits(
                                sampling = 'All', 
                                stop_at_limit = True, 
                                total = 56, 
                                type = 'None', 
                                start_at = 56, 
                                percent = 1.337, 
                                fraction = apteco_api.models.fraction.Fraction(
                                    numerator = 56, 
                                    denominator = 56, ), ), 
                            table_name = '0', 
                            name = '0', ), 
                        today_at = '0', ), 
                    include_query = apteco_api.models.query.Query(
                        today_at = '0', ), 
                    body_query = apteco_api.models.query.Query(
                        today_at = '0', ), 
                    selection_modifiers = apteco_api.models.selection_modifiers.SelectionModifiers(), 
                    queries_lookup = apteco_api.models.system_lookup.SystemLookup(
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
                            ], ), 
                    last_result = apteco_api.models.audience_result_detail.AudienceResultDetail(
                        exclude_results = apteco_api.models.audience_query_result.AudienceQueryResult(
                            counts = [
                                apteco_api.models.count.Count(
                                    table_name = '0', 
                                    count_value = 56, )
                                ], 
                            messages = [
                                apteco_api.models.server_message.ServerMessage(
                                    type = 'Error', 
                                    number = 56, 
                                    text = '0', )
                                ], ), 
                        include_results = apteco_api.models.audience_query_result.AudienceQueryResult(), 
                        body_results = apteco_api.models.audience_query_result.AudienceQueryResult(), 
                        id = 56, 
                        audience_update_id = 56, 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        fast_stats_build_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user = apteco_api.models.user_display_details.UserDisplayDetails(
                            username = '0', 
                            firstname = '0', 
                            surname = '0', 
                            email_address = '0', ), 
                        nett_results = apteco_api.models.audience_query_result.AudienceQueryResult(), 
                        urn_file_path = '0', ), 
                    id = 56, 
                    title = '0', 
                    description = '0', 
                    creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    owner = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '0', 
                        firstname = '0', 
                        surname = '0', 
                        email_address = '0', ), 
                    deletion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    resolve_table_name = '0', 
                    resolve_table_nett_count = 56, 
                    number_of_users_shared_with = 56, 
                    share_id = 56, 
                    number_of_hits = 56, 
                    system_name = '0', 
                    last_updated_user = apteco_api.models.user_display_details.UserDisplayDetails(
                        username = '0', 
                        firstname = '0', 
                        surname = '0', 
                        email_address = '0', ), 
                    last_updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_update_id = 56, ), 
                id = 56, 
                succeeded = True, 
                status = '0', 
                status_code = 56
            )
        else :
            return ModifyUserAudienceDetailResults(
                id = 56,
                succeeded = True,
                status = '0',
                status_code = 56,
        )

    def testModifyUserAudienceDetailResults(self):
        """Test ModifyUserAudienceDetailResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
