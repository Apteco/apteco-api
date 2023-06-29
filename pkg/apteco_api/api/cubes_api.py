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


class CubesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cubes_calculate_cube_synchronously(self, data_view_name, system_name, **kwargs):  # noqa: E501
        """EXPERIMENTAL: Calcaultes a cube using the given definition and returns the results.  The data to build the cube from is defined by the base query provided.  # noqa: E501

        EXPERIMENTAL  Requires licence flags [Cube]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cubes_calculate_cube_synchronously(data_view_name, system_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param system_name: The name of the FastStats system to act on (required)
        :type system_name: str
        :param timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration
        :type timeout_in_seconds: int
        :param return_definition: Whether to include the cube's definition in the results.  Default is false.
        :type return_definition: bool
        :param cube: The cube definition to use
        :type cube: Cube
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
        :rtype: CubeResult
        """
        kwargs['_return_http_data_only'] = True
        return self.cubes_calculate_cube_synchronously_with_http_info(data_view_name, system_name, **kwargs)  # noqa: E501

    def cubes_calculate_cube_synchronously_with_http_info(self, data_view_name, system_name, **kwargs):  # noqa: E501
        """EXPERIMENTAL: Calcaultes a cube using the given definition and returns the results.  The data to build the cube from is defined by the base query provided.  # noqa: E501

        EXPERIMENTAL  Requires licence flags [Cube]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cubes_calculate_cube_synchronously_with_http_info(data_view_name, system_name, async_req=True)
        >>> result = thread.get()

        :param data_view_name: The name of the DataView to act on (required)
        :type data_view_name: str
        :param system_name: The name of the FastStats system to act on (required)
        :type system_name: str
        :param timeout_in_seconds: The number of seconds before the request will time out.  Leave unspecified to use the default value given in the analysis service's configuration
        :type timeout_in_seconds: int
        :param return_definition: Whether to include the cube's definition in the results.  Default is false.
        :type return_definition: bool
        :param cube: The cube definition to use
        :type cube: Cube
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
        :rtype: tuple(CubeResult, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'data_view_name',
            'system_name',
            'timeout_in_seconds',
            'return_definition',
            'cube'
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
                    " to method cubes_calculate_cube_synchronously" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_view_name' is set
        if self.api_client.client_side_validation and ('data_view_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_view_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_view_name` when calling `cubes_calculate_cube_synchronously`")  # noqa: E501
        # verify the required parameter 'system_name' is set
        if self.api_client.client_side_validation and ('system_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['system_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `system_name` when calling `cubes_calculate_cube_synchronously`")  # noqa: E501

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

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cube' in local_var_params:
            body_params = local_var_params['cube']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json', 'application/xml', 'text/xml', 'application/*+xml'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['faststats_auth']  # noqa: E501

        response_types_map = {
            200: "CubeResult",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            '/{dataViewName}/Cubes/{systemName}/CalculateSync', 'POST',
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
