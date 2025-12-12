import threading
import time
import os
from handlers.TemperatureHandler import TemperatureHandler
from handlers.HumidityHandler import HumidityHandler
from handlers.LuminosityHandler import LuminosityHandler
from handlers.PhHandler import PhHandler
from service.TemperatureService import TemperatureService 
from service.HumidityService import HumidityService
from service.LuminosityService import LuminosityService
from service.PhService import PhService
from core.EventBus import EventBus

def main():

    event_bus = EventBus()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CA_CERT = os.path.join(BASE_DIR, "mqtt", "emqxsl-ca.crt")

    temperature = TemperatureService(CA_CERT, event_bus)
    humidity = HumidityService(CA_CERT, event_bus)
    luminosity = LuminosityService(CA_CERT, event_bus)
    ph = PhService(CA_CERT, event_bus)

    services = [temperature, humidity, luminosity, ph]

    TemperatureHandler(event_bus, temperature.mqtt.publisher)
    HumidityHandler(event_bus, humidity.mqtt.publisher)
    LuminosityHandler(event_bus, luminosity.mqtt.publisher)
    PhHandler(event_bus, ph.mqtt.publisher)

    print("🚀 Sistema iniciado com arquitetura orientada a eventos!")

    for service in services:
        threading.Thread(target=service.start, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando...")

if __name__ == "__main__":
    main()
