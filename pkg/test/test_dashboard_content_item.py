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
from apteco_api.models.dashboard_content_item import DashboardContentItem  # noqa: E501
from apteco_api.rest import ApiException

class TestDashboardContentItem(unittest.TestCase):
    """DashboardContentItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DashboardContentItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.dashboard_content_item.DashboardContentItem()  # noqa: E501
        if include_optional :
            return DashboardContentItem(
                id = '0', 
                title = '0', 
                breakpoints = [
                    apteco_api.models.breakpoint.Breakpoint(
                        breakpoint = 'xs', 
                        x = 56, 
                        y = 56, 
                        size = apteco_api.models.size.Size(
                            width = 1.337, 
                            height = 1.337, ), 
                        notes_alignment = apteco_api.models.notes_alignment.NotesAlignment(
                            notes_position = 'Top', 
                            notes_content_vertical_alignment = 'Top', 
                            notes_content_horizontal_alignment = 'Left', ), )
                    ], 
                dashboard_item_details = [
                    apteco_api.models.dashboard_content_item_detail.DashboardContentItemDetail(
                        drilldown_level = 56, 
                        description = '0', 
                        chart_type = 'Bar', 
                        data_specification = apteco_api.models.dashboard_item_data_specification.DashboardItemDataSpecification(
                            cube_specification = apteco_api.models.cube_specification.CubeSpecification(
                                dimensions = [
                                    apteco_api.models.dimension.Dimension(
                                        id = '0', 
                                        type = 'Selector', 
                                        query = apteco_api.models.query.Query(
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
                                        variable_name = '0', 
                                        banding = apteco_api.models.dimension_banding.DimensionBanding(
                                            type = 'None', 
                                            custom_values = '0', ), 
                                        function = 'None', 
                                        none_cell = True, 
                                        omit_unclassified = True, 
                                        filter_query = apteco_api.models.query.Query(
                                            today_at = '0', ), 
                                        minimum_category_count = 56, 
                                        top_n_category_count = 56, 
                                        percentage_of_maximum_category_threshold = 56, )
                                    ], 
                                measures = [
                                    apteco_api.models.measure.Measure(
                                        id = '0', 
                                        resolve_table_name = '0', 
                                        function = 'Count', 
                                        variable_name = '0', 
                                        expression = apteco_api.models.expression.Expression(
                                            table_name = '0', 
                                            desc = '0', 
                                            display_text = '0', 
                                            server_text = '0', 
                                            output_type = 'Double', 
                                            string_size = 56, ), 
                                        sort = 'None', )
                                    ], ), 
                            pareto_specification = apteco_api.models.pareto_specification.ParetoSpecification(
                                value_variable_name = '0', 
                                category_variable_name = '0', 
                                number_of_bands = 56, 
                                resolve_table_name = '0', ), ), 
                        allow_category_display = True, 
                        category_display = apteco_api.models.dashboard_item_category_display.DashboardItemCategoryDisplay(
                            display_type = 'All', 
                            limit = 56, 
                            auto_adjust = True, 
                            user_adjust = True, ), 
                        omit_zeros = True, 
                        omit_unclassified = True, 
                        sort_order = 'Natural', 
                        show_underlying_data = True, 
                        notes = '0', )
                    ]
            )
        else :
            return DashboardContentItem(
                id = '0',
                title = '0',
        )

    def testDashboardContentItem(self):
        """Test DashboardContentItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
