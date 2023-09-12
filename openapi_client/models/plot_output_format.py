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





class PlotOutputFormat(str, Enum):
    """
    PlotOutputFormat
    """

    """
    allowed enum values
    """
    JSONPLAIN = 'JsonPlain'
    JSONVEGA = 'JsonVega'
    IMAGEPNG = 'ImagePng'

    @classmethod
    def from_json(cls, json_str: str) -> PlotOutputFormat:
        """Create an instance of PlotOutputFormat from a JSON string"""
        return PlotOutputFormat(json.loads(json_str))


