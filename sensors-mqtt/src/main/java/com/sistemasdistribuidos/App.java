package com.sistemasdistribuidos;

import com.sistemasdistribuidos.client.TemperatureSensorClient;
import com.sistemasdistribuidos.client.HumiditySensorClient;
import com.sistemasdistribuidos.client.LuminositySensorClient;
import com.sistemasdistribuidos.client.PhSensorClient;

public class App {

    public static void main(String[] args) {
        System.out.println("Iniciando todos os sensores...");

        Thread tempThread = new Thread(() -> {
            TemperatureSensorClient.main(new String[]{});
        });

        Thread humidityThread = new Thread(() -> {
            HumiditySensorClient.main(new String[]{});
        });

        Thread phThread = new Thread(() -> {
            PhSensorClient.main(new String[]{});
        });

        Thread lightThread = new Thread(() -> {
            LuminositySensorClient.main(new String[]{});
        });

        tempThread.start();
        humidityThread.start();
        phThread.start();
        lightThread.start();

        System.out.println("Todos os sensores foram iniciados com sucesso!");
    }
}
