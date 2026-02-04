from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

from .base import ArtifactBase

CheckStatus = Literal["pass", "fail", "warning", "not_tested"]

class AssumptionCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    status: CheckStatus
    message: str = ""
    evidence: dict = Field(default_factory=dict)


class AssumptionReport(ArtifactBase):
    model_config = ConfigDict(extra="forbid")

    module: str = Field(default="C2")

    proceed: bool
    blocking_reasons: list[str] = Field(default_factory=list)

    checks: list[AssumptionCheck] = Field(default_factory=list)

    fallback_suggestion: dict = Field(default_factory=dict)
