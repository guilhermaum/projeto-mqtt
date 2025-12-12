from core.MqttBaseService import MqttBaseService
from util.time_stamp import get_date_time_as_long

class HumidityService:
    def __init__(self, ca_cert, event_bus):
        self.mqtt = MqttBaseService(
            client_id="alerta-umidade",
            input_topic="estufa/visao/umidade",
            output_topic="estufa/alerta/umidade",
            ca_cert=ca_cert,
            event_bus=event_bus
        )

    def start(self):
        self.mqtt.start()