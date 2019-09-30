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
from apteco_api.exceptions import (
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

    def exports_perform_export_synchronously(self, data_view_name, system_name, **kwargs):  # noqa: E501
        """EXPERIMENTAL: Exports data using the given export definition and returns the results.  The results might contain the actual data in the \"rows\" part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.  # noqa: E501

        EXPERIMENTAL  Requires licence flags [Export]  # noqa: E501
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
        """EXPERIMENTAL: Exports data using the given export definition and returns the results.  The results might contain the actual data in the \"rows\" part of the result or this might be written to a file.  The data to be exported is defined by the base query provided, along with any limits defined in the export request.  # noqa: E501

        EXPERIMENTAL  Requires licence flags [Export]  # noqa: E501
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

        all_params = ['data_view_name', 'system_name', 'timeout_in_seconds', 'return_definition', 'export']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exports_perform_export_synchronously" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `exports_perform_export_synchronously`")  # noqa: E501
        # verify the required parameter 'system_name' is set
        if ('system_name' not in local_var_params or
                local_var_params['system_name'] is None):
            raise ApiValueError("Missing the required parameter `system_name` when calling `exports_perform_export_synchronously`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'system_name' in local_var_params:
            path_params['systemName'] = local_var_params['system_name']  # noqa: E501

        query_params = []
        if 'timeout_in_seconds' in local_var_params:
            query_params.append(('timeoutInSeconds', local_var_params['timeout_in_seconds']))  # noqa: E501
        if 'return_definition' in local_var_params:
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
