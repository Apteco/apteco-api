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


class TemporaryFilesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def temporary_files_get_temporary_file(self, data_view_name, id, **kwargs):  # noqa: E501
        """Returns the contents of a temporary file with the given id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_get_temporary_file(data_view_name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id of the temporary file to return the contents for (required)
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
        return self.temporary_files_get_temporary_file_with_http_info(data_view_name, id, **kwargs)  # noqa: E501

    def temporary_files_get_temporary_file_with_http_info(self, data_view_name, id, **kwargs):  # noqa: E501
        """Returns the contents of a temporary file with the given id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_get_temporary_file_with_http_info(data_view_name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id of the temporary file to return the contents for (required)
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

        all_params = ['data_view_name', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method temporary_files_get_temporary_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `temporary_files_get_temporary_file`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `temporary_files_get_temporary_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

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
            '/{dataViewName}/TemporaryFiles/{id}', 'GET',
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

    def temporary_files_get_temporary_file_part(self, data_view_name, id, part_number, **kwargs):  # noqa: E501
        """Returns the contents of a temporary file part with the given id and part number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_get_temporary_file_part(data_view_name, id, part_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id of the temporary file (required)
        :param int part_number: The number of the temporary file part to return the contents for (required)
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
        return self.temporary_files_get_temporary_file_part_with_http_info(data_view_name, id, part_number, **kwargs)  # noqa: E501

    def temporary_files_get_temporary_file_part_with_http_info(self, data_view_name, id, part_number, **kwargs):  # noqa: E501
        """Returns the contents of a temporary file part with the given id and part number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_get_temporary_file_part_with_http_info(data_view_name, id, part_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id of the temporary file (required)
        :param int part_number: The number of the temporary file part to return the contents for (required)
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

        all_params = ['data_view_name', 'id', 'part_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method temporary_files_get_temporary_file_part" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `temporary_files_get_temporary_file_part`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `temporary_files_get_temporary_file_part`")  # noqa: E501
        # verify the required parameter 'part_number' is set
        if ('part_number' not in local_var_params or
                local_var_params['part_number'] is None):
            raise ApiValueError("Missing the required parameter `part_number` when calling `temporary_files_get_temporary_file_part`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'part_number' in local_var_params:
            path_params['partNumber'] = local_var_params['part_number']  # noqa: E501

        query_params = []

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
            '/{dataViewName}/TemporaryFiles/{id}/{partNumber}', 'GET',
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

    def temporary_files_upsert_temporary_file(self, data_view_name, id, file, **kwargs):  # noqa: E501
        """Creates or updates a temporary file with the given id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_upsert_temporary_file(data_view_name, id, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id for the temporary file to create or update (required)
        :param file file: The file to upload. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TemporaryFile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.temporary_files_upsert_temporary_file_with_http_info(data_view_name, id, file, **kwargs)  # noqa: E501

    def temporary_files_upsert_temporary_file_with_http_info(self, data_view_name, id, file, **kwargs):  # noqa: E501
        """Creates or updates a temporary file with the given id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_upsert_temporary_file_with_http_info(data_view_name, id, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id for the temporary file to create or update (required)
        :param file file: The file to upload. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TemporaryFile, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['data_view_name', 'id', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method temporary_files_upsert_temporary_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `temporary_files_upsert_temporary_file`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `temporary_files_upsert_temporary_file`")  # noqa: E501
        # verify the required parameter 'file' is set
        if ('file' not in local_var_params or
                local_var_params['file'] is None):
            raise ApiValueError("Missing the required parameter `file` when calling `temporary_files_upsert_temporary_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

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
            '/{dataViewName}/TemporaryFiles/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemporaryFile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def temporary_files_upsert_temporary_file_part(self, data_view_name, id, part_number, file, **kwargs):  # noqa: E501
        """Creates or updates part of a temporary file with the given id and part number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_upsert_temporary_file_part(data_view_name, id, part_number, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id for the temporary file (required)
        :param int part_number: The number of the temporary file part to create or update (required)
        :param file file: The file to upload. (required)
        :param bool final_part: Whether this part is the final part and the full temporary file should be assembled.  If this is not specified it defaults to false
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TemporaryFilePart
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.temporary_files_upsert_temporary_file_part_with_http_info(data_view_name, id, part_number, file, **kwargs)  # noqa: E501

    def temporary_files_upsert_temporary_file_part_with_http_info(self, data_view_name, id, part_number, file, **kwargs):  # noqa: E501
        """Creates or updates part of a temporary file with the given id and part number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.temporary_files_upsert_temporary_file_part_with_http_info(data_view_name, id, part_number, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_view_name: The name of the DataView to act on (required)
        :param str id: The id for the temporary file (required)
        :param int part_number: The number of the temporary file part to create or update (required)
        :param file file: The file to upload. (required)
        :param bool final_part: Whether this part is the final part and the full temporary file should be assembled.  If this is not specified it defaults to false
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TemporaryFilePart, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['data_view_name', 'id', 'part_number', 'file', 'final_part']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method temporary_files_upsert_temporary_file_part" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if ('data_view_name' not in local_var_params or
                local_var_params['data_view_name'] is None):
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `temporary_files_upsert_temporary_file_part`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `temporary_files_upsert_temporary_file_part`")  # noqa: E501
        # verify the required parameter 'part_number' is set
        if ('part_number' not in local_var_params or
                local_var_params['part_number'] is None):
            raise ApiValueError("Missing the required parameter `part_number` when calling `temporary_files_upsert_temporary_file_part`")  # noqa: E501
        # verify the required parameter 'file' is set
        if ('file' not in local_var_params or
                local_var_params['file'] is None):
            raise ApiValueError("Missing the required parameter `file` when calling `temporary_files_upsert_temporary_file_part`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_name' in local_var_params:
            path_params['dataViewName'] = local_var_params['data_view_name']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'part_number' in local_var_params:
            path_params['partNumber'] = local_var_params['part_number']  # noqa: E501

        query_params = []
        if 'final_part' in local_var_params:
            query_params.append(('finalPart', local_var_params['final_part']))  # noqa: E501

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
            '/{dataViewName}/TemporaryFiles/{id}/{partNumber}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemporaryFilePart',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
