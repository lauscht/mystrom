from pydantic import BaseModel

class Report(BaseModel):
    power: float
    Ws: float
    relay: bool
    temperature: float