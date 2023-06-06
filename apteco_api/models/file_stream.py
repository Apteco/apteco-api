# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from apteco_api.configuration import Configuration


class FileStream(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'handle': 'object',
        'can_read': 'bool',
        'can_write': 'bool',
        'safe_file_handle': 'SafeFileHandle',
        'name': 'str',
        'is_async': 'bool',
        'length': 'int',
        'position': 'int',
        'can_seek': 'bool',
        'can_timeout': 'bool',
        'read_timeout': 'int',
        'write_timeout': 'int'
    }

    attribute_map = {
        'handle': 'handle',
        'can_read': 'canRead',
        'can_write': 'canWrite',
        'safe_file_handle': 'safeFileHandle',
        'name': 'name',
        'is_async': 'isAsync',
        'length': 'length',
        'position': 'position',
        'can_seek': 'canSeek',
        'can_timeout': 'canTimeout',
        'read_timeout': 'readTimeout',
        'write_timeout': 'writeTimeout'
    }

    def __init__(self, handle=None, can_read=None, can_write=None, safe_file_handle=None, name=None, is_async=None, length=None, position=None, can_seek=None, can_timeout=None, read_timeout=None, write_timeout=None, local_vars_configuration=None):  # noqa: E501
        """FileStream - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._handle = None
        self._can_read = None
        self._can_write = None
        self._safe_file_handle = None
        self._name = None
        self._is_async = None
        self._length = None
        self._position = None
        self._can_seek = None
        self._can_timeout = None
        self._read_timeout = None
        self._write_timeout = None
        self.discriminator = None

        if handle is not None:
            self.handle = handle
        if can_read is not None:
            self.can_read = can_read
        if can_write is not None:
            self.can_write = can_write
        if safe_file_handle is not None:
            self.safe_file_handle = safe_file_handle
        if name is not None:
            self.name = name
        if is_async is not None:
            self.is_async = is_async
        if length is not None:
            self.length = length
        if position is not None:
            self.position = position
        if can_seek is not None:
            self.can_seek = can_seek
        if can_timeout is not None:
            self.can_timeout = can_timeout
        if read_timeout is not None:
            self.read_timeout = read_timeout
        if write_timeout is not None:
            self.write_timeout = write_timeout

    @property
    def handle(self):
        """Gets the handle of this FileStream.  # noqa: E501


        :return: The handle of this FileStream.  # noqa: E501
        :rtype: object
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this FileStream.


        :param handle: The handle of this FileStream.  # noqa: E501
        :type: object
        """

        self._handle = handle

    @property
    def can_read(self):
        """Gets the can_read of this FileStream.  # noqa: E501


        :return: The can_read of this FileStream.  # noqa: E501
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        """Sets the can_read of this FileStream.


        :param can_read: The can_read of this FileStream.  # noqa: E501
        :type: bool
        """

        self._can_read = can_read

    @property
    def can_write(self):
        """Gets the can_write of this FileStream.  # noqa: E501


        :return: The can_write of this FileStream.  # noqa: E501
        :rtype: bool
        """
        return self._can_write

    @can_write.setter
    def can_write(self, can_write):
        """Sets the can_write of this FileStream.


        :param can_write: The can_write of this FileStream.  # noqa: E501
        :type: bool
        """

        self._can_write = can_write

    @property
    def safe_file_handle(self):
        """Gets the safe_file_handle of this FileStream.  # noqa: E501


        :return: The safe_file_handle of this FileStream.  # noqa: E501
        :rtype: SafeFileHandle
        """
        return self._safe_file_handle

    @safe_file_handle.setter
    def safe_file_handle(self, safe_file_handle):
        """Sets the safe_file_handle of this FileStream.


        :param safe_file_handle: The safe_file_handle of this FileStream.  # noqa: E501
        :type: SafeFileHandle
        """

        self._safe_file_handle = safe_file_handle

    @property
    def name(self):
        """Gets the name of this FileStream.  # noqa: E501


        :return: The name of this FileStream.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileStream.


        :param name: The name of this FileStream.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_async(self):
        """Gets the is_async of this FileStream.  # noqa: E501


        :return: The is_async of this FileStream.  # noqa: E501
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        """Sets the is_async of this FileStream.


        :param is_async: The is_async of this FileStream.  # noqa: E501
        :type: bool
        """

        self._is_async = is_async

    @property
    def length(self):
        """Gets the length of this FileStream.  # noqa: E501


        :return: The length of this FileStream.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this FileStream.


        :param length: The length of this FileStream.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def position(self):
        """Gets the position of this FileStream.  # noqa: E501


        :return: The position of this FileStream.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this FileStream.


        :param position: The position of this FileStream.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def can_seek(self):
        """Gets the can_seek of this FileStream.  # noqa: E501


        :return: The can_seek of this FileStream.  # noqa: E501
        :rtype: bool
        """
        return self._can_seek

    @can_seek.setter
    def can_seek(self, can_seek):
        """Sets the can_seek of this FileStream.


        :param can_seek: The can_seek of this FileStream.  # noqa: E501
        :type: bool
        """

        self._can_seek = can_seek

    @property
    def can_timeout(self):
        """Gets the can_timeout of this FileStream.  # noqa: E501


        :return: The can_timeout of this FileStream.  # noqa: E501
        :rtype: bool
        """
        return self._can_timeout

    @can_timeout.setter
    def can_timeout(self, can_timeout):
        """Sets the can_timeout of this FileStream.


        :param can_timeout: The can_timeout of this FileStream.  # noqa: E501
        :type: bool
        """

        self._can_timeout = can_timeout

    @property
    def read_timeout(self):
        """Gets the read_timeout of this FileStream.  # noqa: E501


        :return: The read_timeout of this FileStream.  # noqa: E501
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this FileStream.


        :param read_timeout: The read_timeout of this FileStream.  # noqa: E501
        :type: int
        """

        self._read_timeout = read_timeout

    @property
    def write_timeout(self):
        """Gets the write_timeout of this FileStream.  # noqa: E501


        :return: The write_timeout of this FileStream.  # noqa: E501
        :rtype: int
        """
        return self._write_timeout

    @write_timeout.setter
    def write_timeout(self, write_timeout):
        """Sets the write_timeout of this FileStream.


        :param write_timeout: The write_timeout of this FileStream.  # noqa: E501
        :type: int
        """

        self._write_timeout = write_timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileStream):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileStream):
            return True

        return self.to_dict() != other.to_dict()
