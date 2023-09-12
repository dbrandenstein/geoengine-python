# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class WcsVersion(str, Enum):
    """
    WcsVersion
    """

    """
    allowed enum values
    """
    ENUM_1_DOT_1_DOT_0 = '1.1.0'
    ENUM_1_DOT_1_DOT_1 = '1.1.1'

    @classmethod
    def from_json(cls, json_str: str) -> WcsVersion:
        """Create an instance of WcsVersion from a JSON string"""
        return WcsVersion(json.loads(json_str))


