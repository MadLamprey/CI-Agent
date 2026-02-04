from __future__ import annotations

from typing import Literal
from pydantic import Field, ConfigDict

from .base import ArtifactBase
from .dataset_profile import DatasetProfile

Estimand = Literal["ATE", "ATT", "LATE", "CATE", "UNKNOWN"]

class ProblemCard(ArtifactBase):
    model_config = ConfigDict(extra="forbid")

    module: str = Field(default="C0")

    user_question: str
    dataset: DatasetProfile

    treatment_col: str | None = None
    outcome_col: str | None = None
    estimand: Estimand = "UNKNOWN"

    controls_hint: list[str] = Field(default_factory=list)
    subgroup_cols: list[str] = Field(default_factory=list)

    open_questions: list[str] = Field(default_factory=list)
