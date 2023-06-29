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


class AudienceHitsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def audience_hits_get_audience_hit(self, data_view_name, audience_hit_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns details for a given audience hit  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audience_hits_get_audience_hit(data_view_name, audience_hit_id, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param audience_hit_id: The id of the hit (required)
        :type audience_hit_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AudienceHitDetail
        """
        kwargs['_return_http_data_only'] = True
        return self.audience_hits_get_audience_hit_with_http_info(data_view_name, audience_hit_id, **kwargs)  # noqa: E501

    def audience_hits_get_audience_hit_with_http_info(self, data_view_name, audience_hit_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns details for a given audience hit  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audience_hits_get_audience_hit_with_http_info(data_view_name, audience_hit_id, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param audience_hit_id: The id of the hit (required)
        :type audience_hit_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AudienceHitDetail, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'audience_hit_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method audience_hits_get_audience_hit" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `audience_hits_get_audience_hit`")  # noqa: E501
        # verify the required parameter 'audience_hit_id' is set
        if self.api_client.client_side_validation and ('audience_hit_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['audience_hit_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `audience_hit_id` when calling `audience_hits_get_audience_hit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'audience_hit_id' in local_var_params:
            path_params['audienceHitId'] = local_var_params['audience_hit_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        response_types_map = {
            200: "AudienceHitDetail",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            '/{dataViewName}/AudienceHits/{audienceHitId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def audience_hits_get_audience_hits(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all the hit information for all audiences.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audience_hits_get_audience_hits(data_view_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param filter: Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails
        :type filter: str
        :param order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, Timestamp, UserAgentDetails
        :type order_by: str
        :param offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :type offset: int
        :param count: The maximum number of items to show from the (potentially filtered) result set.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PagedResultsAudienceHitSummary
        """
        kwargs['_return_http_data_only'] = True
        return self.audience_hits_get_audience_hits_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def audience_hits_get_audience_hits_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all the hit information for all audiences.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audience_hits_get_audience_hits_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param filter: Filter the list of items using a simple expression language.  The available list of fields are Username, Timestamp, UserAgentDetails
        :type filter: str
        :param order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, Timestamp, UserAgentDetails
        :type order_by: str
        :param offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :type offset: int
        :param count: The maximum number of items to show from the (potentially filtered) result set.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PagedResultsAudienceHitSummary, status_code(int), headers(HTTPHeaderDict))
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
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method audience_hits_get_audience_hits" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `audience_hits_get_audience_hits`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `audience_hits_get_audience_hits`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `audience_hits_get_audience_hits`, must be a value greater than or equal to `0`")  # noqa: E501
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

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        response_types_map = {
            200: "PagedResultsAudienceHitSummary",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            '/{dataViewName}/AudienceHits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
