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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from openapi_client.models.provider_layer_id import ProviderLayerId

class LayerListingWithType(BaseModel):
    """
    LayerListingWithType
    """
    description: StrictStr = Field(...)
    id: ProviderLayerId = Field(...)
    name: StrictStr = Field(...)
    properties: Optional[conlist(conlist(StrictStr, max_items=2, min_items=2))] = Field(None, description="properties, for instance, to be rendered in the UI")
    type: StrictStr = Field(...)
    __properties = ["description", "id", "name", "properties", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('layer'):
            raise ValueError("must be one of enum values ('layer')")
        return value

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
    def from_json(cls, json_str: str) -> LayerListingWithType:
        """Create an instance of LayerListingWithType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LayerListingWithType:
        """Create an instance of LayerListingWithType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LayerListingWithType.parse_obj(obj)

        _obj = LayerListingWithType.parse_obj({
            "description": obj.get("description"),
            "id": ProviderLayerId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "name": obj.get("name"),
            "properties": obj.get("properties"),
            "type": obj.get("type")
        })
        return _obj


