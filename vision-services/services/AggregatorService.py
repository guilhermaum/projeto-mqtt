import json
import time
import threading
import paho.mqtt.client as mqtt
from mqtt.MqttPublisher import MqttPublisher

class AggregatorService:

    def __init__(self, broker, port, input_topic, output_topic, client_id):
        self.broker = broker
        self.port = port
        self.input_topic = input_topic
        self.output_topic = output_topic
        self.client_id = client_id
        self.last_values = []

        self.buffers = {}

        self.client = mqtt.Client(client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.publisher = MqttPublisher(self.client, output_topic)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"🔌 [{self.client_id}] Conectado")
            client.subscribe(self.input_topic)
            print(f"📡 [{self.client_id}] Inscrito em {self.input_topic}")
        else:
            print(f"❌ [{self.client_id}] Erro ao conectar: {rc}")

    def on_message(self, client, userdata, message):
        payload = json.loads(message.payload.decode())

        value = payload.get("value")
        sensor_type = payload.get("type")
        sensor_id = payload.get("id")

        if value is None or sensor_id is None:
            print(f"⚠️ [{self.client_id}] Payload ignorado (faltando 'value' ou 'id'):", payload)
            return

        if sensor_id not in self.buffers:
            self.buffers[sensor_id] = []

        buffer = self.buffers[sensor_id]
        buffer.append(value)

        if len(buffer) == 5:
            avg = sum(buffer) / 5

            out_payload = {
                "id": sensor_id,
                "type": sensor_type,
                "avg": avg,
                "timestamp": int(time.time() * 1000)
            }

            print(f"📤 [{self.client_id}] Publicando média do sensor [{sensor_id}]:", out_payload)
            self.publisher.publish(out_payload)

            self.buffers[sensor_id] = []


    def start_in_thread(self):
        t = threading.Thread(target=self.start)
        t.daemon = True
        t.start()

    def start(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()
