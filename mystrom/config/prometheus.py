from pydantic import BaseSettings
from typing import List
from driconfig import DriConfig

class PrometheusConfig(BaseSettings):

    #: Scape interval in seconds
    scrape_interval: int = 15

    #: Port to expose metrics endpoint
    port: int = 8000

  
class AppConfig(DriConfig):
   """Interface for the config/config.yaml file."""

   class Config:
       """Configure the YAML file location."""

       config_folder = "."
       config_file_name = "config.yml"

   prometheus: PrometheusConfig
   ips: List[str]
