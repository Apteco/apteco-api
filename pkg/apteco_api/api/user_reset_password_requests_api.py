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


class UserResetPasswordRequestsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_reset_password_requests_confirm_reset_password_request(self, data_view_name, token, **kwargs):  # noqa: E501
        """Confirms a given reset password request and changes the password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_confirm_reset_password_request(data_view_name, token, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param token: The token of the request (required)
        :type token: str
        :param confirm_reset_password_request: The details needed to confirm the reset password request
        :type confirm_reset_password_request: ConfirmResetPasswordRequest
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.user_reset_password_requests_confirm_reset_password_request_with_http_info(data_view_name, token, **kwargs)  # noqa: E501

    def user_reset_password_requests_confirm_reset_password_request_with_http_info(self, data_view_name, token, **kwargs):  # noqa: E501
        """Confirms a given reset password request and changes the password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_confirm_reset_password_request_with_http_info(data_view_name, token, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param token: The token of the request (required)
        :type token: str
        :param confirm_reset_password_request: The details needed to confirm the reset password request
        :type confirm_reset_password_request: ConfirmResetPasswordRequest
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'token',
            'confirm_reset_password_request'
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
                    " to method user_reset_password_requests_confirm_reset_password_request" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `user_reset_password_requests_confirm_reset_password_request`")  # noqa: E501
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `user_reset_password_requests_confirm_reset_password_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'token' in local_var_params:
            path_params['token'] = local_var_params['token']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'confirm_reset_password_request' in local_var_params:
            body_params = local_var_params['confirm_reset_password_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json', 'application/xml', 'text/xml', 'application/*+xml'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            '/{dataViewName}/UserResetPasswordRequests/{token}', 'POST',
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

    def user_reset_password_requests_create_reset_password_request(self, data_view_name, **kwargs):  # noqa: E501
        """Creates a new reset password requests, which will check that the provided email address exists and then issue a confirmation notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_create_reset_password_request(data_view_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param create_reset_password_request: The details needed to create the reset password request
        :type create_reset_password_request: CreateResetPasswordRequest
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
        :rtype: ResetPasswordRequestDetail
        """
        kwargs['_return_http_data_only'] = True
        return self.user_reset_password_requests_create_reset_password_request_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def user_reset_password_requests_create_reset_password_request_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Creates a new reset password requests, which will check that the provided email address exists and then issue a confirmation notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_create_reset_password_request_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param create_reset_password_request: The details needed to create the reset password request
        :type create_reset_password_request: CreateResetPasswordRequest
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
        :rtype: tuple(ResetPasswordRequestDetail, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'create_reset_password_request'
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
                    " to method user_reset_password_requests_create_reset_password_request" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `user_reset_password_requests_create_reset_password_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_reset_password_request' in local_var_params:
            body_params = local_var_params['create_reset_password_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json', 'application/xml', 'text/xml', 'application/*+xml'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            201: "ResetPasswordRequestDetail",
            400: None,
            404: None,
        }

        return self.api_client.call_api(
            '/{dataViewName}/UserResetPasswordRequests', 'POST',
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

    def user_reset_password_requests_get_reset_password_request(self, data_view_name, token, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns details for a given reset password request  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_get_reset_password_request(data_view_name, token, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param token: The token of the request (required)
        :type token: str
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
        :rtype: ResetPasswordRequestDetail
        """
        kwargs['_return_http_data_only'] = True
        return self.user_reset_password_requests_get_reset_password_request_with_http_info(data_view_name, token, **kwargs)  # noqa: E501

    def user_reset_password_requests_get_reset_password_request_with_http_info(self, data_view_name, token, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns details for a given reset password request  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_get_reset_password_request_with_http_info(data_view_name, token, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param token: The token of the request (required)
        :type token: str
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
        :rtype: tuple(ResetPasswordRequestDetail, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'token'
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
                    " to method user_reset_password_requests_get_reset_password_request" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `user_reset_password_requests_get_reset_password_request`")  # noqa: E501
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `user_reset_password_requests_get_reset_password_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'token' in local_var_params:
            path_params['token'] = local_var_params['token']  # noqa: E501

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
            200: "ResetPasswordRequestDetail",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            '/{dataViewName}/UserResetPasswordRequests/{token}', 'GET',
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

    def user_reset_password_requests_get_reset_password_requests(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all the current reset password requests in the system.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_get_reset_password_requests(data_view_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param filter: Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate
        :type filter: str
        :param order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate
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
        :rtype: PagedResultsUserRegistrationRequestSummary
        """
        kwargs['_return_http_data_only'] = True
        return self.user_reset_password_requests_get_reset_password_requests_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def user_reset_password_requests_get_reset_password_requests_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns all the current reset password requests in the system.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_reset_password_requests_get_reset_password_requests_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param filter: Filter the list of items using a simple expression language.  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate
        :type filter: str
        :param order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Username, EmailAddress, CreationDate, ConfirmedDate, ExpiredDate
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
        :rtype: tuple(PagedResultsUserRegistrationRequestSummary, status_code(int), headers(HTTPHeaderDict))
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
                    " to method user_reset_password_requests_get_reset_password_requests" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `user_reset_password_requests_get_reset_password_requests`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `user_reset_password_requests_get_reset_password_requests`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `user_reset_password_requests_get_reset_password_requests`, must be a value greater than or equal to `0`")  # noqa: E501
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
            200: "PagedResultsUserRegistrationRequestSummary",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            '/{dataViewName}/UserResetPasswordRequests', 'GET',
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
