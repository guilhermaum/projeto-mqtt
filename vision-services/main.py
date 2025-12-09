from services.AggregatorService import AggregatorService

from topics.topics import (
    SENSOR_UMIDADE, MEDIA_UMIDADE,
    SENSOR_TEMPERATURA, MEDIA_TEMPERATURA,
    SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE,
    SENSOR_PH, MEDIA_PH
)

def main():
    BROKER = "broker.emqx.io"
    PORT = 1883

    services = [
        AggregatorService(BROKER, PORT, SENSOR_UMIDADE, MEDIA_UMIDADE, "agregador-umidade"),
        AggregatorService(BROKER, PORT, SENSOR_TEMPERATURA, MEDIA_TEMPERATURA, "agregador-temperatura"),
        AggregatorService(BROKER, PORT, SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE, "agregador-luminosidade"),
        AggregatorService(BROKER, PORT, SENSOR_PH, MEDIA_PH, "agregador-ph"),
    ]

    for service in services:
        service.start_in_thread()

    print("Todos os agregadores estão rodando...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Encerrando...")


if __name__ == "__main__":
    main()
