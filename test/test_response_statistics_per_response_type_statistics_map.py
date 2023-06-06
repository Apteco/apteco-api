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
from apteco_api.models.response_statistics_per_response_type_statistics_map import ResponseStatisticsPerResponseTypeStatisticsMap  # noqa: E501
from apteco_api.rest import ApiException

class TestResponseStatisticsPerResponseTypeStatisticsMap(unittest.TestCase):
    """ResponseStatisticsPerResponseTypeStatisticsMap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResponseStatisticsPerResponseTypeStatisticsMap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.response_statistics_per_response_type_statistics_map.ResponseStatisticsPerResponseTypeStatisticsMap()  # noqa: E501
        if include_optional :
            return ResponseStatisticsPerResponseTypeStatisticsMap(
                unknown = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_bounce = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_open = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_click = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_reply = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_opt_in = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_opt_out = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_delivered = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                broadcast_failed = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                facebook_like = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                facebook_comment = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                facebook_share = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                facebook_link_click = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                twitter_like = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, ), 
                twitter_retweet = apteco_api.models.per_response_type_statistics.PerResponseTypeStatistics(
                    per_channel_statistics_map = {
                        'key' : apteco_api.models.per_response_type_per_channel_statistics.PerResponseTypePerChannelStatistics(
                            responses_counts = [
                                56
                                ], 
                            total_responses_count = 56, )
                        }, 
                    total_responses_count = 56, )
            )
        else :
            return ResponseStatisticsPerResponseTypeStatisticsMap(
        )

    def testResponseStatisticsPerResponseTypeStatisticsMap(self):
        """Test ResponseStatisticsPerResponseTypeStatisticsMap"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
