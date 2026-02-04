from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .base import ArtifactBase


class RobustnessRun(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    config: dict = Field(default_factory=dict)

    main_effect: dict = Field(default_factory=dict)

    status: str = "ok"
    notes: str = ""


class RobustnessReport(ArtifactBase):
    model_config = ConfigDict(extra="forbid")

    module: str = Field(default="C4")

    runs: list[RobustnessRun] = Field(default_factory=list)

    effect_direction_consistent: bool | None = None
    effect_magnitude_range: dict = Field(default_factory=dict)
    conclusions: list[str] = Field(default_factory=list)
