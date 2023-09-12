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



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.permission import Permission
from openapi_client.models.resource import Resource

class PermissionRequest(BaseModel):
    """
    Request for adding a new permission to the given role on the given resource
    """
    permission: Permission = Field(...)
    resource: Resource = Field(...)
    role_id: StrictStr = Field(..., alias="roleId")
    __properties = ["permission", "resource", "roleId"]

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
    def from_json(cls, json_str: str) -> PermissionRequest:
        """Create an instance of PermissionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PermissionRequest:
        """Create an instance of PermissionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PermissionRequest.parse_obj(obj)

        _obj = PermissionRequest.parse_obj({
            "permission": obj.get("permission"),
            "resource": Resource.from_dict(obj.get("resource")) if obj.get("resource") is not None else None,
            "role_id": obj.get("roleId")
        })
        return _obj


