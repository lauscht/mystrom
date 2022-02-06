from enum import Enum
from pydantic import BaseModel


class Type(int, Enum):
    Switch_CH_v1 = 101
    Bulb = 102
    Button_plus = 103
    Button = 104
    LED_strip = 105
    Switch_CH_v2 = 106
    Switch_EU = 107


class Info(BaseModel):
    version: str
    mac: str
    ssid: str
    ip: str
    type: Type