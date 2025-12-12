from util.time_stamp import get_date_time_as_long

class TemperatureHandler:
    def __init__(self, event_bus, publisher):
        self.publisher = publisher
        event_bus.subscribe("estufa/visao/temperatura.received", self.handle)

    def handle(self, data):
        sensor_type = data.get("type")
        sensor_id = data.get("id")
        avg = data.get("avg")

        if sensor_type is None or avg is None:
            return

        print(f"[Temp] Média recebida do sensor {sensor_type}: {avg}")

        if 32 <= avg <= 40:
            msg = f"CUIDADO: Temperatura muito alta detectada no {sensor_id}: {avg}"
            
            alerta = {
                "type": sensor_type,
                "msg": msg,
                "timestamp": get_date_time_as_long()
            }
            self.publisher.publish(alerta)
            print("[Temp] ALERTA enviado:", alerta)
