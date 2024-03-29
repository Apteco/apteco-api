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
from apteco_api.models.value_rule import ValueRule  # noqa: E501
from apteco_api.rest import ApiException

class TestValueRule(unittest.TestCase):
    """ValueRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ValueRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.value_rule.ValueRule()  # noqa: E501
        if include_optional :
            return ValueRule(
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
                name = '0'
            )
        else :
            return ValueRule(
        )

    def testValueRule(self):
        """Test ValueRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
