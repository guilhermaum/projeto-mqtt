package com.sistemasdistribuidos.mqtt;

import javax.net.ssl.SSLContext;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;

public class MqttConnector {

    public static MqttClient connect(
            String broker,
            String clientId,
            String username,
            String password,
            SSLContext sslContext
    ) throws Exception {

        MqttConnectOptions options = new MqttConnectOptions();
        options.setCleanSession(true);
        options.setUserName(username);
        options.setPassword(password.toCharArray());

        // TLS
        if (sslContext != null) {
            options.setSocketFactory(sslContext.getSocketFactory());
        }

        // Criar cliente
        MqttClient client = new MqttClient(broker, clientId);

        // Conectar
        client.connect(options);

        return client;
    }
}
