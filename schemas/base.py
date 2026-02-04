from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Status = Literal["ok", "warning", "error"]


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class ArtifactBase(BaseModel):
    """
    Base fields for every component.
    """
    model_config = ConfigDict(extra="forbid")

    schema_version: str = Field(default="0.1")
    run_id: str
    created_at: datetime = Field(default_factory=utcnow)
    module: str  # Eg: "C0", "C5", "INTROSPECTOR" etc.
    status: Status = Field(default="ok")
    errors: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
