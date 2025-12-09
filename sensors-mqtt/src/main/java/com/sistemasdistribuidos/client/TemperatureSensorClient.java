package com.sistemasdistribuidos.client;

import org.eclipse.paho.client.mqttv3.MqttClient;
import com.google.gson.Gson;

import com.sistemasdistribuidos.controller.TemperatureController;
import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.sensors.TemperatureSensor;

public class TemperatureSensorClient {

    public static void main(String[] args) {

        String broker = "tcp://broker.emqx.io:1883";
        String clientId = "thermometer-1";
        String topic = "estufa/sensores/temperatura";

        try {
            MqttClient client = new MqttClient(broker, clientId);
            client.connect();
            System.out.println("Conectado ao broker");

            MqttPublisher publisher = new MqttPublisher(client);
            Gson gson = new Gson();

            TemperatureSensor sensor = new TemperatureSensor();
            TemperatureController controller =
                    new TemperatureController(sensor, clientId);

            while (true) {

                SensorData data = controller.readData();
                String json = gson.toJson(data);

                publisher.publish(topic, json);
                System.out.println("Publicado [Temperatura] -> " + json);

                Thread.sleep(6000); // 60 segundos
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
