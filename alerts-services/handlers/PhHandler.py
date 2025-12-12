from util.time_stamp import get_date_time_as_long

class PhHandler:
    def __init__(self, event_bus, publisher):
        self.publisher = publisher
        self.buffers = {}

        event_bus.subscribe("estufa/visao/ph.received", self.handle)

    def ensure_buffer(self, sensor_id):
        if sensor_id not in self.buffers:
            self.buffers[sensor_id] = []


    def classificar(self, ph):
        if ph < 5.5:
            return "Solo muito ácido"
        elif 5.5 <= ph < 6.5:
            return "Solo levemente ácido"
        elif 6.5 <= ph <= 7.5:
            return "Solo neutro"
        else:
            return "Solo alcalino"

    def handle(self, data):
        sensor_id = data.get("id")
        avg = data.get("avg")
        sensor_type = data.get("type")

        if sensor_id is None or avg is None:
            return

        print(f"[pH] Média recebida do sensor {sensor_id}: {avg}")

        self.ensure_buffer(sensor_id)
        self.buffers[sensor_id].append(avg)

        if len(self.buffers[sensor_id]) == 12:
            media_final = sum(self.buffers[sensor_id]) / 12
            situacao = self.classificar(media_final)
            msg = f"O ph do solo registrado na última hora foi: {round(media_final, 2)} no sensor {sensor_id}: {situacao}"

            alerta = {
                "type": sensor_type,
                "msg": msg,
                "timestamp": get_date_time_as_long()
            }

            self.publisher.publish(alerta)
            print("[pH] ALERTA enviado:", alerta)

            self.buffers[sensor_id] = []