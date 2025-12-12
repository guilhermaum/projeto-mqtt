from core.MqttBaseService import MqttBaseService

class AggregatorService:
    def __init__(self, input_topic, output_topic, ca_cert, event_bus):
        self.mqtt = MqttBaseService(
            client_id=f"avg-{input_topic.replace('/','-')}",
            input_topic=input_topic,
            output_topic=output_topic,
            ca_cert=ca_cert,
            event_bus=event_bus
        )
    def start(self):
        self.mqtt.start()