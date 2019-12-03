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
VERSION = "0.2.0"
README = "introduction.md"

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, README), encoding='utf-8') as f:
    long_description = f.read()

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
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.apteco.com/",
	author="Apteco Ltd",
    author_email="support@apteco.com",
	license="Apache 2.0",
	classifiers=[
		"License :: OSI Approved :: Apache Software License",
		"Development Status :: 4 - Beta",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
	],
    keywords=[
		"Apteco",
		"Apteco API",
		"Apteco Marketing Suite",
		"Apteco FastStats",
		"FastStats",
		"Apteco Orbit",
		"Orbit",
		"OpenAPI",
		"OpenAPI-Generator",
		"Swagger",
		"Swagger API",
		"API",
		"REST",
	],
    install_requires=REQUIRES,
    packages=["apteco_api", "apteco_api.api", "apteco_api.models"],
    include_package_data=True,
)
