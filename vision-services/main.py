'''import os

from services.AggregatorService import AggregatorService

from topics.topics import (
    SENSOR_UMIDADE, MEDIA_UMIDADE,
    SENSOR_TEMPERATURA, MEDIA_TEMPERATURA,
    SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE,
    SENSOR_PH, MEDIA_PH
)

def main():
    BROKER = "z2a78b18.ala.eu-central-1.emqxsl.com"
    PORT = 8883
    USERNAME = "guilhermaum"
    PASSWORD = "12345678"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CA_CERT = os.path.join(BASE_DIR, "mqtt", "emqxsl-ca.crt")


    services = [
        AggregatorService(BROKER, PORT, SENSOR_UMIDADE, MEDIA_UMIDADE, "agregador-umidade",
                          USERNAME, PASSWORD, CA_CERT),
        AggregatorService(BROKER, PORT, SENSOR_TEMPERATURA, MEDIA_TEMPERATURA, "agregador-temperatura",
                          USERNAME, PASSWORD, CA_CERT),
        AggregatorService(BROKER, PORT, SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE, "agregador-luminosidade",
                          USERNAME, PASSWORD, CA_CERT),
        AggregatorService(BROKER, PORT, SENSOR_PH, MEDIA_PH, "agregador-ph",
                          USERNAME, PASSWORD, CA_CERT),
    ]

    for service in services:
        service.start_in_thread()

    print("Todos os agregadores estão rodando...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Encerrando...")


if __name__ == "__main__":
    main()'''

import os
import threading
from core.EventBus import EventBus
from service.AggregatorService import AggregatorService
from handlers.AggregatorHandler import AggregatorHandler
from core.MqttPublisher import MqttPublisher

from topics.topics import (
    SENSOR_UMIDADE, MEDIA_UMIDADE,
    SENSOR_TEMPERATURA, MEDIA_TEMPERATURA,
    SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE,
    SENSOR_PH, MEDIA_PH
)

def add_aggregator(input_topic, output_topic, CA_CERT, event_bus, services, handlers):
        service = AggregatorService(
            input_topic, output_topic, CA_CERT,
            event_bus
        )
        publisher = MqttPublisher(service.mqtt.client, output_topic)
        handler = AggregatorHandler(event_bus, input_topic, publisher)
        services.append(service)
        handlers.append(handler)

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CA_CERT = os.path.join(BASE_DIR, "mqtt", "emqxsl-ca.crt")

    event_bus = EventBus()

    services = []
    handlers = []

    add_aggregator(SENSOR_UMIDADE, MEDIA_UMIDADE, CA_CERT, event_bus, services, handlers)
    add_aggregator(SENSOR_TEMPERATURA, MEDIA_TEMPERATURA, CA_CERT, event_bus, services, handlers)
    add_aggregator(SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE, CA_CERT, event_bus, services, handlers)
    add_aggregator(SENSOR_PH, MEDIA_PH, CA_CERT, event_bus, services, handlers)

    for svc in services:
        threading.Thread(target=svc.start, daemon=True).start()

    print("Todos os agregadores em execução...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Encerrando...")

if __name__ == "__main__":
    main()

