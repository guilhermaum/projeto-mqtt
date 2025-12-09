package com.sistemasdistribuidos.sensors;

import com.sistemasdistribuidos.model.SensorData;

public class TemperatureSensor implements Sensor {
    
    @Override
    public SensorData read(){
        double value = 15 + Math.random() * 10;
        return new SensorData("temperature", value, System.currentTimeMillis());
    }
}
