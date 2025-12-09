import threading
import time
from services.AlertsServices import TemperaturaService, UmidadeService, LuminosidadeService, PhService

def main():
    services = [
        TemperaturaService(),
        UmidadeService(),
        LuminosidadeService(),
        PhService()
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
