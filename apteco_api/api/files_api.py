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


class FilesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def files_delete_file(self, data_view_name, system_name, file_path, **kwargs):  # noqa: E501
        """Deletes file at location  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_delete_file(data_view_name, system_name, file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param str file_path: The path to the file to be deleted (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration
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
        return self.files_delete_file_with_http_info(data_view_name, system_name, file_path, **kwargs)  # noqa: E501

    def files_delete_file_with_http_info(self, data_view_name, system_name, file_path, **kwargs):  # noqa: E501
        """Deletes file at location  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_delete_file_with_http_info(data_view_name, system_name, file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param str file_path: The path to the file to be deleted (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration
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

        all_params = ['data_view_name', 'system_name', 'file_path', 'timeout_in_seconds']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_delete_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `files_delete_file`")  # noqa: E501
        # verify the required parameter 'system_name' is set
        if ('system_name' not in local_var_params or
                local_var_params['system_name'] is None):
            raise ApiValueError("Missing the required parameter `system_name` when calling `files_delete_file`")  # noqa: E501
        # verify the required parameter 'file_path' is set
        if ('file_path' not in local_var_params or
                local_var_params['file_path'] is None):
            raise ApiValueError("Missing the required parameter `file_path` when calling `files_delete_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'system_name' in local_var_params:
            path_params['systemName'] = local_var_params['system_name']  # noqa: E501
        if 'file_path' in local_var_params:
            path_params['filePath'] = local_var_params['file_path']  # noqa: E501

        query_params = []
        if 'timeout_in_seconds' in local_var_params:
            query_params.append(('timeoutInSeconds', local_var_params['timeout_in_seconds']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Files/{systemName}/{filePath}', 'DELETE',
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

    def files_get_file(self, data_view_name, system_name, file_path, **kwargs):  # noqa: E501
        """Returns the contents for a file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_file(data_view_name, system_name, file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param str file_path: The path of the file to return the contents for (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.files_get_file_with_http_info(data_view_name, system_name, file_path, **kwargs)  # noqa: E501

    def files_get_file_with_http_info(self, data_view_name, system_name, file_path, **kwargs):  # noqa: E501
        """Returns the contents for a file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_get_file_with_http_info(data_view_name, system_name, file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param str file_path: The path of the file to return the contents for (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(file, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['data_view_name', 'system_name', 'file_path', 'timeout_in_seconds']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_get_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `files_get_file`")  # noqa: E501
        # verify the required parameter 'system_name' is set
        if ('system_name' not in local_var_params or
                local_var_params['system_name'] is None):
            raise ApiValueError("Missing the required parameter `system_name` when calling `files_get_file`")  # noqa: E501
        # verify the required parameter 'file_path' is set
        if ('file_path' not in local_var_params or
                local_var_params['file_path'] is None):
            raise ApiValueError("Missing the required parameter `file_path` when calling `files_get_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'system_name' in local_var_params:
            path_params['systemName'] = local_var_params['system_name']  # noqa: E501
        if 'file_path' in local_var_params:
            path_params['filePath'] = local_var_params['file_path']  # noqa: E501

        query_params = []
        if 'timeout_in_seconds' in local_var_params:
            query_params.append(('timeoutInSeconds', local_var_params['timeout_in_seconds']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Files/{systemName}/{filePath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def files_upsert_file(self, data_view_name, system_name, file_path, file, **kwargs):  # noqa: E501
        """Creates or updates a file at a location  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_upsert_file(data_view_name, system_name, file_path, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param str file_path: The path in the system where the file will be put (required)
        :param file file: The file to upload. (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FileEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.files_upsert_file_with_http_info(data_view_name, system_name, file_path, file, **kwargs)  # noqa: E501

    def files_upsert_file_with_http_info(self, data_view_name, system_name, file_path, file, **kwargs):  # noqa: E501
        """Creates or updates a file at a location  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.files_upsert_file_with_http_info(data_view_name, system_name, file_path, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str system_name: The name of the FastStats system to act on (required)
        :param str file_path: The path in the system where the file will be put (required)
        :param file file: The file to upload. (required)
        :param int timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the file service's configuration
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FileEntry, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['data_view_name', 'system_name', 'file_path', 'file', 'timeout_in_seconds']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method files_upsert_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `files_upsert_file`")  # noqa: E501
        # verify the required parameter 'system_name' is set
        if ('system_name' not in local_var_params or
                local_var_params['system_name'] is None):
            raise ApiValueError("Missing the required parameter `system_name` when calling `files_upsert_file`")  # noqa: E501
        # verify the required parameter 'file_path' is set
        if ('file_path' not in local_var_params or
                local_var_params['file_path'] is None):
            raise ApiValueError("Missing the required parameter `file_path` when calling `files_upsert_file`")  # noqa: E501
        # verify the required parameter 'file' is set
        if ('file' not in local_var_params or
                local_var_params['file'] is None):
            raise ApiValueError("Missing the required parameter `file` when calling `files_upsert_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'system_name' in local_var_params:
            path_params['systemName'] = local_var_params['system_name']  # noqa: E501
        if 'file_path' in local_var_params:
            path_params['filePath'] = local_var_params['file_path']  # noqa: E501

        query_params = []
        if 'timeout_in_seconds' in local_var_params:
            query_params.append(('timeoutInSeconds', local_var_params['timeout_in_seconds']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        return self.api_client.call_api(
            '/{dataViewName}/Files/{systemName}/{filePath}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
