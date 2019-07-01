# coding: utf-8

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "apteco-api"
VERSION = "0.1.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Apteco API",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://www.apteco.com/",
	author="Apteco Ltd",
    author_email="support@apteco.com",
	license="Apache 2.0",
    keywords=["OpenAPI", "OpenAPI-Generator", "Apteco API"],
    install_requires=REQUIRES,
    packages=["apteco_api", "apteco_api.api", "apteco_api.models"],
    include_package_data=True,
)
