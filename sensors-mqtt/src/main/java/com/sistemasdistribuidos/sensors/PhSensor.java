package com.sistemasdistribuidos.sensors;

import com.sistemasdistribuidos.model.SensorData;

public class PhSensor implements Sensor {

    @Override
    public SensorData read() {
        double ph = Math.random() * 14;
        return new SensorData("ph", ph, System.currentTimeMillis());
    }
    
}
