from util.time_stamp import get_date_time_as_long

class AggregatorHandler:
    def __init__(self, event_bus, input_topic, publisher):
        self.input_topic = input_topic
        self.publisher = publisher
        self.buffers = {}

        event_bus.subscribe(f"{input_topic}.received", self.handle)

    def handle(self, payload):
        value = payload.get("value")
        sensor_type = payload.get("type")
        sensor_id = payload.get("id")

        if value is None or sensor_id is None:
            print(f"⚠️ [AGG {self.input_topic}] Payload inválido:", payload)
            return

        if sensor_id not in self.buffers:
            self.buffers[sensor_id] = []

        self.buffers[sensor_id].append(value)

        if len(self.buffers[sensor_id]) == 5:
            avg = sum(self.buffers[sensor_id]) / 5

            out_payload = {
                "id": sensor_id,
                "type": sensor_type,
                "avg": avg,
                "timestamp": get_date_time_as_long()
            }

            print(f"📤 Média calculada [{sensor_id}] →", out_payload)
            self.publisher.publish(out_payload)

            self.buffers[sensor_id] = []