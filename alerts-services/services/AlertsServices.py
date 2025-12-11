import json
from mqtt.MqttPublisher import MqttPublisher
import paho.mqtt.client as mqtt

BROKER = "z2a78b18.ala.eu-central-1.emqxsl.com"
PORT = 8883
CA_CERT = "mqtt/emqxsl-ca.crt"
USERNAME = "guilhermaum"
PASSWORD = "12345678"

class BaseService:
    def __init__(self, client_id, input_topic, output_topic, ca_cert):
        self.client = mqtt.Client(client_id)

        # Login
        self.client.username_pw_set(USERNAME, PASSWORD)

        # TLS
        self.client.tls_set(ca_cert)
        self.client.tls_insecure_set(False)

        self.publisher = MqttPublisher(self.client, output_topic)

        self.input_topic = input_topic
        self.output_topic = output_topic
        self.client_id = client_id

        self.buffers = {}  # Armazena valores por sensor ID

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def start(self):
        print(f"🔌 Iniciando {self.client_id}...")
        self.client.connect(BROKER, PORT)
        self.client.loop_forever()

    def ensure_buffer(self, sensor_id):
        if sensor_id not in self.buffers:
            self.buffers[sensor_id] = []


class TemperaturaService(BaseService):
    def __init__(self, car_cert):
        super().__init__(
            client_id="alerta-temperatura",
            input_topic="estufa/visao/temperatura",
            output_topic="estufa/alerta/temperatura",
            ca_cert=car_cert
        )

    def on_connect(self, c, u, f, rc):
        print("[Temp] Conectado")
        c.subscribe(self.input_topic)

    def on_message(self, c, u, msg):
        payload = json.loads(msg.payload.decode())

        sensor_id = payload.get("id")
        avg = payload.get("avg")

        if sensor_id is None or avg is None:
            return

        print(f"[Temp] Média recebida do sensor {sensor_id}: {avg}")

        if 32 <= avg <= 40:
            alerta = {
                "id": sensor_id,
                "temperatura": avg,
                "alerta": "Temperatura muito alta!"
            }
            self.publisher.publish(alerta)
            print("[Temp] ALERTA enviado:", alerta)


class UmidadeService(BaseService):
    def __init__(self, ca_cert):
        super().__init__(
            client_id="alerta-umidade",
            input_topic="estufa/visao/umidade",
            output_topic="estufa/alerta/umidade",
            ca_cert=ca_cert
        )

    def on_connect(self, c, u, f, rc):
        print("[Umid] Conectado")
        c.subscribe(self.input_topic)

    def on_message(self, c, u, msg):
        payload = json.loads(msg.payload.decode())

        sensor_id = payload.get("id")
        avg = payload.get("avg")

        if sensor_id is None or avg is None:
            return

        print(f"[Umid] Média recebida do sensor {sensor_id}: {avg}")

        alerta = None
        if avg < 30:
            alerta = {"id": sensor_id, "umidade": avg, "alerta": "Umidade muito baixa!"}
        elif avg > 80:
            alerta = {"id": sensor_id, "umidade": avg, "alerta": "Umidade muito alta!"}

        if alerta:
            self.publisher.publish(alerta)
            print("[Umid] ALERTA enviado:", alerta)

class LuminosidadeService(BaseService):
    def __init__(self, ca_cert):
        super().__init__(
            client_id="alerta-luz",
            input_topic="estufa/visao/iluminacao",
            output_topic="estufa/alerta/iluminacao",
            ca_cert=ca_cert
        )
        self.buffers = {}

    def on_connect(self, c, u, f, rc):
        print("[Luz] Conectado")
        c.subscribe(self.input_topic)

    def on_message(self, c, u, msg):
        payload = json.loads(msg.payload.decode())
        sensor_id = payload.get("id")
        avg = payload.get("avg")

        if sensor_id is None or avg is None:
            return

        print(f"[Luz] Média recebida do sensor {sensor_id}: {avg}")

        self.ensure_buffer(sensor_id)
        self.buffers[sensor_id].append(avg)

        if len(self.buffers[sensor_id]) == 12:
            media_hora = sum(self.buffers[sensor_id]) / 12

            alerta = {
                "id": sensor_id,
                "periodo": "última hora",
                "media_luminosidade": round(media_hora, 2)
            }

            self.publisher.publish(alerta)
            print("[Luz] ALERTA enviado:", alerta)

            self.buffers[sensor_id] = []


class PhService(BaseService):
    def __init__(self, ca_cert):
        super().__init__(
            client_id="alerta-ph",
            input_topic="estufa/visao/ph",
            output_topic="estufa/alerta/ph",
            ca_cert=ca_cert
        )
        self.buffers = {}

    def classificar(self, ph):
        if ph < 5.5:
            return "Solo muito ácido"
        elif 5.5 <= ph < 6.5:
            return "Solo levemente ácido"
        elif 6.5 <= ph <= 7.5:
            return "Solo neutro"
        else:
            return "Solo alcalino"

    def on_connect(self, c, u, f, rc):
        print("[pH] Conectado")
        c.subscribe(self.input_topic)

    def on_message(self, c, u, msg):
        payload = json.loads(msg.payload.decode())
        sensor_id = payload.get("id")
        avg = payload.get("avg")

        if sensor_id is None or avg is None:
            return

        print(f"[pH] Média recebida do sensor {sensor_id}: {avg}")

        self.ensure_buffer(sensor_id)
        self.buffers[sensor_id].append(avg)

        if len(self.buffers[sensor_id]) == 12:
            media_final = sum(self.buffers[sensor_id]) / 12
            situacao = self.classificar(media_final)

            alerta = {
                "id": sensor_id,
                "ph_medio_hora": round(media_final, 2),
                "situacao_solo": situacao
            }

            self.publisher.publish(alerta)
            print("[pH] ALERTA enviado:", alerta)

            self.buffers[sensor_id] = []