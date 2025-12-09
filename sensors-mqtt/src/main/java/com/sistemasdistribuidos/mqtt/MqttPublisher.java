package com.sistemasdistribuidos.mqtt;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class MqttPublisher {
    
    private final MqttClient client;
    
    public MqttPublisher(MqttClient client){
        this.client = client;
    }

    public void publish(String topic, String payload) throws MqttException{
        MqttMessage msg = new MqttMessage(payload.getBytes());
        msg.setQos(1);
        client.publish(topic, msg);
    }
}
