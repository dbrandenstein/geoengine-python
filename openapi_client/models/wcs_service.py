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





class WcsService(str, Enum):
    """
    WcsService
    """

    """
    allowed enum values
    """
    WCS = 'WCS'

    @classmethod
    def from_json(cls, json_str: str) -> WcsService:
        """Create an instance of WcsService from a JSON string"""
        return WcsService(json.loads(json_str))


