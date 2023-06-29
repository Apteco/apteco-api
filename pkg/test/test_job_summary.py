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
from apteco_api.models.job_summary import JobSummary  # noqa: E501
from apteco_api.rest import ApiException

class TestJobSummary(unittest.TestCase):
    """JobSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.job_summary.JobSummary()  # noqa: E501
        if include_optional :
            return JobSummary(
                id = 56, 
                priority = 56, 
                state = '', 
                cancel_requested = True, 
                time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_sent = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_finished = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                server = '', 
                system_name = '', 
                thread_number = 56, 
                username = '', 
                job_type = ''
            )
        else :
            return JobSummary(
                id = 56,
                priority = 56,
                state = '',
                cancel_requested = True,
                server = '',
                system_name = '',
                thread_number = 56,
                username = '',
                job_type = '',
        )

    def testJobSummary(self):
        """Test JobSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
