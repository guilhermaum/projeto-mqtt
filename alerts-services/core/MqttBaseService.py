import json
import paho.mqtt.client as mqtt
from core.MqttPublisher import MqttPublisher

BROKER = "z2a78b18.ala.eu-central-1.emqxsl.com"
PORT = 8883
USERNAME = "guilhermaum"
PASSWORD = "12345678"

class MqttBaseService:
    def __init__(self, client_id, input_topic, output_topic, ca_cert, event_bus):
        self.event_bus = event_bus
        self.input_topic = input_topic
        self.output_topic = output_topic

        self.client = mqtt.Client(client_id)
        self.client.username_pw_set(USERNAME, PASSWORD)
        self.client.tls_set(ca_cert)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

        self.publisher = MqttPublisher(self.client, output_topic)

    def start(self):
        print(f"🔌 Iniciando {self.input_topic} ...")
        self.client.connect(BROKER, PORT)
        self.client.loop_start()

    def _on_connect(self, c, u, f, rc):
        print(f"[MQTT] Conectado e ouvindo {self.input_topic}")
        c.subscribe(self.input_topic)

    def _on_message(self, c, u, msg):
        data = json.loads(msg.payload.decode())
        self.event_bus.emit(f"{self.input_topic}.received", data)