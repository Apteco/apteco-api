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
from apteco_api.models.paged_results_element_status import PagedResultsElementStatus  # noqa: E501
from apteco_api.rest import ApiException

class TestPagedResultsElementStatus(unittest.TestCase):
    """PagedResultsElementStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResultsElementStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.paged_results_element_status.PagedResultsElementStatus()  # noqa: E501
        if include_optional :
            return PagedResultsElementStatus(
                offset = 56, 
                count = 56, 
                total_count = 56, 
                list = [
                    apteco_api.models.element_status.ElementStatus(
                        id = '0', 
                        description = '0', 
                        type = 'Unknown', 
                        successful_campaigns_count = 56, 
                        errored_campaigns_count = 56, 
                        inactive_campaigns_count = 56, 
                        needs_approval_campaigns_count = 56, 
                        channel_types = [
                            'Unknown'
                            ], 
                        first_ran = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_ran = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        statistics_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        path = [
                            apteco_api.models.element_key.ElementKey(
                                id = '0', 
                                description = '0', )
                            ], )
                    ]
            )
        else :
            return PagedResultsElementStatus(
                offset = 56,
                count = 56,
                total_count = 56,
                list = [
                    apteco_api.models.element_status.ElementStatus(
                        id = '0', 
                        description = '0', 
                        type = 'Unknown', 
                        successful_campaigns_count = 56, 
                        errored_campaigns_count = 56, 
                        inactive_campaigns_count = 56, 
                        needs_approval_campaigns_count = 56, 
                        channel_types = [
                            'Unknown'
                            ], 
                        first_ran = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_ran = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        statistics_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        path = [
                            apteco_api.models.element_key.ElementKey(
                                id = '0', 
                                description = '0', )
                            ], )
                    ],
        )

    def testPagedResultsElementStatus(self):
        """Test PagedResultsElementStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
