# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from openapi_client.models.data_id import DataId
from openapi_client.models.provenance import Provenance

class ProvenanceEntry(BaseModel):
    """
    ProvenanceEntry
    """
    data: conlist(DataId) = Field(...)
    provenance: Provenance = Field(...)
    __properties = ["data", "provenance"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ProvenanceEntry:
        """Create an instance of ProvenanceEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of provenance
        if self.provenance:
            _dict['provenance'] = self.provenance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProvenanceEntry:
        """Create an instance of ProvenanceEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProvenanceEntry.parse_obj(obj)

        _obj = ProvenanceEntry.parse_obj({
            "data": [DataId.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "provenance": Provenance.from_dict(obj.get("provenance")) if obj.get("provenance") is not None else None
        })
        return _obj


