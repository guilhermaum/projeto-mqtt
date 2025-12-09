package com.sistemasdistribuidos.client;

import org.eclipse.paho.client.mqttv3.MqttClient;
import com.google.gson.Gson;
import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.mqtt.MqttPublisher;
import com.sistemasdistribuidos.sensors.TemperatureSensor;

public class TemperatureSensorClient{

    public static void main(String args[]){
        String broker = "tcp://broker.emqx.io:1883";
        String clientId = "thermometer-1";
        String topic = "estufa/sensores/temperatura";

        try{

            MqttClient client = new MqttClient(broker, clientId);
            client.connect();
            System.out.println("Conectado ao broker");

            MqttPublisher publisher = new MqttPublisher(client);
            Gson gson = new Gson();

            TemperatureSensor thermometer = new TemperatureSensor();

            while(true){

                SensorData data = thermometer.read();
                publisher.publish(topic, gson.toJson(data));
                System.out.println("Publicado [Temperatura] -> " + gson.toJson(data));

                Thread.sleep(60000);
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    } 

}