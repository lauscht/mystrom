from .base import Api, Endpoint
from ..models import Info, Settings, Report


class RestApi:
    
    def __init__(self, url: str):

        self.api = Api(url=url)
        self.info = Endpoint(model=Info, uri='/api/v1/info', api=self.api)
        self.settings = Endpoint(model=Settings, uri='/api/v1/settings', api=self.api)
        self.report = Endpoint(model=Report, uri='/report', api=self.api)
