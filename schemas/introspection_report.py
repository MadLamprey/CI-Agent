from __future__ import annotations

from pydantic import ConfigDict, Field

from .base import ArtifactBase


class IntrospectionReport(ArtifactBase):
    model_config = ConfigDict(extra="forbid")

    module: str = Field(default="INTROSPECTOR")

    trigger_stage: str
    trigger_reason: str

    actions_taken: list[str] = Field(default_factory=list)
    updated_fields: dict = Field(default_factory=dict)
