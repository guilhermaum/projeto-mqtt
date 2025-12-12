package com.sistemasdistribuidos.client;

import java.util.Arrays;
import java.util.List;

import javax.net.ssl.SSLContext;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.controller.LuminosityController;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.mqtt.MqttConnector;
import com.sistemasdistribuidos.mqtt.TLSUtil;

public class LuminositySensorClient {

    public static void main(String[] args) {

        String broker = "ssl://z2a78b18.ala.eu-central-1.emqxsl.com:8883";
        String clientId = "photosensor-1";
        String topic = "estufa/sensores/iluminacao";
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

            List<LuminosityController> controllers = Arrays.asList(
                    new LuminosityController("photo-01"),
                    new LuminosityController("photo-02"),
                    new LuminosityController("photo-03"),
                    new LuminosityController("photo-04"),
                    new LuminosityController("photo-05"),
                    new LuminosityController("photo-06"),
                    new LuminosityController("photo-07"),
                    new LuminosityController("photo-08"),
                    new LuminosityController("photo-09"),
                    new LuminosityController("photo-10")
            );

            while (true) {

                for (LuminosityController controller : controllers) {
                    String json = gson.toJson(controller.readData());
                    publisher.publish(topic, json);
                    System.out.println("Publicado [Luminosidade] -> " + json);
                }
                Thread.sleep(6000);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
