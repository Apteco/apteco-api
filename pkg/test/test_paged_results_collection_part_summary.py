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
from apteco_api.models.paged_results_collection_part_summary import PagedResultsCollectionPartSummary  # noqa: E501
from apteco_api.rest import ApiException

class TestPagedResultsCollectionPartSummary(unittest.TestCase):
    """PagedResultsCollectionPartSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResultsCollectionPartSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = apteco_api.models.paged_results_collection_part_summary.PagedResultsCollectionPartSummary()  # noqa: E501
        if include_optional :
            return PagedResultsCollectionPartSummary(
                offset = 56, 
                count = 56, 
                total_count = 56, 
                list = [
                    apteco_api.models.collection_part_summary.CollectionPartSummary(
                        title = '0', 
                        index = 56, 
                        visualisation_type = 'None', 
                        visualisation_id = '0', )
                    ]
            )
        else :
            return PagedResultsCollectionPartSummary(
                offset = 56,
                count = 56,
                total_count = 56,
                list = [
                    apteco_api.models.collection_part_summary.CollectionPartSummary(
                        title = '0', 
                        index = 56, 
                        visualisation_type = 'None', 
                        visualisation_id = '0', )
                    ],
        )

    def testPagedResultsCollectionPartSummary(self):
        """Test PagedResultsCollectionPartSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
