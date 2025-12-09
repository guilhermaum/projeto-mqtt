package com.sistemasdistribuidos.sensors;

import com.sistemasdistribuidos.model.SensorData;

public class HumiditySensor implements Sensor {

    @Override
    public SensorData read() {
        double humidity = Math.random() * 100;
        return new SensorData("humidity", humidity, System.currentTimeMillis());
    }
 
}
