# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from apteco_api.api_client import ApiClient
from apteco_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def groups_get_group_details(self, data_view_name, group_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns details for the given group  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_group_details(data_view_name, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int group_id: The id of the group to view the details for (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UserDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_get_group_details_with_http_info(data_view_name, group_id, **kwargs)  # noqa: E501

    def groups_get_group_details_with_http_info(self, data_view_name, group_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns details for the given group  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_group_details_with_http_info(data_view_name, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int group_id: The id of the group to view the details for (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UserDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_get_group_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `groups_get_group_details`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_get_group_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Groups/{groupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def groups_get_groups(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all groups in the DataView.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_groups(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Name
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name
        :param int offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :param int count: The maximum number of items to show from the (potentially filtered) result set.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResultsGroupSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_get_groups_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def groups_get_groups_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all groups in the DataView.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_groups_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Name
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name
        :param int offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :param int count: The maximum number of items to show from the (potentially filtered) result set.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedResultsGroupSummary, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'filter',
            'order_by',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_get_groups" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `groups_get_groups`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `groups_get_groups`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `groups_get_groups`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501

        query_params = []
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResultsGroupSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def groups_get_user_details_for_group(self, data_view_name, group_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all users in the given group.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_user_details_for_group(data_view_name, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int group_id: The id of the group to get users for (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param int offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :param int count: The maximum number of items to show from the (potentially filtered) result set.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResultsUserSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_get_user_details_for_group_with_http_info(data_view_name, group_id, **kwargs)  # noqa: E501

    def groups_get_user_details_for_group_with_http_info(self, data_view_name, group_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all users in the given group.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_user_details_for_group_with_http_info(data_view_name, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int group_id: The id of the group to get users for (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param int offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :param int count: The maximum number of items to show from the (potentially filtered) result set.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedResultsUserSummary, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'group_id',
            'filter',
            'order_by',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_get_user_details_for_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `groups_get_user_details_for_group`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_get_user_details_for_group`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `groups_get_user_details_for_group`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `groups_get_user_details_for_group`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = []
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Groups/{groupId}/Users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResultsUserSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def groups_get_user_details_for_unallocated_group(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all users that haven't been allocated to a group.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_user_details_for_unallocated_group(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param int offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :param int count: The maximum number of items to show from the (potentially filtered) result set.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResultsUserSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_get_user_details_for_unallocated_group_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def groups_get_user_details_for_unallocated_group_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all users that haven't been allocated to a group.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_user_details_for_unallocated_group_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, Firstname, Surname, UserDisabledDate
        :param int offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :param int count: The maximum number of items to show from the (potentially filtered) result set.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedResultsUserSummary, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'filter',
            'order_by',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_get_user_details_for_unallocated_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `groups_get_user_details_for_unallocated_group`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `groups_get_user_details_for_unallocated_group`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `groups_get_user_details_for_unallocated_group`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501

        query_params = []
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Groups/Unallocated/Users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResultsUserSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
