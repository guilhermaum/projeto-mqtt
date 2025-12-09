package com.sistemasdistribuidos.sensors;

import com.sistemasdistribuidos.model.SensorData;

public class LuminositySensor implements Sensor {

    @Override
    public SensorData read() {
        double luminosity = Math.random() * 100;
        return new SensorData("luminosity", luminosity, System.currentTimeMillis());
    }


}
