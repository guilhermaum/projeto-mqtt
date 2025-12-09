import json
from paho.mqtt.client import Client

class MqttPublisher:

    def __init__(self, client: Client, output_topic):
        self.client = client
        self.output_topic = output_topic

    def publish(self, payload):
        if isinstance(payload, dict):
            payload = json.dumps(payload)

        payload_bytes = payload.encode("utf-8")
        self.client.publish(self.output_topic, payload_bytes, qos=1)
