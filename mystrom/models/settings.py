from pydantic import BaseModel


class Settings(BaseModel):
    rest: bool
    panel: bool
    name: str
    temp_offset: float