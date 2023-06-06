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
from apteco_api.models.paged_results_dashboard_summary import PagedResultsDashboardSummary  # noqa: E501
from apteco_api.rest import ApiException

class TestPagedResultsDashboardSummary(unittest.TestCase):
    """PagedResultsDashboardSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResultsDashboardSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.paged_results_dashboard_summary.PagedResultsDashboardSummary()  # noqa: E501
        if include_optional :
            return PagedResultsDashboardSummary(
                offset = 56, 
                count = 56, 
                total_count = 56, 
                list = [
                    apteco_api.models.dashboard_summary.DashboardSummary(
                        id = 56, 
                        title = '0', 
                        description = '0', 
                        system_name = '0', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_updated_by = '0', 
                        deleted_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return PagedResultsDashboardSummary(
                offset = 56,
                count = 56,
                total_count = 56,
                list = [
                    apteco_api.models.dashboard_summary.DashboardSummary(
                        id = 56, 
                        title = '0', 
                        description = '0', 
                        system_name = '0', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_updated_by = '0', 
                        deleted_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )

    def testPagedResultsDashboardSummary(self):
        """Test PagedResultsDashboardSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
