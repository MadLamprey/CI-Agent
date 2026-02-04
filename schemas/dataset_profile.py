from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class ColumnProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    inferred_type: Literal["numeric", "binary", "categorical", "datetime", "text", "unknown"]
    n_unique: int
    missing_frac: float  # Between 0 and 1
    is_likely_id: bool = False
    is_likely_time: bool = False

class DatasetProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dataset_name: str
    n_rows: int
    n_cols: int
    columns: list[ColumnProfile]