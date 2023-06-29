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
from apteco_api.models.audience_result_summary import AudienceResultSummary  # noqa: E501
from apteco_api.rest import ApiException

class TestAudienceResultSummary(unittest.TestCase):
    """AudienceResultSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AudienceResultSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.audience_result_summary.AudienceResultSummary()  # noqa: E501
        if include_optional :
            return AudienceResultSummary(
                id = 56, 
                audience_update_id = 56, 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                fast_stats_build_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = apteco_api.models.user_display_details.UserDisplayDetails(
                    username = '', 
                    firstname = '', 
                    surname = '', 
                    email_address = '', ), 
                nett_results = apteco_api.models.audience_query_result.AudienceQueryResult(
                    counts = [
                        apteco_api.models.count.Count(
                            table_name = '', 
                            count_value = 56, )
                        ], 
                    messages = [
                        apteco_api.models.server_message.ServerMessage(
                            type = 'Error', 
                            number = 56, 
                            text = '', )
                        ], ), 
                urn_file_path = ''
            )
        else :
            return AudienceResultSummary(
                id = 56,
                audience_update_id = 56,
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fast_stats_build_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = apteco_api.models.user_display_details.UserDisplayDetails(
                    username = '', 
                    firstname = '', 
                    surname = '', 
                    email_address = '', ),
                nett_results = apteco_api.models.audience_query_result.AudienceQueryResult(
                    counts = [
                        apteco_api.models.count.Count(
                            table_name = '', 
                            count_value = 56, )
                        ], 
                    messages = [
                        apteco_api.models.server_message.ServerMessage(
                            type = 'Error', 
                            number = 56, 
                            text = '', )
                        ], ),
                urn_file_path = '',
        )

    def testAudienceResultSummary(self):
        """Test AudienceResultSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
