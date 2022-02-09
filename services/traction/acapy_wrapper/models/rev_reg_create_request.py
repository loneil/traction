# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class RevRegCreateRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevRegCreateRequest - a model defined in OpenAPI

        credential_definition_id: The credential_definition_id of this RevRegCreateRequest [Optional].
        max_cred_num: The max_cred_num of this RevRegCreateRequest [Optional].
    """

    credential_definition_id: Optional[str] = None
    max_cred_num: Optional[int] = None

    @validator("credential_definition_id")
    def credential_definition_id_pattern(cls, value):
        assert value is not None and re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$",
            value,
        )
        return value

    @validator("max_cred_num")
    def max_cred_num_max(cls, value):
        assert value <= 32768
        return value

    @validator("max_cred_num")
    def max_cred_num_min(cls, value):
        assert value >= 4
        return value


RevRegCreateRequest.update_forward_refs()