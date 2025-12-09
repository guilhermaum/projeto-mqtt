package com.sistemasdistribuidos.client;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.controller.PhController;
import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.sensors.PhSensor;

public class PhSensorClient {

    public static void main(String[] args) {

        String broker = "tcp://broker.emqx.io:1883";
        String clientId = "phMeter-1";
        String topic = "estufa/sensores/ph";

        try {
            MqttClient client = new MqttClient(broker, clientId);
            client.connect();
            System.out.println("Conectado ao broker");

            MqttPublisher publisher = new MqttPublisher(client);
            Gson gson = new Gson();

            PhSensor sensor = new PhSensor();
            PhController controller = new PhController(sensor, clientId);

            while (true) {

                SensorData data = controller.readData();
                String json = gson.toJson(data);

                publisher.publish(topic, json);
                System.out.println("Publicado [Nível de PH] -> " + json);

                Thread.sleep(60000);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
