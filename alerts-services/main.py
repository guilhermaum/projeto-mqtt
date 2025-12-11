import threading
import time
import os
from services.AlertsServices import TemperaturaService, UmidadeService, LuminosidadeService, PhService

def main():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CA_CERT = os.path.join(BASE_DIR, "mqtt", "emqxsl-ca.crt")

    services = [
        TemperaturaService(CA_CERT),
        UmidadeService(CA_CERT),
        LuminosidadeService(CA_CERT),
        PhService(CA_CERT)
    ]

    for service in services:
        t = threading.Thread(target=service.start, daemon=True)
        t.start()

    print("🚀 Todos os serviços foram iniciados!")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando...")


if __name__ == "__main__":
    main()
