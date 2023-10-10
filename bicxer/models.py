import enum
import pydantic


class FilterKey(str, enum.Enum):
    FROM = "from"
    TO = "to"


class Operator(str, enum.Enum):
    EQUAL = "eq"


class FilterItem(pydantic.BaseModel):
    value: str
    key: FilterKey
    op: Operator
