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
from apteco_api.models.expression import Expression  # noqa: E501
from apteco_api.rest import ApiException

class TestExpression(unittest.TestCase):
    """Expression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Expression
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.expression.Expression()  # noqa: E501
        if include_optional :
            return Expression(
                table_name = '', 
                queries = [
                    apteco_api.models.query.Query(
                        selection = apteco_api.models.selection.Selection(
                            ancestor_counts = True, 
                            record_set = apteco_api.models.record_set.RecordSet(
                                type = 'URN', 
                                key_variable_name = '', 
                                by_reference = True, 
                                path = '', 
                                transient = True, 
                                values = '', 
                                min_occurs = 56, ), 
                            rule = apteco_api.models.rule.Rule(
                                clause = apteco_api.models.clause.Clause(
                                    logic = apteco_api.models.logic.Logic(
                                        operation = 'INCLUDE', 
                                        operands = [
                                            apteco_api.models.clause.Clause(
                                                criteria = apteco_api.models.criteria.Criteria(
                                                    variable_name = '', 
                                                    path = '', 
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
                                                                list = '', 
                                                                variable_name = '', ), 
                                                            time_rule = apteco_api.models.time_rule.TimeRule(
                                                                range_low = '', 
                                                                range_high = '', ), 
                                                            predefined_rule = 'DateRange', 
                                                            name = '', )
                                                        ], 
                                                    expression_rule = apteco_api.models.expression.Expression(
                                                        table_name = '', 
                                                        desc = '', 
                                                        display_text = '', 
                                                        server_text = '', 
                                                        query_descriptions = [
                                                            ''
                                                            ], 
                                                        output_type = 'Double', 
                                                        string_size = 56, ), 
                                                    today_at = '', 
                                                    table_name = '', 
                                                    name = '', ), 
                                                sub_selection = apteco_api.models.sub_selection.SubSelection(
                                                    by_reference = True, 
                                                    path = '', ), )
                                            ], 
                                        table_name = '', 
                                        name = '', ), 
                                    criteria = apteco_api.models.criteria.Criteria(
                                        variable_name = '', 
                                        path = '', 
                                        include = True, 
                                        ignore_case = True, 
                                        text_match_type = 'Ranges', 
                                        today_at = '', 
                                        table_name = '', 
                                        name = '', ), 
                                    sub_selection = apteco_api.models.sub_selection.SubSelection(
                                        by_reference = True, 
                                        path = '', ), ), ), 
                            rfv = apteco_api.models.rfv.RFV(
                                frequency = apteco_api.models.rfv_frequency.RFVFrequency(
                                    values = '', ), 
                                recency = apteco_api.models.rfv_recency.RFVRecency(
                                    variable_name = '', 
                                    sequence = '', 
                                    direction = 'Any', 
                                    value = 56, 
                                    distinct = True, ), 
                                value = apteco_api.models.rfv_value.RFVValue(
                                    variable_name = '', 
                                    action = 'Sum', 
                                    values = '', ), 
                                grouping_table = '', 
                                transactional_table = '', ), 
                            n_per = apteco_api.models.n_per.NPer(
                                grouping_table_name = '', 
                                transactional_table_name = '', ), 
                            top_n = apteco_api.models.top_n.TopN(
                                variable_name = '', 
                                order_expression = apteco_api.models.expression.Expression(
                                    table_name = '', 
                                    desc = '', 
                                    display_text = '', 
                                    server_text = '', 
                                    output_type = 'Double', 
                                    string_size = 56, ), 
                                expression = '', 
                                direction = 'Top', 
                                percent = 1.337, 
                                min_value = 1.337, 
                                max_value = 1.337, 
                                sequence = '', 
                                grouping_variable_name = '', 
                                grouping_sequence_variable_name = '', 
                                grouping_ascending = True, 
                                grouping_sequence = '', 
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
                            table_name = '', 
                            name = '', ), 
                        today_at = '', )
                    ], 
                desc = '', 
                display_text = '', 
                server_text = '', 
                query_descriptions = [
                    ''
                    ], 
                output_type = 'Double', 
                string_size = 56
            )
        else :
            return Expression(
        )

    def testExpression(self):
        """Test Expression"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
