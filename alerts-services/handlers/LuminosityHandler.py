from util.time_stamp import get_date_time_as_long

class LuminosityHandler:
    def __init__(self, event_bus, publisher):
        self.publisher = publisher
        self.buffers = {}

        event_bus.subscribe("estufa/visao/iluminacao.received", self.handle)

    def ensure_buffer(self, sensor_id):
        if sensor_id not in self.buffers:
            self.buffers[sensor_id] = []
            
    def handle(self, data):
        sensor_id = data.get("id")
        avg = data.get("avg")
        sensor_type = data.get("type")

        if sensor_id is None or avg is None:
            return

        print(f"[Luz] Média recebida do sensor {sensor_id}: {avg}")

        self.ensure_buffer(sensor_id)
        self.buffers[sensor_id].append(avg)

        if len(self.buffers[sensor_id]) == 12:
            media_hora = sum(self.buffers[sensor_id]) / 12
            msg = f"Na última hora foi registrado uma média de {round(media_hora, 2)} no sensor {sensor_id}"
            
            alerta = {
                "type": sensor_type,
                "msg": msg,
                "timestamp": get_date_time_as_long()
            }

            self.publisher.publish(alerta)
            print("[Luz] ALERTA enviado:", alerta)

            self.buffers[sensor_id] = []