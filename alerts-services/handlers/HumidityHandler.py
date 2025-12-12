from util.time_stamp import get_date_time_as_long

class HumidityHandler:
    def __init__(self, event_bus, publisher):
        self.publisher = publisher
        event_bus.subscribe("estufa/visao/umidade.received", self.handle)

    def handle(self, data):
        sensor_id = data.get("id")
        sensor_type = data.get("type")
        avg = data.get("avg")

        if sensor_id is None or avg is None:
            return

        print(f"[Umid] Média recebida do sensor {sensor_id}: {avg}")

        alerta = None
        if avg < 30:
            msg = f"ALERTA: Umidade muito baixa detectada no sensor {sensor_id}: {avg}"
            
            alerta = {
                "type": sensor_type,
                "msg": msg, 
                "timestamp": get_date_time_as_long()
                }
        elif avg > 80:
            msg = f"ALERTA: Umidade muito alta detectada no sensor {sensor_id}: {avg}"
            
            alerta = {
                "type": sensor_type,
                "msg": msg, 
                "timestamp": get_date_time_as_long()
                }
            
        if alerta:
            self.publisher.publish(alerta)
            print("[Umid] ALERTA enviado:", alerta)