package com.sistemasdistribuidos.client;

import org.eclipse.paho.client.mqttv3.MqttClient;

import com.google.gson.Gson;
import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.sensors.HumiditySensor;

public class HumiditySensorClient {
    public static void main(String args[]){
        String broker = "tcp://broker.emqx.io:1883";
        String clientId = "hygrometer-1";
        String topic = "estufa/sensores/umidade";

        try{

            MqttClient client = new MqttClient(broker, clientId);
            client.connect();
            System.out.println("Conectado ao broker");

            MqttPublisher publisher = new MqttPublisher(client);
            Gson gson = new Gson();

            HumiditySensor hygrometer = new HumiditySensor();

            while(true){

                SensorData data = hygrometer.read();
                publisher.publish(topic, gson.toJson(data));
                System.out.println("Publicado [Umidade] -> " + gson.toJson(data));

                Thread.sleep(60000);
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
