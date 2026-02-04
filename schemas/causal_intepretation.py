from __future__ import annotations

from pydantic import ConfigDict, Field

from .base import ArtifactBase

class CausalInterpretation(ArtifactBase):
    model_config = ConfigDict(extra="forbid")

    module: str = Field(default="C5")

    summary: str
    identification_claim: str

    key_assumptions: list[str] = Field(default_factory=list)

    estimated_effect: str | None = None
    uncertainty_note: str = ""

    limitations: list[str] = Field(default_factory=list)
    next_steps: list[str] = Field(default_factory=list)
