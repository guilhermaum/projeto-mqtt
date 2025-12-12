from core.MqttBaseService import MqttBaseService
from util.time_stamp import get_date_time_as_long

class PhService:
    def __init__(self, ca_cert, event_bus):
        self.mqtt = MqttBaseService(
            client_id="alerta-ph",
            input_topic="estufa/visao/ph",
            output_topic="estufa/alerta/ph",
            ca_cert=ca_cert,
            event_bus=event_bus
        )

    def start(self):
        self.mqtt.start()