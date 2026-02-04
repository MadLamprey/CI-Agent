from pydantic import BaseModel
from typing import Literal

class ColumnProfile(BaseModel):
    name: str
    inferred_type: Literal["numeric","binary","categorical","datetime","text","unknown"]
    n_unique: int
    missing_frac: int
    is_likely_id: bool
    is_likely_time: bool

class DatasetProfile(BaseModel):
    dataset_name: str
    n_rows: int
    n_cols: int
    columns: list[ColumnProfile]