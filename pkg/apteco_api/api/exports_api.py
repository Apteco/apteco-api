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


class ExportsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def exports_get_export_system(self, data_view_name, system_name, **kwargs):  # noqa: E501
        """SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level details for the specified FastStats system to export from  # noqa: E501

        SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exports_get_export_system(data_view_name, system_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to return details for (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExportSystemDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.exports_get_export_system_with_http_info(data_view_name, system_name, **kwargs)  # noqa: E501

    def exports_get_export_system_with_http_info(self, data_view_name, system_name, **kwargs):  # noqa: E501
        """SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns some top-level details for the specified FastStats system to export from  # noqa: E501

        SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exports_get_export_system_with_http_info(data_view_name, system_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to return details for (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExportSystemDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'system_name'
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
                    " to method exports_get_export_system" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `exports_get_export_system`")  # noqa: E501
        # verify the required parameter 'system_name' is set
        if self.api_client.client_side_validation and ('system_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['system_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `system_name` when calling `exports_get_export_system`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'system_name' in local_var_params:
            path_params['systemName'] = local_var_params['system_name']  # noqa: E501

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
            '/{dataViewName}/Exports/{systemName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportSystemDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def exports_get_export_systems(self, data_view_name, **kwargs):  # noqa: E501
        """SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for exporting data from  # noqa: E501

        SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exports_get_export_systems(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Name.
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name.
        :param int offset: The number of items to skip in the (potentially filtered) result set before returning subsequent items.
        :param int count: The maximum number of items to show from the (potentially filtered) result set.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResultsExportSystemSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.exports_get_export_systems_with_http_info(data_view_name, **kwargs)  # noqa: E501

    def exports_get_export_systems_with_http_info(self, data_view_name, **kwargs):  # noqa: E501
        """SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE: Returns the list of FastStats systems available for exporting data from  # noqa: E501

        SUBJECT TO CHANGE OR REMOVAL WITHOUT NOTICE  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exports_get_export_systems_with_http_info(data_view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str filter: Filter the list of items using a simple expression language.  The available list of fields are Name.
        :param str order_by: Order the items by a given field (in ascending order unless the field is preceeded by a \"-\" character).  The available list of fields are Name.
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
        :return: tuple(PagedResultsExportSystemSummary, status_code(int), headers(HTTPHeaderDict))
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
                    " to method exports_get_export_systems" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `exports_get_export_systems`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `exports_get_export_systems`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `exports_get_export_systems`, must be a value greater than or equal to `0`")  # noqa: E501
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
            '/{dataViewName}/Exports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResultsExportSystemSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def exports_perform_export_synchronously(self, data_view_name, system_name, **kwargs):  # noqa: E501
        """Exports data using the given export definition and returns the results.  The results might contain the actual data in the \"rows\" part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.  # noqa: E501

        Requires licence flags [Export]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exports_perform_export_synchronously(data_view_name, system_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration
        :param bool return_definition: Whether to include the export's definition in the results.  Default is false.
        :param Export export: The export definition to use
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExportResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.exports_perform_export_synchronously_with_http_info(data_view_name, system_name, **kwargs)  # noqa: E501

    def exports_perform_export_synchronously_with_http_info(self, data_view_name, system_name, **kwargs):  # noqa: E501
        """Exports data using the given export definition and returns the results.  The results might contain the actual data in the \"rows\" part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.  # noqa: E501

        Requires licence flags [Export]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exports_perform_export_synchronously_with_http_info(data_view_name, system_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration
        :param bool return_definition: Whether to include the export's definition in the results.  Default is false.
        :param Export export: The export definition to use
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExportResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'system_name',
            'timeout_in_seconds',
            'return_definition',
            'export'
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
                    " to method exports_perform_export_synchronously" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `exports_perform_export_synchronously`")  # noqa: E501
        # verify the required parameter 'system_name' is set
        if self.api_client.client_side_validation and ('system_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['system_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `system_name` when calling `exports_perform_export_synchronously`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'system_name' in local_var_params:
            path_params['systemName'] = local_var_params['system_name']  # noqa: E501

        query_params = []
        if 'timeout_in_seconds' in local_var_params and local_var_params['timeout_in_seconds'] is not None:  # noqa: E501
            query_params.append(('timeoutInSeconds', local_var_params['timeout_in_seconds']))  # noqa: E501
        if 'return_definition' in local_var_params and local_var_params['return_definition'] is not None:  # noqa: E501
            query_params.append(('returnDefinition', local_var_params['return_definition']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'export' in local_var_params:
            body_params = local_var_params['export']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json', 'application/xml', 'text/xml', 'application/*+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Exports/{systemName}/ExportSync', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
