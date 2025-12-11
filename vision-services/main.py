from services.AggregatorService import AggregatorService

from topics.topics import (
    SENSOR_UMIDADE, MEDIA_UMIDADE,
    SENSOR_TEMPERATURA, MEDIA_TEMPERATURA,
    SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE,
    SENSOR_PH, MEDIA_PH
)

def main():
    BROKER = "z2a78b18.ala.eu-central-1.emqxsl.com"
    PORT = 8883
    USERNAME = "guilhermaum"
    PASSWORD = "12345678"
    CA_CERT = "mqtt/emqxsl-ca.crt"

    services = [
        AggregatorService(BROKER, PORT, SENSOR_UMIDADE, MEDIA_UMIDADE, "agregador-umidade",
                          USERNAME, PASSWORD, CA_CERT),
        AggregatorService(BROKER, PORT, SENSOR_TEMPERATURA, MEDIA_TEMPERATURA, "agregador-temperatura",
                          USERNAME, PASSWORD, CA_CERT),
        AggregatorService(BROKER, PORT, SENSOR_LUMINOSIDADE, MEDIA_LUMINOSIDADE, "agregador-luminosidade",
                          USERNAME, PASSWORD, CA_CERT),
        AggregatorService(BROKER, PORT, SENSOR_PH, MEDIA_PH, "agregador-ph",
                          USERNAME, PASSWORD, CA_CERT),
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
