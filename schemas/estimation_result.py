from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .base import ArtifactBase


class Coef(BaseModel):
    model_config = ConfigDict(extra="forbid")

    term: str
    estimate: float
    std_err: float | None = None
    p_value: float | None = None
    ci_low: float | None = None
    ci_high: float | None = None


class EstimationResult(ArtifactBase):
    model_config = ConfigDict(extra="forbid")

    module: str = Field(default="C3")

    method: str
    formula: str | None = None

    treatment_effect_term: str | None = None
    main_effect: Coef | None = None

    coefficients: list[Coef] = Field(default_factory=list)

    n_obs: int | None = None
    fit_stats: dict = Field(default_factory=dict)
    model_config: dict = Field(default_factory=dict)

    tool_raw: dict = Field(default_factory=dict)
