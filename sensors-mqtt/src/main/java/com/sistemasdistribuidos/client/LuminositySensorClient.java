package com.sistemasdistribuidos.client;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.controller.LuminosityController;
import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.sensors.LuminositySensor;

public class LuminositySensorClient {
    
    public static void main(String[] args) {

        String broker = "tcp://broker.emqx.io:1883";
        String clientId = "photosensor-1";
        String topic = "estufa/sensores/iluminacao";

        try {
            MqttClient client = new MqttClient(broker, clientId);
            client.connect();
            System.out.println("Conectado ao broker");

            MqttPublisher publisher = new MqttPublisher(client);
            Gson gson = new Gson();

            LuminositySensor sensor = new LuminositySensor();
            LuminosityController controller = new LuminosityController(sensor, clientId);

            while (true) {

                SensorData data = controller.readData();
                String json = gson.toJson(data);

                publisher.publish(topic, json);
                System.out.println("Publicado [Luminosidade] -> " + json);

                Thread.sleep(60000);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
