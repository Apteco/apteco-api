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

import apteco_api
from apteco_api.api.collections_api import CollectionsApi  # noqa: E501
from apteco_api.rest import ApiException


class TestCollectionsApi(unittest.TestCase):
    """CollectionsApi unit test stubs"""

    def setUp(self):
        self.api = apteco_api.api.collections_api.CollectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_collections_create_collection(self):
        """Test case for collections_create_collection

        Creates a new collection from the given details for the logged in user.  # noqa: E501
        """
        pass

    def test_collections_create_collection_hit_for_collection(self):
        """Test case for collections_create_collection_hit_for_collection

        Register a hit (view) for the given collection  # noqa: E501
        """
        pass

    def test_collections_delete_collection(self):
        """Test case for collections_delete_collection

        Deletes the specified collection  # noqa: E501
        """
        pass

    def test_collections_get_collection(self):
        """Test case for collections_get_collection

        Returns the details of a particular collection  # noqa: E501
        """
        pass

    def test_collections_get_collection_hit_for_collection(self):
        """Test case for collections_get_collection_hit_for_collection

        Returns details for a given collection hit for this collection  # noqa: E501
        """
        pass

    def test_collections_get_collection_hits_for_collection(self):
        """Test case for collections_get_collection_hits_for_collection

        Returns a summary of the hits for this collection - i.e. information about when users have viewed the collection.  # noqa: E501
        """
        pass

    def test_collections_get_collection_part(self):
        """Test case for collections_get_collection_part

        Returns details of a part contained within a particular collection  # noqa: E501
        """
        pass

    def test_collections_get_collection_parts(self):
        """Test case for collections_get_collection_parts

        Returns a summary of the parts contained within a particular collection  # noqa: E501
        """
        pass

    def test_collections_get_collections(self):
        """Test case for collections_get_collections

        Requires OrbitAdmin: Gets summary information about each collection in the DataView.  # noqa: E501
        """
        pass

    def test_collections_transfer_collection_ownership(self):
        """Test case for collections_transfer_collection_ownership

        Transfer ownership of a collection from the current user to a new owner  # noqa: E501
        """
        pass

    def test_collections_upsert_collection(self):
        """Test case for collections_upsert_collection

        Updates the details of a particular collection.  If you don't have an id for the  collection then POST to the /Collections URL to create a new collection.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
