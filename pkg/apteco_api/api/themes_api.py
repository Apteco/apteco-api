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


class ThemesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def themes_create_theme(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Creates a new theme from the given details for the logged in user.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_create_theme(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param CreateUpdateTheme theme_detail: The details for the theme to create.  If you want              to update a specific theme then POST to the /Theme/{themeId} URL
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Theme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.themes_create_theme_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def themes_create_theme_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Creates a new theme from the given details for the logged in user.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_create_theme_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param CreateUpdateTheme theme_detail: The details for the theme to create.  If you want              to update a specific theme then POST to the /Theme/{themeId} URL
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Theme, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'theme_detail'
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
                    " to method themes_create_theme" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `themes_create_theme`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'theme_detail' in local_var_params:
            body_params = local_var_params['theme_detail']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json', 'application/xml', 'text/xml', 'application/*+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Themes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Theme',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def themes_delete_theme(self, data_view_name, theme_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Deletes the specified theme  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_delete_theme(data_view_name, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int theme_id: The id of the theme to delete (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.themes_delete_theme_with_http_info(data_view_name, theme_id, **kwargs)  # noqa: E501

    def themes_delete_theme_with_http_info(self, data_view_name, theme_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Deletes the specified theme  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_delete_theme_with_http_info(data_view_name, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int theme_id: The id of the theme to delete (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'theme_id'
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
                    " to method themes_delete_theme" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `themes_delete_theme`")  # noqa: E501
        # verify the required parameter 'theme_id' is set
        if self.api_client.client_side_validation and ('theme_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['theme_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `theme_id` when calling `themes_delete_theme`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'theme_id' in local_var_params:
            path_params['themeId'] = local_var_params['theme_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Themes/{themeId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def themes_get_theme(self, data_view_name, theme_id, **kwargs):  # noqa: E501
        """Returns a theme for this dataview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get_theme(data_view_name, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int theme_id: The themeId of the Theme to retrieve (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Theme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.themes_get_theme_with_http_info(data_view_name, theme_id, **kwargs)  # noqa: E501

    def themes_get_theme_with_http_info(self, data_view_name, theme_id, **kwargs):  # noqa: E501
        """Returns a theme for this dataview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get_theme_with_http_info(data_view_name, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int theme_id: The themeId of the Theme to retrieve (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Theme, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'theme_id'
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
                    " to method themes_get_theme" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `themes_get_theme`")  # noqa: E501
        # verify the required parameter 'theme_id' is set
        if self.api_client.client_side_validation and ('theme_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['theme_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `theme_id` when calling `themes_get_theme`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'theme_id' in local_var_params:
            path_params['themeId'] = local_var_params['theme_id']  # noqa: E501

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
            '/{dataViewName}/Themes/{themeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Theme',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def themes_get_themes(self, data_view_name, **kwargs):  # noqa: E501
        """Returns a list of all themes for this dataview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get_themes(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Theme]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.themes_get_themes_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def themes_get_themes_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Returns a list of all themes for this dataview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get_themes_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Theme], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name'
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
                    " to method themes_get_themes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `themes_get_themes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501

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
            '/{dataViewName}/Themes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Theme]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def themes_get_usage(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns a list of all themes with associated usage information  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get_usage(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ThemeUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.themes_get_usage_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def themes_get_usage_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Returns a list of all themes with associated usage information  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get_usage_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ThemeUsage, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name'
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
                    " to method themes_get_usage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `themes_get_usage`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501

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
            '/{dataViewName}/Themes/Usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ThemeUsage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def themes_update_theme(self, data_view_name, theme_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Updates the details of a particular theme.  If you don't have an id for the  theme then POST to the /Themes URL to create a new theme.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_update_theme(data_view_name, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int theme_id: The id of the theme to add/update (required)
        :param CreateUpdateTheme theme_detail: The details for the theme to update
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Theme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.themes_update_theme_with_http_info(data_view_name, theme_id, **kwargs)  # noqa: E501

    def themes_update_theme_with_http_info(self, data_view_name, theme_id, **kwargs):  # noqa: E501
        """Requires OrbitAdmin: Updates the details of a particular theme.  If you don't have an id for the  theme then POST to the /Themes URL to create a new theme.  # noqa: E501

        This endpoint is only available for users with the OrbitAdmin role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_update_theme_with_http_info(data_view_name, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param int theme_id: The id of the theme to add/update (required)
        :param CreateUpdateTheme theme_detail: The details for the theme to update
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Theme, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'theme_id',
            'theme_detail'
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
                    " to method themes_update_theme" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `themes_update_theme`")  # noqa: E501
        # verify the required parameter 'theme_id' is set
        if self.api_client.client_side_validation and ('theme_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['theme_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `theme_id` when calling `themes_update_theme`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'theme_id' in local_var_params:
            path_params['themeId'] = local_var_params['theme_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'theme_detail' in local_var_params:
            body_params = local_var_params['theme_detail']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json', 'application/xml', 'text/xml', 'application/*+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Themes/{themeId}/Updates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Theme',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
