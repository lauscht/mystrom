from prometheus_client import start_http_server, Gauge
import time

from mystrom.models.info import Type
from mystrom.api.rest import RestApi
from mystrom.config.prometheus import AppConfig


config = AppConfig()

apis = [RestApi(f"http://{ip}") for ip in config.ips]
apis = [api for api in apis if api.info().type == Type.Switch_EU]

labelnames = ('name', 'mac')
labels = [(api.settings().name, api.info().mac) for api in apis]

power = Gauge('mystrom_switch_power', 'Power in watts', labelnames)
temperature = Gauge('mystrom_switch_temperature', 'Temperature in degC', labelnames)
relay = Gauge('mystrom_switch_relay', 'Relay state 0=off, 1=on', labelnames)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(config.prometheus.port)
    while True:
        for label, api in zip(labels, apis):
            report = api.report()
            power.labels(*label).set(report.power)
            temperature.labels(*label).set(report.temperature)
            relay.labels(*label).set(float(report.relay))

        time.sleep(config.prometheus.scrape_interval)
        