package com.sistemasdistribuidos.client;

import javax.net.ssl.SSLContext;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.controller.PhController;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.mqtt.MqttConnector;
import com.sistemasdistribuidos.sensors.PhSensor;
import com.sistemasdistribuidos.mqtt.TLSUtil;

public class PhSensorClient {

    public static void main(String[] args) {

        String broker = "ssl://z2a78b18.ala.eu-central-1.emqxsl.com:8883";
        String clientId = "phMeter-1";
        String topic = "estufa/sensores/ph";
        String username = "guilhermaum";
        String password = "12345678";

        try {

            SSLContext sslContext = TLSUtil.createSSLContext("emqxsl-ca.crt");

            MqttClient client = MqttConnector.connect(
                    broker,
                    clientId,
                    username,
                    password,
                    sslContext
            );

            System.out.println("Conectado ao broker via TLS!");

            MqttPublisher publisher = new MqttPublisher(client);
            Gson gson = new Gson();

            PhSensor sensor = new PhSensor();
            PhController controller = new PhController(sensor, clientId);

            while (true) {

                String json = gson.toJson(controller.readData());

                publisher.publish(topic, json);
                System.out.println("Publicado [Nível de PH] -> " + json);

                Thread.sleep(60000);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
