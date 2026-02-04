from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

from .base import ArtifactBase

MethodName = Literal["OLS", "FE", "IV", "DID", "RD", "PSM"]

class MethodCandidate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    method: MethodName
    score: float
    rationale: str

    required_columns: list[str] = Field(default_factory=list)
    optional_columns: list[str] = Field(default_factory=list)
    blocking_questions: list[str] = Field(default_factory=list)

    config: dict = Field(default_factory=dict)


class MethodCard(ArtifactBase):
    model_config = ConfigDict(extra="forbid")

    module: str = Field(default="C1")

    chosen_method: MethodName
    chosen_rationale: str

    ranked_candidates: list[MethodCandidate] = Field(default_factory=list)
