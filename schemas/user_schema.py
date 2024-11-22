from __future__ import annotations
from typing import Union  # Import Union for compatibility

from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    is_active: bool = True

    class Config:
        orm_mode = True


class UpdateUserSchema(BaseModel):
    name: Union[str, None] = None  # Use Union for optional fields
    email: Union[str, None] = None
    is_active: Union[bool, None] = None  # Use Union for optional fields

    class Config:
        orm_mode = True
