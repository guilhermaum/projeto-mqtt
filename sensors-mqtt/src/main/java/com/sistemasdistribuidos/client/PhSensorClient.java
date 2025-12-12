package com.sistemasdistribuidos.client;

import java.util.Arrays;
import java.util.List;

import javax.net.ssl.SSLContext;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.controller.PhController;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.mqtt.MqttConnector;
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

            List<PhController> controllers = Arrays.asList(
                    new PhController("ph-01"),
                    new PhController("ph-02"),
                    new PhController("ph-03"),
                    new PhController("ph-04"),
                    new PhController("ph-05"),
                    new PhController("ph-06"),
                    new PhController("ph-07"),
                    new PhController("ph-08"),
                    new PhController("ph-09"),
                    new PhController("ph-10")
            );

            while (true) {

                for (PhController controller : controllers) {
                    String json = gson.toJson(controller.readData());
                    publisher.publish(topic, json);
                    System.out.println("Publicado [pH] -> " + json);
                }

                Thread.sleep(1000);
            }


        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
