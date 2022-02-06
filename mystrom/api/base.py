import requests
from typing import Any
from enum import Enum
from pydantic import BaseModel

class Method(str, Enum):
    POST = 'post'
    GET = 'get'


class Api(BaseModel):
    url: str
    
    
class Endpoint(BaseModel):
    model: Any
    uri: str
        
    api: Api = None
    query: BaseModel = None
    parameter: BaseModel = None
    method: Method = Method.GET
    
    def __call__(self):
        uri = f"{self.api.url}{self.uri}"
        request = requests.request(self.method.value, uri)
        instance = self.model.parse_raw(request.content)
        return instance
