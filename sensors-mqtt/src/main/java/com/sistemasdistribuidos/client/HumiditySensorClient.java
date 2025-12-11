package com.sistemasdistribuidos.client;

import javax.net.ssl.SSLContext;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.controller.HumidityController;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.mqtt.MqttConnector;
import com.sistemasdistribuidos.sensors.HumiditySensor;
import com.sistemasdistribuidos.mqtt.TLSUtil;

public class HumiditySensorClient {

    public static void main(String[] args) {

        String broker = "ssl://z2a78b18.ala.eu-central-1.emqxsl.com:8883";
        String clientId = "hygrometer-1";
        String topic = "estufa/sensores/umidade";
        String username = "guilhermaum";
        String password = "12345678";

        // Caminho do certificado CA
        // String caFilePath = "src/main/resources/emqxsl-ca.crt";

        try {
            // Criar contexto SSL
            SSLContext sslContext = TLSUtil.createSSLContext("emqxsl-ca.crt");

            // Conectar usando a classe separada
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

            HumiditySensor sensor = new HumiditySensor();
            HumidityController controller = new HumidityController(sensor, clientId);

            while (true) {

                String json = gson.toJson(controller.readData());

                publisher.publish(topic, json);
                System.out.println("Publicado [Umidade] -> " + json);

                Thread.sleep(60000);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
