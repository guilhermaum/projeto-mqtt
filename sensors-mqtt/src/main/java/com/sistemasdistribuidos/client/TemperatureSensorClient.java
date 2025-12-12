package com.sistemasdistribuidos.client;

import java.util.Arrays;
import java.util.List;

import javax.net.ssl.SSLContext;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.controller.TemperatureController;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.mqtt.MqttConnector;
import com.sistemasdistribuidos.mqtt.TLSUtil;

public class TemperatureSensorClient {

    public static void main(String[] args) {

        String broker = "ssl://z2a78b18.ala.eu-central-1.emqxsl.com:8883";
        String clientId = "thermometer-1";
        String topic = "estufa/sensores/temperatura";
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

            List<TemperatureController> controllers = Arrays.asList(
                new TemperatureController("thermometer-01"),
                new TemperatureController("thermometer-02"),
                new TemperatureController("thermometer-03"),
                new TemperatureController("thermometer-04"),
                new TemperatureController("thermometer-05"),
                new TemperatureController("thermometer-06"),
                new TemperatureController("thermometer-07"),
                new TemperatureController("thermometer-08"),
                new TemperatureController("thermometer-09"),
                new TemperatureController("thermometer-10")
            );

            while (true) {

                for(TemperatureController controller : controllers){
                    String json = gson.toJson(controller.readData());
                    publisher.publish(topic, json);
                    System.out.println("Publicado [Temperatura] -> " + json);
                }

                Thread.sleep(6000);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
